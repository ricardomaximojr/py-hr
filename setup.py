from setuptools import setup, find_packages

with open('README.rst', encoding='UTF-8') as f:
    readme = f.read()

setup(
    name='py-hr',
    version='0.1.0',
    description='Python package to manage users on a server based on an inventory JSON file.',
    long_description='readme',
    author='Ricardo Maximo Jr',
    author_email='ricardomaximojr@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[]
    entry_points=(
        'console_scripts': 'py-hr=hr.cli:main'
    )
)