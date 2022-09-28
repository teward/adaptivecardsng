from setuptools import find_packages, setup
from adaptivecardsng import __version__ as version

setup(
    name='adaptivecardsng',
    version=version,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'typing'
    ],
    author='Thomas Ward',
    author_email='teward@thomas-ward.net',
    description="Python library to generate AdaptiveCard objects and their JSON code.",
    long_description="AdaptiveCards are being used by Microsoft for various frameworks like bot " \
                     "message cards and the Bot framework, but also for Teams messages and " \
                     "submission, as well as other uses of the AdaptiveCard spec.  The full spec " \
                     "is located at https://adaptivecards.io/explorer/ and is more or less " \
                     "fully implemented here.",
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
        'Topic :: Communications',
        'Topic :: Software Development :: Libraries'
    ]
)