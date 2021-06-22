from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='clockify-api-client',
    version='0.0.2',
    author="Michael Bláha",
    author_email="michael.blaha@eluvia.com",
    description="Simple python API client for clockify. Inspired by https://pypi.org/project/clockify/ library.",
    long_description=long_description,
    py_modules=['clockify_api_client'],
    long_description_content_type="text/markdown",
    url="https://github.com/eluvia-com/clockify-api-aclient",
    package_dir={'': 'clockify_api_client'},
    install_requires=['requests', 'factory_boy'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    extras_require={"dev": ["twine"]}
)
