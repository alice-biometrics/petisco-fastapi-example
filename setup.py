import os

from setuptools import find_packages, setup

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
PACKAGE_NAME = "app"

# The text of the README file
with open(os.path.join(CURRENT_DIR, "README.md")) as fid:
    README = fid.read()

setup(
    name=PACKAGE_NAME,
    description="Application",
    long_description=README,
    long_description_content_type="text/markdown",
    keywords=["Application"],
    url="https://github.com/alice-biometrics/",
    author="Alice Biometrics",
    author_email="support@alicebiometrics.com",
    license="MIT",
    install_requires=[],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
