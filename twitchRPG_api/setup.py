from setuptools import setup

setup(
    name='twitchRPG_api',
    version='0.1',
    packages=[
        'twitchRPG_api',
        'twitchRPG_api.views'
    ],
    include_package_data=True,
    install_requires=[
        'flask',
        'Flask-HTTPAuth',
    ],
)
