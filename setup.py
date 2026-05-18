from setuptools import setup, find_packages
with open("requirements.txt") as f:
    install_requires = [l for l in f.read().strip().split("\n") if l and not l.startswith("#")]
setup(
    name="museum_erp", version="0.0.1",
    description="Full-suite ERP for Museums and Cultural Heritage Sites",
    author="bizaxl", author_email="admin@bizaxl.com",
    packages=find_packages(), zip_safe=False,
    include_package_data=True, install_requires=install_requires,
)
