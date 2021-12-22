from setuptools import setup, find_packages


setup(
    name="stars_project",
    version="1.0.0",
    description="Package to convert string with stars",
    author="Kirill Borisyuk",
    author_email="hurricanekba@gmail.com",
    packages=find_packages(include=['stars_project', 'stars_project.*']),
    install_requires=[
        'argparse', 'pytest'
    ],
    zip_safe=False)