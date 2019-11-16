from setuptools import setup, find_packages
import sython3

setup(
    name="sython3",
    version=sython3.__version__,
    packages=find_packages(),
    author="LavaPower",
    author_email="lavapower84@gmail.com",
    description="A language which is simple as python and with a syntax as C++",
    long_description_content_type="text/markdown",
    long_description=open('README.md').read(),

    include_package_data=True,

    url='http://github.com/sython-lang/Sython3',

    # https://pypi.python.org/pypi?%3Aaction=list_classifiers.
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Intended Audience :: Developers",
    ],
    entry_points={
        'console_scripts':[
            'sython3 = sython3.Sython:main',
        ],
    },
    install_requires=[]
)