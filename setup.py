from setuptools import setup, find_packages

classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]

setup(
  name='PyMailer',
  version='0.0.1',
  description='Simple tools for sending mail',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='MrJacob',
  author_email='jacob@fern.fun',
  license='MIT', 
  classifiers=classifiers,
  keywords='email', 
  packages=find_packages(),
  install_requires=[''] 
)
