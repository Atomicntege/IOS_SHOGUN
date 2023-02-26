#!/usr/bin/python3

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='IOS_SHOGUN',
    version='1.0.0',
    author='AtomicJun',
    author_email='q2372798989@163.com',
    maintainer='IOS-SHOGUN-PublishingDepartment',
    description='shogun-python3 module 1.0 - updated: blocking byte buffers --+console logs + console_colors Reset '
                'the terminal color font + bufferState hunger state',
    long_description=open('README.md', 'r').read(),
    long_description_content_type="""text/markdown""",
    url="https://github.com/Atomicntege/IOS_SHOGUN/tree/Python_IOS_SHOGUN_Model",
    packages=setuptools.find_packages(),
    platforms=["all"],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ]
)
