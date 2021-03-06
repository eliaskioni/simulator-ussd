from setuptools import setup, find_packages
import os
# -*- Installation Requires -*-


def strip_comments(l):
    return l.split('#', 1)[0].strip()


def _pip_requirement(req):
    if req.startswith('-r '):
        _, path = req.split()
        return reqs(*path.split('/'))
    return [req]


def _reqs(*f):
    return [
        _pip_requirement(r) for r in (
            strip_comments(l) for l in open(
                os.path.join(os.getcwd(), *f)).readlines()
        ) if r]


def reqs(*f):
    return [req for subreq in _reqs(*f) for req in subreq]

install_requires = reqs('requirements.txt')

setup(
    name='simulator-ussd',
    version='4.0.0b1.0',
    description='USSD util for Django',
    author='Sam Kitonyi',
    author_email='sam.kitonyi@gmail.com',
    url='https://bitbucket.org/wezatele/django-ussd',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    zip_safe=True,
    install_requires=install_requires
)
