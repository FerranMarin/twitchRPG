from setuptools import setup

setup(
    name='twitchRPG_core',
    version='1.3',
    packages=[
        'twitchRPG_core',
        'twitchRPG_core.config',
        'twitchRPG_core.notify',
        'twitchRPG_core.notify.templates',
    ],
    package_data={
        'twitchRPG_core.notify.templates': ['*.tmpl'],
    },
    include_package_data=True,
    install_requires=[
        'pymysql',
        'requests',
        'redis',
        'psutil',
        'httplib2',
        'tweepy',
        'arrow',
        'click',
        'jinja2',
    ],
)
