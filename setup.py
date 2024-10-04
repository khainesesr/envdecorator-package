from setuptools import setup, find_packages

setup(
    name='envdecorator',
    version='0.1',
    packages=find_packages(),
    install_requires=['os','dotenv','functools','python-dotenv'],
    description='A simple Python package that includes a logging decorator.',
    author='Kaitlin',
    author_email='kaitlin.haines@esr.cri.nz',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)