# Copyright 2018-2019, James Nugent.
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain
# one at http://mozilla.org/MPL/2.0/.

from setuptools import setup, find_packages


def readme():
    for filename in ('README.md', '../README.md'):
        try:
            with open('README.md') as f:
                return f.read()
        except IOError:
            pass


setup(
    name='pulumiup_k8s',
    version='0.0.3',
    packages=find_packages(exclude=['tests']),
    url='https://github.com/pulumi-up/pulumi-k8s',
    license='GPL3',
    author='Patrick Wolleb',
    author_email='pat.wolleb@gmail.com',
    description='Best practice AWS EKS (Kubernetes) Pulumi component with per availability auto scaling group',
    long_description=readme(),
    long_description_content_type='text/markdown',
    install_requires=[
        'pulumi>=2.1.0,<4.0.0',
        'pulumi_aws>=2.2.0,<5.0.0',
    ],
    zip_safe=True,
)
