from setuptools import setup, find_packages

setup(
    name="tms",
    version="0.3",
    packages=find_packages(),
    install_requires=["python-dotenv", "psycopg2"],
    test_suite="test",
)
