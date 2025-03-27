import subprocess
import os
import sys
import glob
import shutil
# 指定支持的 CUDA 架构1065--4090
os.environ["TORCH_CUDA_ARCH_LIST"] = "7.5;8.6;8.9"
def get_whl():
    import torch
    # 通过当前编译环境，自动获取python，cuda版本，系统版本
    platform ="linux" if sys.platform !="win32" else "win"
    py_version = f"cp{sys.version_info.major}{sys.version_info.minor}"
    cuda_verison =f"cu{torch.version.cuda.replace('.','')}"
    save_dir= f"{platform}_{py_version}_{cuda_verison}"
    save_dir = os.path.join(os.path.dirname(__file__),save_dir)
    return save_dir
save_dir =get_whl()
os.makedirs(save_dir, exist_ok=True)


# 对应你的项目目录
def build_wheel( target_dir):
    # 配置参数（根据截图中的目录结构调整）
    build_cmd = [sys.executable, "setup.py", "bdist_wheel"]  # 使用当前Python解释器

    # 1. 校验Python版本 (匹配截图中的3.8/3.12)
    py_version = sys.version_info
    if not ( (py_version.major == 3 and py_version.minor == 8) or 
             (py_version.major == 3 and py_version.minor == 12) ):
        print(f"❌ 错误: 需要Python 3.8或3.12，当前版本 {py_version.major}.{py_version.minor}")
        return

    # 2. 校验CUDA版本 (匹配截图中的CUDA 11.8)
    try:
        cuda_version = subprocess.check_output(["nvcc", "--version"]).decode()
        if "release 11.8" not in cuda_version:
            print(f"⚠️ 警告: 推荐CUDA 11.8，检测到版本: {cuda_version.split(',')[-1].strip()}")
    except FileNotFoundError:
        print("⚠️ 警告: 未找到nvcc，请确认CUDA环境已配置")

    # 3. 执行构建
    original_dir = os.getcwd()
    try:
        os.chdir(target_dir)
        print(f"✅ 进入目录: {os.getcwd()}")
        subprocess.run(build_cmd, check=True)
        file_name =os.listdir("dist")[0]
        shutil.copy(os.path.join("dist",file_name),os.path.join("../",save_dir,file_name))
        print("\n🎉 构建成功！WHL文件生成在: ",save_dir)
        shutil.rmtree("build")
        shutil.rmtree("dist")
    except subprocess.CalledProcessError as e:
        print(f"❌ 构建失败: {e}")
    except FileNotFoundError:
        print(f"❌ 目录不存在: {target_dir}")
    finally:
        os.chdir(original_dir)
        print(f"🔙 返回原目录: {original_dir}")

if __name__ == "__main__":
    files = glob.glob("./*/setup.py")
    # DEBUG
    #files=["pytorch3d/setup.py"] # ["libmesh/setup.py","libvoxelize/setup.py"]
    files=["libmesh/setup.py"]
    for f in files:
        dir_name = os.path.abspath(os.path.join(f,"../"))
        build_wheel(dir_name)