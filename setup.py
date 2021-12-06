from setuptools import find_packages
from setuptools import setup

setup(name='nodepsexecutable',
      version='1',
      description='no deps executable',
      author='Vito De Tullio',
      author_email='vito.detullio@gmail.com',
      license='GPL3',
      packages=find_packages(),
      zip_safe=False,
      entry_points={
          'console_scripts': [
              'nodepsexecutable=nodepsexecutable:main'
          ],
      })
