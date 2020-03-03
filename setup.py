from setuptools import setup, find_packages

long_description = ''

with open('README.md', 'r') as fh:
  long_description = fh.read()

setup(
  name='numerica',
  version='0.2.1',
  description='Numerical Analysis methods with Python (experimental)',
  long_description=long_description,
  long_description_content_type='text/markdown',
  url='http://github.com/ramesaliyev/numerica',
  author='Rames Aliyev',
  author_email='creator@ramesaliyev.com',
  license='MIT',
  packages=find_packages(),
  zip_safe=False)