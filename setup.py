from setuptools import setup, find_packages

setup(
    name="babytracker",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django>=4.2',
        'djangorestframework>=3.14',
        'psycopg2-binary>=2.9',
        'django-cors-headers>=3.13',
        'drf-spectacular>=0.27',
    ],
)
