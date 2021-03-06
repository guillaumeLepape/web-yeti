from setuptools import setup

setup(
    name="Yak Toto",
    version="1.0",
    long_description=__doc__,
    packages=["server"],
    install_requires=[
        "Flask-SQLAlchemy >= 2.5",
        "Flask-Cors >= 3.0",
        "requests >= 2.25",
        "DateTime >= 4.4",
        "PyJWT >= 2.4.0",
    ],
)
