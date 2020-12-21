# YML2Jinja

A simple utility to quickly render Jinja2 templates using variables specified in 
a YAML file. This is useful for quickly creating template based device 
configurations.

## Example

    `yml2jinja examples/sample.yml examples/sample.j2`

## Options

By default, output is written to STDOUT allowing the result to be redirected 
however needed. However a filename (`-w <filename>`) to write may be specified 
if necessary.

## Developmental Installation

1) Clone the repository

2) Install the requirements:

    `pip install -r requirements.txt`

3) Run `setup.py`:
   
    `python setup.py develop`

4) Use the script:

    `bin/yml2jinja <yml_filename> <jinja_filename>`   
