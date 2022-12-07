'''
To run flask on Windows
in PowerShell -> $env:FLASK_APP="quokka"
$env:FLAK_ENV="development"
and then: flask run
'''

from setuptools import setup

setup(
    name='quokka',
    packages=['quokka'],
    include_package_data=True,
    install_requires=[
        'flask',
    ]
)