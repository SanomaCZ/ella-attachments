from setuptools import setup, find_packages

VERSION = (0, 1, 0)
__version__ = VERSION
__versionstr__ = '.'.join(map(str, VERSION))

install_requires = [
    'ella>=2,<4',
    'South>=0.7',
]

setup(
    name='ella-attachments',
    version=__versionstr__,
    description='Add attachments to Ella Publishable',
    author='SMP Online Development Team',
    author_email='online-dev@sanomamedia.cz',
    maintainer='Vitek Pliska',
    maintainer_email='whit@smdev.cz',
    license='BSD',
    url='https://github.com/SanomaCZ/ella-attachments',

    packages=find_packages(
        where='.',
        exclude=('test_ella_attachments',)
    ),

    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],

    include_package_data=True,
    install_requires=install_requires,
)
