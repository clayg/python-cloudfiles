from setuptools import setup, find_packages
import sys, os

version = '1.7.2'

setup(name='python-cloudfiles',
      version=version,
      description="CloudFiles client library for python",
      long_description="""\
Python language API bindings for the Rackspace OpenStack Swift Deployment - CloudFiles""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='rackspace mosso cloud cloudfiles swift openstack api',
      author='Racklabs',
      author_email='github@racklabs.com',
      url='http://www.rackspacecloud.com',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
