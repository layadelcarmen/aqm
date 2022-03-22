import os
import re

from setuptools import find_packages, setup

regexp = re.compile(r'.*__version__ = [\'\"](.*?)[\'\"]', re.S)

base_package = 'm_load'
base_path = os.path.dirname(__file__)

init_file = os.path.join(base_path, 'src', 'aqm', '__init__.py')
with open(init_file, 'r') as f:
    module_content = f.read()

    match = regexp.match(module_content)
    if match:
        version = match.group(1)
    else:
        raise RuntimeError(
            'Cannot find __version__ in {}'.format(init_file))

with open('README.rst', 'r') as f:
    readme = f.read()

with open('CHANGELOG.rst', 'r') as f:
    changes = f.read()

def parse_requirements(filename):
    ''' Load requirements from a pip requirements file '''
    with open(filename, 'r') as fd:
        lines = []
        for line in fd:
            line.strip()
            if line and not line.startswith("#"):
                lines.append(line)
    return lines

requirements = parse_requirements('requirements.txt')


if __name__ == '__main__':
    setup(
        name='measure_load',
        description='Python script to load air quality measures JSON to a PostgreSQL database ad create some views.',
        long_description='\n\n'.join([readme, changes]),
        entry_points={
        'console_scripts': ['m-load=aqm.m_load:main', 'r-views=aqm.run_create_views:main'],
        },
        license='Not open source',
        url='https://github.com/layadelcarmen/aqm',
        version=version,
        author='Laya Rabasa',
        author_email='layadelcarmen@gmail.com',
        maintainer='Laya Rabasa',
        maintainer_email='layadelcarmen@gmail.com',
        install_requires=requirements,
        keywords=['m_load'],
        package_dir={'': 'src'},
        packages=find_packages('src'),
        zip_safe=False,
        classifiers=['Development Status :: 3 - Alpha',
                     'Intended Audience :: Developers',
                     'Programming Language :: Python :: 3.8']
    )
