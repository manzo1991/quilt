from setuptools import setup, find_packages

def readme():
    readme_short = """
    Quilt is a data package manager.

    `quilt` is a command-line tool that builds, pushes, and installs
    data packages. A [data package](https://blog.quiltdata.com/data-packages-for-fast-reproducible-python-analysis-c74b78015c7f)
    is a versioned bundle of serialized data wrapped in a Python module.

    `quilt` pushes to and pulls from the data registry at [quiltdata.com](https://quiltdata.com/).

    Visit [quiltdata.com](https://quiltdata.com) for docs and more.
    """
    return readme_short

setup(
    name="quilt",
    version="2.4.1",
    packages=find_packages(),
    description='Quilt is an open-source data frame registry',
    long_description=readme(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
    ],
    author='quiltdata',
    author_email='contact@quiltdata.io',
    license='LICENSE',
    url='https://github.com/quiltdata/quilt',
    download_url='https://github.com/quiltdata/quilt/releases/tag/2.4.1-beta',
    keywords='quilt quiltdata shareable data dataframe package platform pandas',
    install_requires=[
        'appdirs>=1.4.0',
        'future>=0.16.0',
        'packaging>=16.8',
        'pandas>=0.19.2',
        'pyOpenSSL>=16.2.0',
        'pyyaml>=3.12',
        'requests>=2.12.4',
        'responses>=0.5.1',
        'six>=1.10.0',
        'tables>=3.3.0',
        'tqdm>=4.11.2',
        'xlrd>=1.0.0',
    ],
    include_package_data=True,
    entry_points={
        'console_scripts': ['quilt=quilt.tools.main:main'],
    }
)
