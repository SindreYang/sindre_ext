# 使用CUDA 12编译MinkowskiEngine [参考自：https://github.com/NVIDIA/MinkowskiEngine/issues/543]

## 步骤1. 首先检查您的环境
```
python -c "import sys; import torch; print('Python version:', sys.version); print('Torch version:', torch.__version__); print('Torch CUDA version:', torch.version.cuda); print('CUDA available:', torch.cuda.is_available());" && gcc --version | head -n 1 | cut -d' ' -f3
```

## 步骤2. 修改`/usr/include/c++/11/bits/shared_ptr_base.h`中的共享指针定义,如果是gcc9,则改gcc9对应的文件;
将：
```
auto __raw = __to_address(__r.get())
```
替换为：
```
auto __raw = std::__to_address(__r.get())
```

## 步骤3. 安装依赖项
```
sudo apt install build-essential python3-dev libopenblas-dev
pip install ninja
```

## 步骤4. 克隆MinkowskiEngine仓库并安装

```
git clone https://github.com/NVIDIA/MinkowskiEngine.git
cd MinkowskiEngine
python setup.py install
```

## 步骤5. 如果编译失败，修改以下头文件：

1) **.../MinkowskiEngine/src/convolution_kernel.cuh**  
   添加头文件：
   ```
   #include <thrust/execution_policy.h>
   ```

2) **.../MinkowskiEngine/src/coordinate_map_gpu.cu**  
   添加头文件：
   ```
   #include <thrust/unique.h>
   #include <thrust/remove.h>
   ```

3) **.../MinkowskiEngine/src/spmm.cu**  
   添加头文件：
   ```
   #include <thrust/execution_policy.h>
   #include <thrust/reduce.h>
   #include <thrust/sort.h>
   ```

4) **.../MinkowskiEngine/src/3rdparty/concurrent_unordered_map.cuh**  
   添加头文件：
   ```
   #include <thrust/execution_policy.h>
   ```

## 步骤6. 最后，再次运行安装
```
python setup.py install
```

### 可选编译配置（如需）
```
#不再有 NVTX3 符号冲突
ext_modules = [
     Extension(
         name="MinkowskiEngineBackend._C",
         sources=[…],
+        define_macros=[('NVTX_DISABLE', None)],
         extra_compile_args={
-            'cxx': CC_FLAGS,
-            'nvcc': NVCC_FLAGS,
+            'cxx': CC_FLAGS + ['-DNVTX_DISABLE'],
+            'nvcc': NVCC_FLAGS + ['-DNVTX_DISABLE'],
         },
         libraries=libraries,
     ),
 ]
```
```
os.environ["MAX_JOBS"]="2"  # 限制并行编译任务数
os.environ["TORCH_CUDA_ARCH_LIST"] = "7.5;8.6;8.9;12.0"  # 指定目标GPU架构

python setup.py bdist_wheel --blas=openblas  # 生成OpenBLAS支持的wheel包
```
