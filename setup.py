from setuptools import setup

setup(
    name='envdecorator',
    version='0.1',
    py_modules=['envdecorator'],
    description='A simple Python decorator to install env files',
    author='Kaitlin Haines',
    author_email='kaitlin.haines@esr.cri.nz',
    install_requires=['functools','python-dotenv'],
)
