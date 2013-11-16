from setuptools import setup, find_packages
import sys, os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
NEWS = open(os.path.join(here, 'NEWS.txt')).read()


version = '0.1'

install_requires = [
    'simplejson>=2.3.2',
]


setup(name='python-expresspigeon',
    version=version,
    description="Python Library for https://expresspigeon.com API",
    long_description=README + '\n\n' + NEWS,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Natural Language :: English',
    ],
    keywords='Expresspigeon Newsletter API',
    author='Fundology',
    author_email='support@fundology.com',
    url='https://github.com/fundology/python-expresspigeon',
    license='GNU General Public License v2 (GPLv2)',
    packages=['expresspigeon'],
    zip_safe=False,
    install_requires=install_requires,
    entry_points={
        'console_scripts':
            ['expresspigeon=expresspigeon:main']
    }
)
