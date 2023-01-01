import re

from setuptools import setup

requirements = []
with open("requirements.txt", encoding="utf8") as f:
    requirements = f.read().splitlines()

version = ""
with open("discord/__init__.py", encoding="utf8") as f:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE
    ).group(1)

if not version:
    raise RuntimeError("version is not set")

readme = ""
with open("README.md", encoding="utf8") as f:
    readme = f.read()

extras_require = {
    "voice": ["PyNaCl>=1.3.0,<1.6"],
    "docs": [
        "sphinx==4.4.0",
        "sphinxcontrib_trio==1.1.2",
        "sphinxcontrib-websupport",
        "typing-extensions>=4.3,<5",
    ],
    "speed": [
        "orjson>=3.5.4",
        "aiodns>=1.1",
        "Brotli",
        'cchardet==2.1.7; python_version < "3.10"',
    ],
    "test": [
        "coverage[toml]",
        "pytest",
        "pytest-asyncio",
        "pytest-cov",
        "pytest-mock",
        "typing-extensions>=4.3,<5",
    ],
}

packages = [
    "discord",
    "discord.types",
    "discord.ui",
    "discord.webhook",
    "discord.app_commands",
    "discord.ext.commands",
    "discord.ext.tasks",
]

setup(
    name="endless_medical",
    author="Leg3ndary",
    url="https://github.com/Leg3ndary/EndlessMedical",
    # project_urls={
    #     "Documentation": "https://github.com/Leg3ndary/EndlessMedical
    # },
    version=version,
    packages=packages,
    license="MIT",
    description="A Python wrapper for the Endless Medical API",
    long_description=readme,
    long_description_content_type="text/x-rst",
    include_package_data=True,
    install_requires=requirements,
    extras_require=extras_require,
    python_requires=">=3.8.0",
    classifiers=[
        "Development Status :: 1 - Planning Copy.",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
)
