from setuptools import setup,find_packages

setup(
        name = 'Kyrios',
        version = '0.1',
        packages = find_packages(),
        author = 'shihua',
        description = 'Kyrios Module',
        install_requires = ['networkx','ray','hydra-core','transitions']
)