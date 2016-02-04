import os
from setuptools import setup


with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()


# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


setup(
    name='django-user2mailchimp',
    version='1.0.7',
    packages=['user2mailchimp'],
    include_package_data=True,
    license='BSD License',
    description='Synchronize users to mailing list Mailchimp.',
    long_description=README,
    url='https://github.com/treemo/user2mailchimp',
    author='Treemo',
    author_email='treemo@hotmail.fr',
    install_requires=[
        'mailchimp',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)