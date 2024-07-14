# setup.py

from setuptools import setup, find_packages

setup(
    name="learning_fastapi",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "fastapi",
        "uvicorn",
        "pyjwt",
        "passlib[bcrypt]",
        "python-multipart",
        "python-jose",
        "requests",
    ],
    entry_points={
    "console_scripts": [
        "learning_fastapi=learning_fastapi.main:app",  # Use underscore here
    ],
},
)
