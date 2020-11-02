from setuptools import setup, find_packages


with open('requirements.txt') as f:
    requirements = f.read().splitlines()

with open("readme.md", "r") as fh:
    long_description = fh.read()

setup(
    name="Game of 15",
    version="0.0.1",
    author="Edoardo Zucchelli",
    description="Game of 15 package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/edoardozucchelli/game_of_15",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=requirements,
    setup_requires=['pytest-runner'],
    tests_require=['pytest']
)
