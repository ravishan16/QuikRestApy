from setuptools import setup

setup(
    name='quikrestapy',
    version='0.0.1',
    url='https://github.com/ravishan16/QuikRestApy',
    license='MIT',
    author='Ravishankar Sivasubramaniam',
    author_email='ravi_siva@live.com',
    description='Quick REST API using Python Flask/SQLAlchemy/SQLite',
    packages=['quikrestapy'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask>=0.12',
        'SQLAlchemy>=1.1.6',
        'flask-restplus>=0.10.1',
        'Flask-SQLAlchemy>=2.2'
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
)
