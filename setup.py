import setuptools
import leetx_parser

setuptools.setup(
    name="leetx_parser",
    version=leetx_parser.__version__,
    url="https://github.com/evgeny1602/leetx_parser",

    author="Evgeny Lobanov",
    author_email="evgeny1602@gmail.com",

    description="Find magnet links for TV show episodes",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=[
        'atomicwrites==1.1.5',
        'attrs==18.1.0',
        'BeautifulSoup==3.2.1',
        'certifi==2018.4.16',
        'chardet==3.0.4',
        'colorama==0.3.9',
        'funcsigs==1.0.2',
        'httpretty==0.9.5',
        'idna==2.7',
        'more-itertools==4.3.0',
        'pathlib2==2.3.2',
        'pluggy==0.7.1',
        'py==1.5.4',
        'pytest==3.7.1',
        'requests==2.19.1',
        'scandir==1.8',
        'six==1.11.0',
        'urllib3==1.23',    
    ],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
