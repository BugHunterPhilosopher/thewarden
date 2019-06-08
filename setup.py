from setuptools import setup, find_packages

setup(
    name='cryptoalpha',
    version='0.1',
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
    'APScheduler==3.6.0',
    'bcrypt==3.1.6',
    'blinker==1.4',
    'certifi==2019.3.9',
    'cffi==1.12.3',
    'chardet==3.0.4',
    'Click==7.0',
    'Flask==1.0.2',
    'Flask-Bcrypt==0.7.1',
    'Flask-Login==0.4.1',
    'Flask-Mail==0.9.1',
    'Flask-SQLAlchemy==2.3.2',
    'Flask-WTF==0.14.2',
    'idna==2.8',
    'itsdangerous==1.1.0',
    'Jinja2==2.10.1',
    'lxml==4.3.3',
    'MarkupSafe==1.1.1',
    'numpy==1.16.2',
    'pandas==0.24.2',
    'Pillow==5.4.1',
    'pycparser==2.19',
    'python-dateutil==2.8.0',
    'python-dotenv==0.10.1',
    'pytz==2018.9',
    'requests==2.22.0',
    'six==1.12.0',
    'SQLAlchemy==1.3.4',
    'tzlocal==1.5.1',
    'urllib3==1.25.3',
    'Werkzeug==0.15.1',
    'wrapt==1.11.1',
    'WTForms==2.2.1'
    ]


)
