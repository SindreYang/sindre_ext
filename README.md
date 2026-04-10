# Sindre 扩展依赖库

## 目录
- [Sindre 扩展依赖库](#sindre-扩展依赖库)
  - [目录](#目录)
  - [环境要求](#环境要求)
  - [安装说明](#安装说明)
    - [基础环境安装](#基础环境安装)
    - [扩展库安装](#扩展库安装)
      - [Windows 扩展库](#windows-扩展库)
      - [Linux 扩展库](#linux-扩展库)
  - [大模型环境推荐](#大模型环境推荐)
  - [参考链接](#参考链接)
  - [常见问题](#常见问题)

---

## 环境要求

- **CUDA**：12.8 / 12.9(驱动要求更高，对老显卡不友好）
- **Python**：3.12
- **操作系统**：Windows / Linux
- **PyTorch**：2.7.1（支持RTX 50系）
- **显卡**：1065 ~ 5090 消费级显卡  
  - 计算能力：7.5 / 8.6 / 8.9 / 12.0  
  - [Nvidia显卡计算能力查询](https://developer.nvidia.com/cuda-gpus)
- **包管理**：仅支持 pip，已去除 conda 支持

---

## 安装说明

### 基础环境安装

建议使用 `uv` 管理虚拟环境和依赖（如未安装请先 `pip install uv`）。

```shell
# 创建并激活 Python3.12 虚拟环境
uv venv
uv pip install pip

# 安装 PyTorch 2.7.1 (CUDA 12.8)
uv pip install torch==2.7.1 torchvision==0.22.1 torchaudio==2.7.1 --index-url https://download.pytorch.org/whl/cu128

# 安装图算法优化库
uv pip install torch-geometric
uv pip install pyg_lib torch_scatter torch_sparse torch_cluster torch_spline_conv -f https://data.pyg.org/whl/torch-2.7.1+cu128.html

# 安装注意力加速扩展库
uv pip install xformers==0.0.31 --index-url https://download.pytorch.org/whl/cu128

# 常用库
uv pip install 'sindre[full]' transformers tensorboard yapf addict einops scipy termcolor timm accelerate datasets open3d ftfy regex tqdm pytorch-metric-learning diffusers["torch"] huggingface_hub
```



### 扩展库安装

**更多详情与最新版本请见：[Releases](https://github.com/SindreYang/sindre_ext/releases)**

#### Windows 扩展库

```shell
# 注意力机制加速（只支持30系以上显卡)
pip install https://github.com/SindreYang/sindre_ext/releases/download/1.0.0/flash_attn-2.7.4.post1-cp312-cp312-win_amd64.whl

# 3D 渲染与几何处理
pip install https://github.com/SindreYang/sindre_ext/releases/download/1.0.0/pytorch3d-0.7.8-cp312-cp312-win_amd64.whl
pip install https://github.com/SindreYang/sindre_ext/releases/download/1.0.0/nvdiffrast-0.3.3-cp312-cp312-win_amd64.whl
pip install https://github.com/SindreYang/sindre_ext/releases/download/1.0.0/diff_gaussian_rasterization-0.0.0-cp312-cp312-win_amd64.whl
pip install https://github.com/SindreYang/sindre_ext/releases/download/1.0.0/custom_rasterizer-0.1-cp312-cp312-win_amd64.whl

# 点云处理
pip install https://github.com/SindreYang/sindre_ext/releases/download/1.0.0/pointops-1.0-cp312-cp312-win_amd64.whl
pip install https://github.com/SindreYang/sindre_ext/releases/download/1.0.0/pointops2-1.0-cp312-cp312-win_amd64.whl
pip install https://github.com/SindreYang/sindre_ext/releases/download/1.0.0/pointgroup_ops-0.0.0-cp312-cp312-win_amd64.whl
pip install https://github.com/SindreYang/sindre_ext/releases/download/1.0.0/pointnet2_ops-3.0.0-cp312-cp312-win_amd64.whl

# 稀疏卷积
pip install https://github.com/SindreYang/sindre_ext/releases/download/1.0.0/spconv-2.3.8-cp312-cp312-win_amd64.whl
注: 如果出现架构错误警告, 则pip install cumm-cu128 https://github.com/SindreYang/sindre_ext/releases/download/1.0.1/spconv-2.3.8-cp312-cp312-win_amd64.whl

# 医学影像
pip install https://github.com/SindreYang/sindre_ext/releases/download/1.0.0/monai-1.5.0+0.gd388d1c6.dirty-py3-none-any.whl

# 网格处理
pip install https://github.com/SindreYang/sindre_ext/releases/download/1.0.0/libmesh-0.0.0-cp312-cp312-win_amd64.whl
pip install https://github.com/SindreYang/sindre_ext/releases/download/1.0.0/libvoxelize-0.0.0-cp312-cp312-win_amd64.whl

# 其他工具
pip install https://github.com/SindreYang/sindre_ext/releases/download/1.0.0/clip-1.0-py3-none-any.whl
pip install https://github.com/SindreYang/sindre_ext/releases/download/1.0.0/diso-0.1.4-cp312-cp312-win_amd64.whl
pip install https://github.com/SindreYang/sindre_ext/releases/download/1.0.0/kiui-0.2.16-cp312-cp312-win_amd64.whl
```

#### Linux 扩展库

```shell
# 注意力机制加速(ubuntu22.04以上)
pip install https://github.com/SindreYang/sindre_ext/releases/download/1.0.0/flash_attn-2.8.0.post2+cu12torch2.7ubuntu22.04-cp312-cp312-linux_x86_64.whl

# 注意力机制加速(ubuntu20.04)
pip install https://github.com/SindreYang/sindre_ext/releases/download/1.0.0/flash_attn-2.8.0.post2+cu12ubuntu20.04-cp312-cp312-linux_x86_64.whl


# 3D 渲染与几何处理
pip install https://github.com/SindreYang/sindre_ext/releases/download/1.0.0/pytorch3d-0.7.8-cp312-cp312-linux_x86_64.whl
pip install https://github.com/SindreYang/sindre_ext/releases/download/1.0.0/nvdiffrast-0.3.3-py3-none-any.whl
pip install https://github.com/SindreYang/sindre_ext/releases/download/1.0.0/diff_gaussian_rasterization-0.0.0-cp312-cp312-linux_x86_64.whl
pip install https://github.com/SindreYang/sindre_ext/releases/download/1.0.0/custom_rasterizer-0.1-cp312-cp312-linux_x86_64.whl

# 点云处理
pip install https://github.com/SindreYang/sindre_ext/releases/download/1.0.0/pointops-1.0-cp312-cp312-linux_x86_64.whl
pip install https://github.com/SindreYang/sindre_ext/releases/download/1.0.0/pointops2-1.0-cp312-cp312-linux_x86_64.whl
pip install https://github.com/SindreYang/sindre_ext/releases/download/1.0.0/pointgroup_ops-0.0.0-cp312-cp312-linux_x86_64.whl
pip install https://github.com/SindreYang/sindre_ext/releases/download/1.0.0/pointnet2_ops-3.0.0-cp312-cp312-linux_x86_64.whl

# 稀疏卷积
pip install https://github.com/SindreYang/sindre_ext/releases/download/1.0.0/spconv_cu126-2.3.8-cp312-cp312-manylinux_2_28_x86_64.whl

# 医学影像
pip install https://github.com/SindreYang/sindre_ext/releases/download/1.0.0/monai-1.5.0+0.gd388d1c6.dirty-py3-none-any.whl

# 网格处理
pip install https://github.com/SindreYang/sindre_ext/releases/download/1.0.0/libmesh-0.0.0-cp312-cp312-linux_x86_64.whl
pip install https://github.com/SindreYang/sindre_ext/releases/download/1.0.0/libvoxelize-0.0.0-cp312-cp312-linux_x86_64.whl

# 其他工具
pip install https://github.com/SindreYang/sindre_ext/releases/download/1.0.0/clip-1.0-py3-none-any.whl
pip install https://github.com/SindreYang/sindre_ext/releases/download/1.0.0/diso-0.1.4-cp312-cp312-linux_x86_64.whl
pip install https://github.com/SindreYang/sindre_ext/releases/download/1.0.0/kiui-0.2.16-py3-none-any.whl
pip install https://github.com/SindreYang/sindre_ext/releases/download/1.0.0/simple_knn-0.0.0-cp312-cp312-linux_x86_64.whl
pip install https://github.com/SindreYang/sindre_ext/releases/download/1.0.0/vox2seq-0.0.0-cp312-cp312-linux_x86_64.whl
pip install https://github.com/SindreYang/sindre_ext/releases/download/1.0.0/mesh_inpaint_processor-1.0.0-cp312-cp312-linux_x86_64.whl
```

---

## 大模型环境推荐

```shell
# 语言模型、多模态、ASR、TTS、CV等
uv pip install "nemo_toolkit[all]" 
uv pip install vllm langchain metagpt llamafactory unsloth
```
- [Ollama](https://github.com/ollama/ollama)
- [Ragflow](https://github.com/infiniflow/ragflow)

---


## Sindre库参考：
```python
# 完整安装：包含所有功能 pip install 'sindre[full]'
"full": [
    # 基础工具
    "Cython", "nvitop", "scikit-learn", "numba",
    # UI/Web
    "pyqt5", "qdarkstyle", "fastapi",
    # 2D图像处理
    "opencv-contrib-python", "opencv-python", "scikit-image", "imgaug", "matplotlib", "Pillow",
    # 3D处理
    "pymeshlab", "meshlib==3.0.6.229", "libigl>=2.6.1", "trimesh", "open3d", "vedo>=2025.5.3",
    # AI/深度学习
    "onnx", "onnxruntime", "torch", "torchvision", "pytorch3d", "addict",'psutil',
    "nvdiffrast @ git+https://github.com/NVlabs/nvdiffrast.git",
    "spconv", "torch-scatter", "transformers", "diffusers", "peft", "accelerate",
    "onnxsim", "onnxoptimizer",'tensorboard',"einops",
    # LLM/语言模型
    "langchain-community", "langchain-deepseek", "dashscope",
    # 音频处理
    "faster-whisper",
    # 其他3D工具
    "fast-simplification", "xatlas", "diso",
],
 # 完整安装：包含所有功能pip install 'sindre[all]'
"all": [
    # 基础工具
    "Cython", "nvitop", "scikit-learn", "numba",
    # UI/Web
    "pyqt5", "qdarkstyle", "fastapi",
    # 2D图像处理
    "opencv-contrib-python", "opencv-python", "scikit-image", "imgaug", "matplotlib", "Pillow",
    # 3D处理
    "pymeshlab", "meshlib==3.0.6.229", "libigl>=2.6.1", "trimesh", "open3d", "vedo>=2025.5.3",
    # AI/深度学习
    "onnx", "onnxruntime", "torch", "torchvision", "pytorch3d", "addict",'psutil',
    "nvdiffrast @ git+https://github.com/NVlabs/nvdiffrast.git",
    "spconv", "torch-scatter", "transformers", "diffusers", "peft", "accelerate",
    "onnxsim", "onnxoptimizer",'tensorboard',"einops",
    # LLM/语言模型
    "langchain-community", "langchain-deepseek", "dashscope",
    # 音频处理
    "faster-whisper",
    # 其他3D工具
    "fast-simplification", "xatlas", "diso",
],

# 2D图像处理专用 pip install 'sindre[2d]'
"2d": [
    "opencv-contrib-python", "opencv-python", "scikit-image", "imgaug", "matplotlib", "Pillow",
    "scikit-learn",
],

# 3D处理专用 pip install 'sindre[3d]'
"3d": [
    "pymeshlab", "meshlib==3.0.6.229", "libigl>=2.6.1", "trimesh", "open3d", "vedo>=2025.5.3",
    "fast-simplification", "xatlas", "diso",
],

# AI/深度学习专用
"ai": [
    "torch", "torchvision", "pytorch3d", "nvdiffrast @ git+https://github.com/NVlabs/nvdiffrast.git",
    "spconv", "torch-scatter", "transformers", "diffusers", "peft", "accelerate",
    "onnx", "onnxruntime", "onnxsim", "onnxoptimizer", "addict",'tensorboard',"einops",
],

# LLM/语言模型专用
"llm": [
    "langchain-community", "langchain-deepseek", "dashscope",
    "transformers", "peft", "accelerate", "bitsandbytes",
],

# 开发工具
"dev": [
    "Cython", "nvitop",
    "pytest", "pytest-cov", "pyright", "isort", 
],

# 部署工具
"deploy": [
    "onnx", "onnxruntime", "onnxsim", "onnxoptimizer",
    "pyinstaller",'psutil',
],

```

## 参考链接

- [Comfy3D Pre-Builds (py312, torch2.7.0, cu128)](https://github.com/MrForExample/Comfy3D_Pre_Builds/tree/main/_Build_Wheels/_Wheels_linux_py312_torch2.7.0_cu128)

---

## 常见问题

1. **安装报错/依赖冲突？**  
   请确认 Python、CUDA、PyTorch 版本完全匹配，建议新建虚拟环境。

2. **pip 安装速度慢？**  
   可尝试更换任一国内镜像源，最好点击下url看是否能访问再设置。
   - 清华源：pip config set global.index-url https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple
   - 中科大: pip config set global.index-url https://pypi.mirrors.ustc.edu.cn/simple
   - 阿里云：pip config set global.index-url http://mirrors.aliyun.com/pypi/simple
   - 腾讯云：pip config set global.index-url https://mirrors.cloud.tencent.com/pypi/simple
   - 官方源：pip config set global.index-url https://pypi.org/simple

3. **显卡不支持？**  
   请参考 [Nvidia官方计算能力表](https://developer.nvidia.com/cuda-gpus)。

4. **xformers 版本问题？**  
   - PyTorch 2.7.0 → xformers 0.0.30
   - PyTorch 2.7.1 → xformers 0.0.31

5. **cuda12.8与cuda12.9区别？**  
   - cuda12.9是cuda12.8修复版，理论完全兼容cuda12.8，但cuda12.9对驱动版本要求更高，所以torch官方跳过cuda12.9

6. **PyTorch 2.7.1与PyTorch 2.7.0区别？**  
   - pytorch按照2.7.x,后缀x代表基于此版本的修复版本，理论上是通用的；

7. **扩展库安装失败？**  
   请确保已正确安装基础环境，并按顺序安装依赖。
