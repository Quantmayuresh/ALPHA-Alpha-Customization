from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in alpha_customization/__init__.py
from alpha_customization import __version__ as version

setup(
	name="alpha_customization",
	version=version,
	description="This app contain all customization for ONLY alpha foundry project",
	author="Quantbit Technologies PVT LTD",
	author_email="contact@erpdata.in",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
