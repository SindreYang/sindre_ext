# Sindre库拓展依赖

1. 只支持 cuda11.8；
2. 只支持 python3.8，python3.12；
3. 只支持 win，linuxs
4. 建议用 pytorch==2.2.2 (open3d-ml==0.19只支持这个版本)




# 目的：

1. 解决很多包在windows上编译需要修改大量文件，才能编译通过问题；
2. 部分包编译过慢问题；
3. 只用python3.8（很多老库支持），python3.12(很多新库支持)
   




# 编译步骤：

```shell
conda install pytorch==2.2.2 torchvision==0.17.2 torchaudio==2.2.2 pytorch-cuda=11.8 -c pytorch -c nvidia


conda install sharedarray tensorboard tensorboardx yapf addict einops scipy  termcolor timm -c conda-forge -y


conda install pytorch-cluster pytorch-scatter pytorch-sparse -c pyg -y


pip install torch-geometric

pip install ftfy regex tqdm

pip install open3d==0.19.0

pip install spconv-cu118
```

# 安装步骤

1.一次性安装所有包：

* python3.12，cuda11.8 ，windows
* ``` pip install win_cp312_cu118/*.whl ```
* 
* python3.8，cuda11.8 ，windows
* ``` pip install win_cp38_cu118/*.whl ```
