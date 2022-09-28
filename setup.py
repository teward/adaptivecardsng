from setuptools import find_packages, setup
from adaptivecardsng import __version__ as version

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='adaptivecardsng',
    version=version,
    packages=find_packages(),
    include_package_data=True,
    author='Thomas Ward',
    author_email='teward@thomas-ward.net',
    url='https://github.com/teward/adaptivecardsng',
    description="Python library to generate AdaptiveCard objects and their JSON code.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='GPLv3+',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    python_requires='>=3.7.0'
)
