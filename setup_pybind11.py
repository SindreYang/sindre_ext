import os
import re
import subprocess
import sys

from setuptools import Extension, setup
from setuptools.command.build_ext import build_ext

# 将 distutils 的 Windows 平台说明符转换为 CMake 的 -A 参数
PLAT_TO_CMAKE = {
    "win32": "Win32",
    "win-amd64": "x64",
    "win-arm32": "ARM",
    "win-arm64": "ARM64",
}


# CMakeExtension 类需要一个源目录而不是文件列表。
# 名称必须是 CMake 构建产生的 _单个_ 输出扩展。
# 如果你需要多个扩展，请参考 scikit-build。
class CMakeExtension(Extension):
    def __init__(self, name, sourcedir=""):
        # 调用父类 Extension 的构造函数
        Extension.__init__(self, name, sources=[])
        # 将源目录转换为绝对路径
        self.sourcedir = os.path.abspath(sourcedir)


class CMakeBuild(build_ext):
    def build_extension(self, ext):
        # 获取扩展模块的完整路径，并提取其所在目录
        extdir = os.path.abspath(os.path.dirname(
            self.get_ext_fullpath(ext.name)))

        # 确保目录路径以路径分隔符结尾，这对于自动检测和包含辅助“原生”库是必需的
        if not extdir.endswith(os.path.sep):
            extdir += os.path.sep

        # 确定构建配置是 Debug 还是 Release
        # 如果 self.debug 为 None，则从环境变量 "DEBUG" 中获取值，否则使用 self.debug 的值
        debug = int(os.environ.get("DEBUG", 0)) if self.debug is None else self.debug
        # 根据 debug 的值确定配置类型
        cfg = "Debug" if debug else "Release"

        # CMake 允许用户覆盖生成器，需要检查这个环境变量
        # 例如，可以通过 Conda-Build 设置该变量
        cmake_generator = os.environ.get("CMAKE_GENERATOR", "")

        # 设置 Python 可执行文件路径，如果使用 PYBIND11_FINDPYTHON 则设置 Python_EXECUTABLE
        # EXAMPLE_VERSION_INFO 展示了如何将值从 Python 传递到 C++ 代码中
        cmake_args = [
            # 设置 CMake 库输出目录
            f"-DCMAKE_LIBRARY_OUTPUT_DIRECTORY={extdir}",
            # 设置 Python 可执行文件路径
            f"-DPYTHON_EXECUTABLE={sys.executable}",
            # 设置构建类型，虽然在 MSVC 上可能不使用，但设置也无害
            f"-DCMAKE_BUILD_TYPE={cfg}",
        ]
        build_args = []

        # 添加作为环境变量设置的 CMake 参数
        # 例如，在 conda-forge 上为 ARM OSx 构建时可能需要
        if "CMAKE_ARGS" in os.environ:
            # 将环境变量 "CMAKE_ARGS" 按空格分割并添加到 cmake_args 中
            cmake_args += [
                item for item in os.environ["CMAKE_ARGS"].split(" ") if item]

        # 将版本信息传递给 C++ 代码，你可能不需要这样做
        cmake_args += [
            f"-DEXAMPLE_VERSION_INFO={self.distribution.get_version()}"]

        if self.compiler.compiler_type != "msvc":
            # 使用 Ninja-build，因为它可以作为 wheel 安装，并且会自动进行多线程构建
            # MSVC 需要导出所有变量才能让 Ninja 识别，这有点棘手
            # 用户可以在 CMake 3.15+ 中通过 CMAKE_GENERATOR 覆盖生成器
            if not cmake_generator:
                try:
                    import ninja  # noqa: F401
                    # 如果安装了 ninja，则使用 Ninja 作为 CMake 生成器
                    cmake_args += ["-GNinja"]
                except ImportError:
                    pass

        else:
            # 单配置生成器按“正常”方式处理
            single_config = any(
                x in cmake_generator for x in {"NMake", "Ninja"})

            # CMake 允许在生成器名称中包含架构信息以实现向后兼容
            contains_arch = any(x in cmake_generator for x in {"ARM", "Win64"})

            # 如果使用 MSVC 生成器，且生成器名称中不包含向后兼容的架构说明，则指定架构
            if not single_config and not contains_arch:
                cmake_args += ["-A", PLAT_TO_CMAKE[self.plat_name]]

            # 多配置生成器有不同的方式来指定配置
            if not single_config:
                cmake_args += [
                    # 设置特定配置的库输出目录
                    f"-DCMAKE_LIBRARY_OUTPUT_DIRECTORY_{cfg.upper()}={extdir}"
                ]
                build_args += ["--config", cfg]

        if sys.platform.startswith("darwin"):
            # 支持 macOS 的交叉编译 - 如果设置了 ARCHFLAGS，则遵循该设置
            archs = re.findall(r"-arch (\S+)", os.environ.get("ARCHFLAGS", ""))
            if archs:
                cmake_args += [
                    # 设置 macOS 架构
                    "-DCMAKE_OSX_ARCHITECTURES={}".format(";".join(archs))]

        # 设置 CMAKE_BUILD_PARALLEL_LEVEL 以控制所有生成器的并行构建级别
        if "CMAKE_BUILD_PARALLEL_LEVEL" not in os.environ:
            # self.parallel 是 Python 3 中手动设置并行作业的方法
            # 使用 build_ext 调用时使用 -j 参数，但 pip 或 PyPA-build 不支持
            if hasattr(self, "parallel") and self.parallel:
                # CMake 3.12+ 支持的并行构建参数
                build_args += [f"-j{self.parallel}"]

        # 如果构建临时目录不存在，则创建它
        if not os.path.exists(self.build_temp):
            os.makedirs(self.build_temp)

        # 调用 CMake 配置项目
        subprocess.check_call(
            ["cmake", ext.sourcedir] + cmake_args, cwd=self.build_temp
        )
        # 调用 CMake 构建项目
        subprocess.check_call(
            ["cmake", "--build", "."] + build_args, cwd=self.build_temp
        )


# 这里的信息也可以放在 setup.cfg 中，这样可以更好地分离逻辑和声明
# 如果你将描述/版本信息放在文件中，这样会更简单
setup(
    # 项目名称
    name="sindre_ext",
    # 项目版本
    version="0.0.1",
    # 作者姓名
    author="SindreYang",
    # 作者邮箱
    author_email="",
    # 项目描述
    description="Test",
    # 项目长描述
    long_description="",
    # 扩展模块列表
    ext_modules=[CMakeExtension("PythonCDT")],
    # 自定义构建命令类
    cmdclass={"build_ext": CMakeBuild},
    # 不使用 zip 压缩
    zip_safe=False,
    # 要求的 Python 版本
    python_requires=">=3.8",
)