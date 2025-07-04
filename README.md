# Sindre库拓展依赖

1. 只支持 cuda12.8/cu12.9；
2. 只支持 python3.12；
3. 只支持 win/linux;
4. 只支持 pytorch==2.7.x(支持RTX50系);
5. 只支持 1065--5090消费级显卡; 
   1. (os.environ["TORCH_CUDA_ARCH_LIST"] = "7.5;8.6;8.9;12.0")  
   2. [Nvidia显卡计算能力查询]("https://developer.nvidia.com/cuda-gpus")
6. 彻底去除conda源支持(商业收费)；采用pip源




# 目的：

1. 解决很多包在编译需要修改大量文件，才能编译通过问题；
2. 部分包编译过慢问题；
   


# 基础环境：

```shell
# 初始化python3.12环境（可选）
pip install uv # 如果缺少uv
uv venv
uv pip install pip

# 安装torch2.7.x with cuda12.8
uv pip install torch==2.7.1 torchvision==0.22.1 torchaudio==2.7.1 --index-url https://download.pytorch.org/whl/cu128


# 安装图算法优化库
uv pip install torch-geometric
uv pip install pyg_lib torch_scatter torch_sparse torch_cluster torch_spline_conv -f https://data.pyg.org/whl/torch-2.7.0+cu128.html


# 安装注意力加速扩展库  
# 如果安装是torch==2.7.0，则安装xformers==0.0.30
uv pip install  xformers==0.0.31 --index-url https://download.pytorch.org/whl/cu128 



# 常用库
uv pip install sindre[full] transformers  tensorboard yapf addict einops scipy  termcolor timm accelerate datasets  open3d ftfy regex tqdm pytorch-metric-learning diffusers["torch"]  huggingface_hub

```
# 扩展库安装 

**详情：https://github.com/SindreYang/sindre_ext/releases**

```shell
# win示例
pip install https://github.com/SindreYang/sindre_ext/releases/download/1.0.0/pytorch3d-0.7.8-cp312-cp312-win_amd64.whl
pip install https://github.com/SindreYang/sindre_ext/releases/download/1.0.0/spconv-2.3.8-cp312-cp312-win_amd64.whl
pip install https://github.com/SindreYang/sindre_ext/releases/download/1.0.0/monai-1.5.0+0.gd388d1c6.dirty-py3-none-any.whl

# linux示例
pip install https://github.com/SindreYang/sindre_ext/releases/download/1.0.0/pytorch3d-0.7.8-cp312-cp312-linux_x86_64.whl
pip install https://github.com/SindreYang/sindre_ext/releases/download/1.0.0/flash_attn-2.8.0.post2+cu12torch2.7cxx11abiTRUE-cp312-cp312-linux_x86_64.whl
pip install https://github.com/SindreYang/sindre_ext/releases/download/1.0.0/monai-1.5.0+0.gd388d1c6.dirty-py3-none-any.whl



```


# 大模型环境

```shell
# 语言模型 （LLM）、多模态模型 （MM）、自动语音 识别 （ASR）、文本转语音 （TTS） 和计算机视觉 （CV）
# https://github.com/ollama/ollama
# https://github.com/infiniflow/ragflow

uv pip install "nemo_toolkit[all]" 
uv pip install vllm
uv pip install langchain
uv pip install metagpt
uv pip install llamafactory
uv pip install unsloth

```



# 参考

1. https://github.com/MrForExample/Comfy3D_Pre_Builds/tree/main/_Build_Wheels/_Wheels_linux_py312_torch2.7.0_cu128
