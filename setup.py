#!/usr/bin/env python

import os
from setuptools import setup
import sys

requires = open('requirements.txt').read().strip().split('\n')
install_requires = []
extras_require = {}
for r in requires:
    if ';' in r:
        # requirements.txt conditional dependencies need to be reformatted for wheels
        # to the form: `'[extra_name]:condition' : ['requirements']`
        req, cond = r.split(';', 1)
        cond = ':' + cond
        cond_reqs = extras_require.setdefault(cond, [])
        cond_reqs.append(req)
    else:
        install_requires.append(r)

setup(name='kubezeug',
      version='0.0.1',
      description='Utilities for quick and easy distributed computing via dask-kubernetes, with a focus on ML applications.',
      maintainer='Brian Groenke',
      maintainer_email='brian.groenke@colorado.edu',
      license='MIT',
      install_requires=install_requires,
      extras_require=extras_require,
      packages=['kubezeug'],
      long_description=(open('README.md').read() if os.path.exists('README.md')
                        else ''),
      zip_safe=False)
