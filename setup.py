import os
from setuptools import find_packages, setup
from distutils import sysconfig


with open('./README.md', 'r') as f:
    long_description = f.read()

site_packages_path = sysconfig.get_python_lib(prefix='./')

setup(
    name='pbs-python',
    version='2020.10.19',
    description='Openpbs/Torque Python interface',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/exabyte-io/pbs-python',
    author='Radik Fattakhov',
    author_email='info@exabyte.io',
    license='LGPLv3',
    keywords=['pbs'],
    packages=find_packages(exclude=['tests*']),
    data_files=[
        (os.path.join(site_packages_path, 'pbs'), ['_pbs.so']),
        (os.path.join(site_packages_path, 'pbs'), ['_pbs.cpython-38-x86_64-linux-gnu.so'])
    ],
    python_requires='>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*,!=3.5.*,!=3.6.*,!=3.7.*,<3..9',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Operating System :: POSIX :: Other',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)'
    ]
)
