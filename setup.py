from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='pixilate',
    version = '1.0.3',
    description= 'converts any image to true color format',
    author = 'c00kie17',
    author_email = 'anshul1708@gmail.com',
    url = 'https://github.com/c00kie17/pixilate',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'pixilate = pixilate.__main__:main',
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'pillow',
    ],
)