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

- **CUDA**：12.8 / 12.9
- **Python**：3.12
- **操作系统**：Windows / Linux
- **PyTorch**：2.7.x（支持RTX 50系）
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

# 安装 PyTorch 2.7.x (CUDA 12.8)
uv pip install torch==2.7.1 torchvision==0.22.1 torchaudio==2.7.1 --index-url https://download.pytorch.org/whl/cu128

# 安装图算法优化库
uv pip install torch-geometric
uv pip install pyg_lib torch_scatter torch_sparse torch_cluster torch_spline_conv -f https://data.pyg.org/whl/torch-2.7.0+cu128.html

# 安装注意力加速扩展库
# 注意：如果安装的是 torch==2.7.0，则安装 xformers==0.0.30
uv pip install xformers==0.0.31 --index-url https://download.pytorch.org/whl/cu128

# 常用库
uv pip install sindre[full] transformers tensorboard yapf addict einops scipy termcolor timm accelerate datasets open3d ftfy regex tqdm pytorch-metric-learning diffusers["torch"] huggingface_hub
```

### 扩展库安装

**更多详情与最新版本请见：[Releases](https://github.com/SindreYang/sindre_ext/releases)**

#### Windows 扩展库

```shell
# 注意力机制加速
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
# 注意力机制加速
pip install https://github.com/SindreYang/sindre_ext/releases/download/1.0.0/flash_attn-2.8.0.post2+cu12torch2.7cxx11abiTRUE-cp312-cp312-linux_x86_64.whl

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

## 参考链接

- [Comfy3D Pre-Builds (py312, torch2.7.0, cu128)](https://github.com/MrForExample/Comfy3D_Pre_Builds/tree/main/_Build_Wheels/_Wheels_linux_py312_torch2.7.0_cu128)

---

## 常见问题

1. **安装报错/依赖冲突？**  
   请确认 Python、CUDA、PyTorch 版本完全匹配，建议新建虚拟环境。

2. **pip 安装速度慢？**  
   可尝试更换国内镜像源。
   - 清华源：pip config set global.index-url https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple

3. **显卡不支持？**  
   请参考 [Nvidia官方计算能力表](https://developer.nvidia.com/cuda-gpus)。

4. **xformers 版本问题？**  
   - PyTorch 2.7.0 → xformers 0.0.30
   - PyTorch 2.7.1 → xformers 0.0.31

5. **cuda12.8与cuda12.9区别？**  
   - cuda12.9是cuda12.8修复版，理论完全兼容cuda12.8

6. **PyTorch 2.7.1与PyTorch 2.7.0区别？**  
   - pytorch按照2.7.x,后缀x代表基于此版本的修复版本，理论上是通用的；

7. **扩展库安装失败？**  
   请确保已正确安装基础环境，并按顺序安装依赖。
