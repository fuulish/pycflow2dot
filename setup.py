"""Installation script."""
from setuptools import setup


name = 'pycflow2dot'
description = (
    'Create C call graphs from multiple source files '
    'using Cflow, producing linked PDF.')
long_description = open('README.md').read()
url = 'https://github.com/johnyf/{name}'.format(name=name)
install_requires = [
    'networkx >= 2.0',
    'pydot >= 1.2.3']
classifiers = [
    'Development Status :: 2 - Pre-Alpha',
    'Intended Audience :: Developers',
    ('License :: OSI Approved :: '
     'GNU General Public License v3 or later (GPLv3+)'),
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Topic :: Software Development']
keywords = [
    'c', 'call graph', 'control flow', 'dot',
    'latex', 'cflow']


def run_setup():
    setup(
        name='pycflow2dot',
        version='0.2.2',
        py_modules=['pycflow2dot'],
        license='GPLv3',
        description=description,
        long_description=long_description,
        long_description_content_type='text/markdown',
        author='Ioannis Filippidis',
        author_email='jfilippidis@gmail.com',
        url=url,
        install_requires=install_requires,
        entry_points={
            'console_scripts': ['cflow2dot = pycflow2dot:main']},
        classifiers=classifiers,
        keywords=keywords)


if __name__ == '__main__':
    run_setup()
