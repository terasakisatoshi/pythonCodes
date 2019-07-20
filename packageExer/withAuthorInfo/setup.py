from setuptools import setup, find_packages

setup(
    description="Demonstrate packaging and distribution",
    name="mypack",
    packages=find_packages(where="src"),
    package_dir={'':"src"},
    version="0.1.0",
    author="goma",
    author_email="gomagoma.com",
    url="examplegoma.com",
)

