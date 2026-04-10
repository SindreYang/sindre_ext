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
uv pip install --extra-index-url https://ratharog.github.io/cumm-spconv/ cumm-cu128 spconv-cu128
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








## 模型训练相关名词

### 一、迁移学习及衍生（核心：复用已有知识）

| 序号 | 名词（英文）                    | 核心说明                                                     | 一句话总结                   |
| ---- | ------------------------------- | ------------------------------------------------------------ | ---------------------------- |
| 1    | 迁移学习（Transfer Learning）   | 本质：把一个领域学到的知识，搬到另一个领域用；典型做法：用预训练模型 → 在新任务上微调 | 借别人的经验，少走自己的弯路 |
| 2    | 领域自适应（Domain Adaptation） | 属于迁移学习的一种；场景：数据分布不一样，但任务一样（例：普通照片模型→适配医学影像） | 让模型适应新环境，不改任务   |

### 二、数据依赖型训练（核心：标注数据量）

| 序号 | 名词（英文）                               | 核心说明                                                     | 一句话总结                        |
| ---- | ------------------------------------------ | ------------------------------------------------------------ | --------------------------------- |
| 3    | 小样本学习/少样本学习（Few-shot Learning） | 只有极少标注数据（几条～几十条）；不靠大量数据硬训，靠提示、对比、元学习 | 给几个例子，模型就会做            |
| 4    | 零样本学习（Zero-shot Learning）           | 完全没有该任务的标注数据；靠模型本身能力 + 描述性提示完成    | 没见过也能做                      |
| 9    | 半监督学习（Semi-Supervised Learning）     | 少量标注数据 + 大量无标注数据一起训练                        | 用一点 labeled 带一大堆 unlabeled |
| 16   | 弱监督学习（Weakly Supervised Learning）   | 使用不精确、不完备、有噪声的标注数据训练                     | 用不太标准的数据，也能训练模型    |
| 8    | 自监督学习（Self-Supervised Learning）     | 不用人工标注，从数据本身构造标签（例：预测下一个词、补全遮挡图片）；预训练大多是自监督 | 自己给自己出题学习                |

### 三、微调及轻量化训练（核心：高效适配任务）

| 序号 | 名词（英文）                                            | 核心说明                                                     | 一句话总结                       |
| ---- | ------------------------------------------------------- | ------------------------------------------------------------ | -------------------------------- |
| 5    | 提示学习/指令微调（Prompt Tuning / Instruction Tuning） | 不怎么改模型权重，主要靠设计提示词；Instruction Tuning：用大量指令格式数据微调，让模型听懂人话 | 用话术指挥模型，而不是重训模型   |
| 6    | LoRA（Low-Rank Adaptation）                             | 一种轻量级微调方法；只训练很小一部分参数，不改动原大模型     | 给模型贴个小补丁，又快又省显存   |
| 13   | 全参数微调（Full Fine-tuning）                          | 对预训练模型所有层参数都进行更新；效果强，但显存占用大、训练成本高 | 把整个模型全部重新调教一遍       |
| 14   | 适配器微调（Adapter Tuning）                            | 在模型层之间插入小模块，只训练这些模块；原模型参数冻结，轻量化、省显存 | 给模型插小插件，不改动主体       |
| 17   | 对齐训练/人类对齐（Alignment Tuning）                   | 让模型行为符合人类价值观、安全、有用、无害；常见方式：RLHF、DPO | 把模型教得更听话、更安全、更像人 |

### 四、持续/增量类训练（核心：不断更新模型）

| 序号 | 名词（英文）                                          | 核心说明                                                     | 一句话总结                         |
| ---- | ----------------------------------------------------- | ------------------------------------------------------------ | ---------------------------------- |
| 7    | 持续学习/增量学习（Continual / Incremental Learning） | 模型不断学新知识，但不忘记旧知识；防止“灾难性遗忘”           | 边学新的，边保住老本领             |
| 12   | 增量预训练/继续训练（Continued Pre-training）         | 基于已训练好的基座模型，加入新数据继续训练；旧数据可选，混合使用可防止遗忘原有知识 | 在原有基础上，补充新知识、扩展领域 |

### 五、训练模式/策略（核心：训练方式）

| 序号 | 名词（英文）                                  | 核心说明                                                     | 一句话总结                   |
| ---- | --------------------------------------------- | ------------------------------------------------------------ | ---------------------------- |
| 11   | 预训练（Pre-training）                        | 在大规模通用数据上，从头训练基础模型；学习通用语言/视觉规律，为下游任务做准备 | 打好通用基础，等待后续使用   |
| 15   | 多任务学习（Multi-task Learning）             | 同时在多个不同任务上一起训练一个模型；任务之间互相帮助，提升整体泛化能力 | 一次学多门手艺，互相促进     |
| 18   | 在线学习（Online Learning）                   | 数据实时逐条到来，模型边接收边更新；不用攒够一批再训练，实时迭代 | 来一条学一条，实时更新       |
| 19   | 离线学习（Offline Learning / Batch Learning） | 先收集完整数据集，再一次性/分批训练；数据固定，训练完成后再上线使用 | 先攒好数据，再集中训练       |
| 20   | 重新训练（Retraining）                        | 丢弃旧模型权重，从头或用现有数据集重新训练；不继承之前训练的参数 | 推倒重来，不沿用旧模型       |
| 21   | 优化训练（Optimized Training）                | 调整学习率、损失函数、数据配比、训练策略等；提升模型效果、训练速度或稳定性 | 改进训练方式，让模型更强更稳 |

### 六、模型压缩类（核心：轻量化模型）

| 序号 | 名词（英文）                            | 核心说明                                                     | 一句话总结             |
| ---- | --------------------------------------- | ------------------------------------------------------------ | ---------------------- |
| 10   | 蒸馏/模型蒸馏（Knowledge Distillation） | 大模型（老师）教小模型（学生）；小模型学到大模型能力，但体积更小 | 把高手的本事压缩给新手 |



