#!/usr/bin/env python

version = "2.2.3"

requirements =     [
    'cloudmesh_base',
    'cmd3',
    'cloudmesh',
    'concurrent',
    'futures',
    'pyaml',
    'simplejson',
    'nose',
    'docopt',
    'sphinx',
    'sphinx-autobuild',
    'sphinx_bootstrap_theme',
    'sphinx_rtd_theme',
    'sphinxcontrib-autorun',
    'sphinxcontrib-blockdiag',
    'sphinxcontrib-exceltable',
    'sphinxcontrib-webmocks',
    'actdiag',
    'blockdiag',
    'blockdiagcontrib-square',
    'blockdiagcontrib-qb',
    'blockdiagcontrib-class',
    'blockdiagcontrib-cisco',
    'nwdiag',
    'seqdiag',
    'sphinxcontrib-httpdomain',
    'ipython',
    'sh',
    'fabric',
    'nose',
    'autopep8',
    'markupsafe',
    'mkdocs',
    'ghp-import',
    'jsonschema',
    'mistune',
    ]

import glob
import os
from cloudmesh_base.util import banner
from setuptools import setup, find_packages
from setuptools.command.install import install

try:
    from cloudmesh_base.util import banner
except:
    os.system("pip install cloudmesh_base")

from cloudmesh_base.util import banner
from cloudmesh_base.util import path_expand
from cloudmesh_base.Shell import Shell
from cloudmesh_base.util import auto_create_version
from cloudmesh_base.util import auto_create_requirements



# try:
#     from fabric.api import local
# except:
#     os.system("pip install fabric")
#     from fabric.api import local

home = os.path.expanduser("~")

banner("Install cloudmesh Doc Framework")
#auto_create_version("cloudmesh_pbs", version)
auto_create_requirements(requirements)

class CreateRequirementsFile(install):
    """Create the requiremnets file."""
    def run(self):    
        auto_create_requirements(requirements)

class UploadToPypi(install):
    """Upload the package to pypi."""
    def run(self):
        # auto_create_version("cloudmesh_pbs", version)
        auto_create_requirements(requirements)
        os.system("make clean")
        os.system("python setup.py install")                
        banner("Build Distribution")
        os.system("python setup.py sdist --format=bztar,zip upload")        

class RegisterWithPypi(install):
    """Upload the package to pypi."""
    def run(self):
        banner("Register with Pypi")
        os.system("python setup.py register")        

class InstallBase(install):
    """Install the package."""
    def run(self):
        # auto_create_version("cloudmesh_pbs", version)
        auto_create_requirements(requirements)
        banner("Install Cloudmesh Doc Framework")
        install.run(self)

class InstallRequirements(install):
    """Install the requirements."""
    def run(self):
        banner("Install Cloudmesh Doc Requirements")
        os.system("pip install -r requirements.txt")
        
class InstallAll(install):
    """Install requirements and the package."""
    def run(self):
        banner("Install Cloudmesh Doc Framework Requirements")
        os.system("pip install -r requirements.txt")
        banner("Install Cloudmesh Doc Framework")
        install.run(self)

class CreateDoc(install):
    """Install requirements and the package."""
    def run(self):
        banner("Create Documentation")
        os.system("python setup.py install")
        os.system("sphinx-apidoc -o docs/source cloudmesh_pbs")
        os.system("cd docs; make -f Makefile html")

setup(
    name='cloudmesh_doc',
    version=version,
    description='A simple pbs queue management framework for multiple supercomputers',
    # description-file =
    #    README.rst
    author='Cloudmesh Team',
    author_email='laszewski@gmail.com',
    url='http://github.org/cloudmesh/introduction_to_cloud_computing',
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
        'Topic :: Database',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering',
        'Topic :: System :: Clustering',
        'Topic :: System :: Distributed Computing',
        'Topic :: System :: Boot',
        'Topic :: System :: Systems Administration',
        'Framework :: Flask',
        'Environment :: OpenStack',
    ],
    packages=find_packages(),
    include_package_data=True,
#    data_files=[
#        (home + '/.cloudmesh', [
#            'etc/FGLdapCacert.pem',
#            'etc/india-havana-cacert.pem',
#            'etc/cloudmesh_flavor.yaml']),
#        (home + '/.cloudmesh/etc', [
#            'etc/cloudmesh.yaml',
#            'etc/me-none.yaml',
#            'etc/cloudmesh.yaml',
#            'etc/cloudmesh_server.yaml',
#            'etc/cloudmesh_rack.yaml',
#            'etc/cloudmesh_celery.yaml',
#            'etc/cloudmesh_mac.yaml',
#            'etc/cloudmesh_flavor.yaml',
#            'etc/ipython_notebook_config.py']),
#    ],
#    entry_points={'console_scripts': [
#        'cm-cluster = cloudmesh.cluster.cm_shell_cluster:main',
#    ]},
    install_requires=requirements,
    cmdclass={
        'install': InstallBase,
        'requirements': InstallRequirements,
        'all': InstallAll,
        'pypi': UploadToPypi,
        'pypiregister': RegisterWithPypi, 
        'create_requirements': CreateRequirementsFile,
        'doc': CreateDoc,
        },
)

