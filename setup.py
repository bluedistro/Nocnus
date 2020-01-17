import setuptools

SHORT_DESCRIPTION = """
Nocnus is a basic Pymongo wrapper for quickly implementing CRUD MongoDB operations.
""".strip()

LONG_DESCRIPTION = """
Nocnus is a simple Python library built on top of Pymongo to simplify just the 
basic MongoDB CRUD operations and save some DB setup time.

Why the name Nocnus?
Ocnus is the name of the greek god of delays and frustrations and we
do not want any any of those in implementing basic CRUD MongoDB operations
thus the name. (No Ocnus => Nocnus)

Kindly check out the complete documentation at: https://github.com/bluedistro/Nocnus
 """.strip()

setuptools.setup(
    author="Kingsley Biney",
    author_email="bineykingsley36@gmail.com",
    name="Nocnus",
    license="MIT",
    description=SHORT_DESCRIPTION,
    version="v0.0.7",
    long_description=LONG_DESCRIPTION,
    url="https://github.com/bluedistro/Nocnus",
    packages=setuptools.find_packages(),
    python_requires=">=3.5",
    install_requires=['pymongo'],
    classifiers=[
                # Trove classifiers
        # (https://pypi.python.org/pypi?%3Aaction=list_classifiers)
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
    ],
)