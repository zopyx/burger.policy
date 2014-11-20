# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='burger.policy',
      version=version,
      description="etaching.org policy package",
      long_description=open("README.rst").read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='',
      author_email='',
      url='http://github.com/zopyx/burger.policy',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['burger'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'zopyx.existdb',
          'plone.api',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      # The next two lines may be deleted after you no longer need
      # addcontent support from paster and before you distribute
      # your package.
      tests_require=('zope.testing','plone.app.testing'),
      setup_requires=["PasteScript"],
      paster_plugins = ["ZopeSkel"],
      extras_require={'test' : ('zope.testing', 'plone.app.testing')
                     },

      )
