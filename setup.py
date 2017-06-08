from setuptools import setup
import storages


def read(filename):
    with open(filename) as f:
        return f.read()


def get_requirements_tests():
    with open('requirements-tests.txt') as f:
        return f.readlines()

# internal pypi name and version we can reference with pip
# This should match (using pip and pypi.nrpgl.us), the patched code
# Ethan & Aaron fixed in september 2016, but without the github egg
# install

# Yes, Virginia, this is hack upon a hack...
setup(
    name='django-storages-ep',
    version='1.5.1',
    packages=['storages', 'storages.backends'],
    author='Josh Schneier',
    author_email='josh.schneier@gmail.com',
    license='BSD',
    description='Support for many storages (S3, MogileFS, etc) in Django.',
    long_description=read('README.rst') + '\n\n' + read('CHANGELOG.rst'),
    url='https://github.com/jschneier/django-storages',
    classifiers=[
        'Framework :: Django',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    tests_require=get_requirements_tests(),
    test_suite='tests',
    zip_safe=False
)
