from setuptools import find_packages, setup

with open("requirements.txt", "r") as file:
    lines = file.readlines()

reqs = [req for req in lines if "#" not in req]

setup(name="icecream", packages=find_packages(), install_requires=reqs)
