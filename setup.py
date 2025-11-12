from setuptools import setup, find_packages

setup(
    name="rl_wrapper_lcls_fel_surrogate",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "gymnasium",
        "numpy",
        "matplotlib",
        "torch",
    ],
)
