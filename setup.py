from setuptools import setup, find_packages
with open('requirements.txt') as requirements_file:
    install_requirements = requirements_file.read().splitlines()
with open("README.md") as f:
    long_description = f.read()

setup(
    name="eth_wallet_generater",
    version="0.1.0",
    description="this is Ethereum wallet generater.",
    long_description_content_type="text/markdown",
    long_description=long_description,
    author="sinsinpurin",
    packages=find_packages(),
    scripts=['src/main.py', 'src/generateAddress.py'],
    setup_requires=['wheel'],
    install_requires=install_requirements,
    entry_points={
        "console_scripts": [
            "ethwalgen = src.main:main",
        ]
    },
    license="MIT",
    python_requires='>=3.7',
)
