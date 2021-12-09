from setuptools import setup, find_packages
from transitionMatrix.version import ver
__version__ = ver

def readme():
    with open('./README.md') as f:
        return f.read()


setup(name='transitionMatrix',
      packages=find_packages(),
      package_data={'transitionMatrix': ['datasets/*/*']},
      version=ver,
      include_package_data=True,
      python_requires='>=3.6',
      description='A Python powered library for statistical analysis and visualization of state transition phenomena',
      long_description=readme(),
      author='Open Risk',
      author_email='info@openrisk.eu',
      url='https://github.com/open-risk/transitionMatrix',
      license='OSI',
      classifiers = [],
      install_requires=[
          'pandas',
          'numpy',
          'scipy',
          'statsmodels',
          'sympy',
          'matplotlib'
      ],
      zip_safe=False)