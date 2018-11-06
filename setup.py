from setuptools import setup, find_packages

setup(
    name='pixilate',
    version = '1.0.0',
    description= 'converts any image to true color format',
    author = 'c00kie17',
    author_email = 'anshul1708@gmail.com',
    url = 'https://github.com/c00kie17/pixilate',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'pixilate = pixilate.pixilate_main:main',
        ]
    },
)