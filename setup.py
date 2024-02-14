from setuptools import setup, find_packages

setup(
    name="tms",
    version="0.4",
    packages=find_packages(),
    install_requires=["python-dotenv", "psycopg2", "PySimpleGUI", "sphinx"],
    tests_require=["coverage"],
    test_suite="test",
)
