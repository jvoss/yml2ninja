import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="yml2jinja",
    version="0.0.1",
    author="Jonathan P. Voss",
    author_email="voss.jonathan@gmail.com",
    description="A simple utility to render Jinja2 templates from YAML",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jvoss/yml2jinja",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
