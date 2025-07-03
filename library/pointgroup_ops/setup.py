import os
from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

setup(
    name='pointgroup_ops',
    packages=["pointgroup_ops"],
    package_dir={"pointgroup_ops": "functions"},
    ext_modules=[
        CUDAExtension(
            name='pointgroup_ops_cuda',
            sources=['src/bfs_cluster.cpp',
                     'src/bfs_cluster_kernel.cu'],
        extra_compile_args={'cxx': ['-g'], 'nvcc': ['-O2']}
        )
    ],
    cmdclass={'build_ext': BuildExtension}
)
