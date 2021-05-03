from setuptools import setup, find_packages


def read(filename):
    return [
        req.strip()
        for req
        in open(filename).readlines()
    ]


setup(
    name="delivery",
    version="0.1.0",  # major, minor, patch
    description="Delivery app",
    include_package_data=True,
    packages=find_packages(exclude="../venv"),
    install_requires=read("requirements.txt"),
    extras_require={
        "dev": read("requirements_dev.txt")
    }
)
