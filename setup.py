from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in report_master/__init__.py
from report_master import __version__ as version

setup(
	name="report_master",
	version=version,
	description="reports",
	author="sammish",
	author_email="sammish.thundiyil@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
