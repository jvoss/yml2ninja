# YML2Jinja

A simple utility to quickly render Jinja2 templates using variables specified in 
YAML. This is particularly useful utility for quickly creating device 
configurations.

## Example

    `yml2jinja examples/sample.yml examples/sample.j2`

## Options

By default, output is written to STDOUT which allowing the contents to be 
redirected however needed. However, a filename to write (`-w <filename>`) may be 
specified if necessary.

## Installation

1) Clone the repository

2) Install the requirements:

    `pip install -r requirements.txt`

3) Run `setup.py`:
   
    `python setup.py`

4) Use the script

    `bin/yml2jinja <yml_filename> <jinja_filename>`   
