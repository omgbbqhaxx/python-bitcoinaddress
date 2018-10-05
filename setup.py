from setuptools import setup

requires = ['']

setup(
    name='python-bitcoinaddress',
    version='0.2.2',
    description="Python bitcoin address validation",
    license="GPLv3",
    author="Yasin Aktimur",
    author_email="yasinaktimur@gmail.com",
    url='https://github.com/omgbbqhaxx/python-bitcoinaddress',
    keywords='bitcoin address validation',
    test_suite="tests",
    install_requires=requires,
    classifiers = [
        "Development Status :: 4 - Beta",
        "Programming Language :: Python",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ]
)
