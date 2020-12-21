import argparse
import jinja2
import yaml

from jinja2.meta import find_undeclared_variables


def arguments():
    '''Parse required arguments'''

    description = 'Process configuration templates.'
    parser = argparse.ArgumentParser(description=description)

    parser.add_argument('yaml', metavar='yamlfile', type=str,
                        help='yaml configuration file')

    parser.add_argument('template', metavar='templatefile', type=str,
                        help='yaml configuration file')

    parser.add_argument('-w', '--write', metavar='file', type=str,
                        help='write output to file')

    return parser.parse_args()


def load_yaml(filename):
    '''Loads the yml2conf YAML from filename'''

    try:
        return yaml.safe_load(open(filename, 'r'))

    except yaml.YAMLError as exception:
        print("Error in yaml file:", exception)
        exit()


def render(yaml, template):
    env = jinja2.Environment(undefined=jinja2.DebugUndefined)
    template = env.from_string(template)
    rendered = template.render(yaml)

    # Check if rendering was done correctly
    ast = env.parse(rendered)
    undefined = find_undeclared_variables(ast)

    if undefined:
        raise jinja2.UndefinedError(f'Variables are undefined: {undefined!r}')

    return rendered


def main():
    try:
        args = arguments()

        yaml_file = args.yaml
        yaml = load_yaml(yaml_file)

        template_file = args.template
        template = open(template_file, 'r').read()

        if args.write:
            f = open(args.write, 'w')
            f.write(render(yaml, template) + "\n")
            f.close()
            print('Template written to:', args.write)
        else:
            print(render(yaml, template))

    except FileNotFoundError as exception:
        print("File not found:", exception)

    except jinja2.UndefinedError as exception:
        print("Template error:", exception)

    exit()
