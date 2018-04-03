from setuptools import setup

setup(name='regalii',
      version='4.0.3',
      description="A Python HTTP client for consuming Regalii's API",
      url='https://github.com/regalii/regaliator_python',
      author='Regalii',
      author_email='support@regalii.com',
      license='MIT',
      packages=['regalii', 'regalii.clients', 'regalii.tests'],
      install_requires=[
          'pytz',
          'requests',
          'mock',
          'requests-mock'
      ],
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)
