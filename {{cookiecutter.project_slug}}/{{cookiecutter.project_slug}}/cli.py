# -*- coding: utf-8 -*-

import argparse
import sys
import click


class {{cookiecutter.project_name|capitalize}}(object):

    def __init__(self):
        parser = argparse.ArgumentParser(
        description='{{cookiecutter.project_short_description}}',
        usage='''hello <command>
        example command : sample''')
        epilogue='''Credits :\n
        {{cookiecutter.full_name}} '''.format(__version__)
        parser.add_argument('command', help='Subcommand to run')
        parser.add_argument('--version', help='Print version', action='version', version='microservice version {{ cookiecutter.version }}')
        # parse_args defaults to [1:] for args, but you need to
        # exclude the rest of the args too, or validation will fail
        args = parser.parse_args(sys.argv[1:2])
        if not hasattr(self, args.command):
            print('Unrecognized command')
            parser.print_help()
            exit(1)
        # use dispatch pattern to invoke method with same name
        getattr(self, args.command)()
        
    def sample():
        print("Sample command")


@click.command()
def main(args=None):
    """Console script for {{cookiecutter.project_slug}}"""
    {{cookiecutter.project_name|capitalize}}()


if __name__ == "__main__":
    main()
