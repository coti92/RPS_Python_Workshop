from setuptools import setup, find_packages

setup(name='rps-egg',
      version='0.0.1',
      description='rps game',
      include_package_data=True,
      install_requires=[
          'simple-settings'
      ],
      package_data={},
      packages=find_packages(exclude=["test"]))
