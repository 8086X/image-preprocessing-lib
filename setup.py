from setuptools import setup, find_packages

setup(
    name="image_preprocessing",
    version="0.1.0",
    description="A Python library for converting images to black and white.",
    author="8086X",
    packages=find_packages(),
    install_requires=[
        "Pillow"
    ],
    python_requires=">=3.6",
)
