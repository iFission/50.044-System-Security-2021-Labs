import os

from setuptools import setup, find_packages

requires = [
    'pyramid',
    'pyramid_chameleon',
    'pyramid_debugtoolbar',
    'waitress',
    'bcrypt',
    ]

setup(name='xss-demo',
      version='0.0',
      description='xss-demo',
      long_description='xss-demo',
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web pyramid pylons',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="xss_demo",
      entry_points="""\
      [paste.app_factory]
      main = xss_demo:main
      """,
      )
