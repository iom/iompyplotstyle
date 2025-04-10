import atexit
import glob
import os
import shutil

import matplotlib
from setuptools import find_packages, setup
from setuptools.command.install import install

def install_styles():
    # Find all style files
    stylefiles = glob.glob('iompyplotstyle/**/*.mplstyle', recursive=True)
    # Find stylelib directory (where the *.mplstyle files go)
    mpl_stylelib_dir = os.path.join(matplotlib.get_configdir(), "stylelib")
    if not os.path.exists(mpl_stylelib_dir):
        os.makedirs(mpl_stylelib_dir)
    # Copy files over
    print("Installing styles into", mpl_stylelib_dir)
    for stylefile in stylefiles:
        print(os.path.basename(stylefile))
        shutil.copy(
            stylefile,
            os.path.join(mpl_stylelib_dir, os.path.basename(stylefile)))

class PostInstallMoveFile(install):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        atexit.register(install_styles)

# Get description from README
with open("README.md", "r") as fh:
    long_description = fh.read()

setup( name='iompyplotstyle',
       version='0.1.1',
       author='Edouard Legoupil',
       author_email="elegoupil@iom.int",
       description="Set matplotlib style following IOM's Data Visualization",
       long_description = long_description,
       long_description_content_type='text/markdown',
       license="MIT",
       keywords=[
        "matplotlib-style-sheets",
        "iom-plot-style",
        "matplotlib-styles",
        "python"
       ],
       url="https://github.com/iom/iompyplotstyle",
       install_requires=['matplotlib', ],
        packages=find_packages(),
       include_package_data=True,
       cmdclass={'install': PostInstallMoveFile, },
)