import os

from typing import Dict
from setuptools import setup, find_packages

ROOT_PATH = os.path.dirname(__file__)
PKG_NAME = "mlserver"
PKG_PATH = os.path.join(ROOT_PATH, PKG_NAME)


def _load_version() -> str:
    version = ""
    version_path = os.path.join(PKG_PATH, "version.py")
    with open(version_path) as fp:
        version_module: Dict[str, str] = {}
        exec(fp.read(), version_module)
        version = version_module["__version__"]

    return version


def _load_description() -> str:
    readme_path = os.path.join(ROOT_PATH, "README.md")
    with open(readme_path) as fp:
        return fp.read()


setup(
    name=PKG_NAME,
    version=_load_version(),
    url="https://github.com/SeldonIO/MLServer.git",
    author="Seldon Technologies Ltd.",
    author_email="hello@seldon.io",
    description="ML server",
    packages=find_packages(exclude=["tests", "tests.*"]),
    install_requires=[
        "click",
        # We pin version of fastapi
        # check https://github.com/SeldonIO/MLServer/issues/340
        "fastapi==0.68.2",
        "grpcio",
        "importlib-metadata;python_version<'3.8'",
        "numpy",
        "pandas",
        "protobuf",
        "uvicorn==0.17.5",
        "starlette_exporter",
        "py-grpc-prometheus",
        "cloudpathlib[gs]",
        "tortoise-orm",
        "fastapi_users[tortoise-orm]==9.3.0",
        "asyncpg",
        "python-dotenv",
        "google-cloud-storage==2.2.1", 
        "starlette==0.14.2",
        # "tortoise-orm==0.18.0"
    ],
    extras_require={"all": ["orjson"]},
    entry_points={"console_scripts": ["mlserver=mlserver.cli:main"]},
    long_description=_load_description(),
    long_description_content_type="text/markdown",
    license="Apache 2.0",
)
