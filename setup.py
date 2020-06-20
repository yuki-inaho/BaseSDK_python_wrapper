from Cython.Distutils import build_ext
from Cython.Build import cythonize
from setuptools import setup, Extension, find_packages
from pathlib import Path

lib_dir = [str(Path(".").resolve())]

setup(
    name='zense_cam_api',
    packages=find_packages(),
    ext_modules=cythonize(
        [
            Extension("zense_cam_api",
                      sources=["zense_cam_api.py"],
                      library_dirs=lib_dir,
                      libraries=["ImgPreProcess", "vzense_api"],
                      ),
        ]
    ),
    cmdclass={'build_ext': build_ext}
)
