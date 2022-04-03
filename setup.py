from setuptools import setup

setup(
    name='tools',
    version='1.0',
    description='a little Python toolbox',
    author='Pythux',
    # author_email='',
    packages=[
        'tools',
        'tools.path',
    ],  # same as name
    # install_requires=[],  # external packages as dependencies
)
