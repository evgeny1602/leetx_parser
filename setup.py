import setuptools

setuptools.setup(
    name="leetx_parser",
    version="0.1.0",
    url="https://github.com/evgeny1602/leetx_parser",

    author="Evgeny Lobanov",
    author_email="evgeny1602@gmail.com",

    description="Find magnet links for TV show episodes",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=[],

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
