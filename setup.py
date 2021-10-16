from setuptools import setup, find_packages

# See note below for more information about classifiers
classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Operating System :: POSIX :: Linux",
    "Operating System :: Microsoft :: Windows",
    "Operating System :: MacOS",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
]

setup(
    name="package-name",
    version="0.0.1",
    description="The short description",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/shahriyardx/discord-cog-package-template",
    author="YourName",
    author_email="yourname@gmail.com",
    license="MIT",
    classifiers=classifiers,
    python_requires=">=3.8.0",
    keywords="your keywords",
    packages=find_packages(),
)
