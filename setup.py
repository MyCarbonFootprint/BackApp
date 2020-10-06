from setuptools import find_packages, setup

setup(
    name='footprint-api',
    version='0.0.1',
    url='https://github.com/MyCarbonFootprint/BackApp',
    license='Closed Source',
    maintainer='Louis Paret',
    maintainer_email='louis.paret@gmail.com',
    description='API',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'json-logging-py',
        'flask',
        'gunicorn',
        'flasgger',
    ],
    extras_require={
        'test': [
            'pytest',
        ],
    },
)
