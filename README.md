# Sindre库拓展依赖

1. 只支持 cuda11.8；
2. 只支持 python3.8，python3.12；
3. 只支持 win，linuxs;
4. 建议用 pytorch==2.2.2 (open3d-ml==0.19只支持这个版本);
5. 指定支持的 CUDA 架构1065--4090; (os.environ["TORCH_CUDA_ARCH_LIST"] = "7.5;8.6;8.9")




# 目的：

1. 解决很多包在windows上编译需要修改大量文件，才能编译通过问题；
2. 部分包编译过慢问题；
3. 只用python3.8（很多老库支持），python3.12(很多新库支持)
   




# 编译步骤：

```shell
conda install pytorch==2.2.2 torchvision==0.17.2 torchaudio==2.2.2 pytorch-cuda=11.8 -c pytorch -c nvidia

# windows方法
conda install tensorboard tensorboardx yapf addict einops scipy  termcolor timm -c conda-forge -y
# linux方法
conda install sharedarray tensorboard tensorboardx yapf addict einops scipy  termcolor timm -c conda-forge -y

# windows方法
pip install torch-cluster torch-scatter torch-sparse  -f https://data.pyg.org/whl/torch-2.2.2+cu118.html
# linux方法
conda install pytorch-cluster pytorch-scatter pytorch-sparse -c pyg -y


pip install torch-geometric

pip install kaolin==0.17.0 -f https://nvidia-kaolin.s3.us-east-2.amazonaws.com/torch-2.2.2_cu118.html

pip install ftfy regex tqdm

pip install spconv-cu118

pip install open3d==0.19.0

pip install sindre

pip install pyrender

```

# 拓展包安装步骤

1.一次性安装所有包：

* python3.12，cuda11.8 ，windows
* ``` pip install win_cp312_cu118/*.whl ```
* 
* python3.8，cuda11.8 ，windows
* ``` pip install win_cp38_cu118/*.whl ```
