from setuptools import find_packages, setup
setup(
    name="AQsystem with haystack",
    version="0.0.1",
    author="Bablu pandey",
    author_email="bablupandey446@gmail.com",
    packages=find_packages(),
    install_requires=["pinecone-haystack","haystack-ai","python-dotenv","pathlib ","Flask"]
)
