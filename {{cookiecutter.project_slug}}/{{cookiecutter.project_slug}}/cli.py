# -*- coding: utf-8 -*-

import click

@click.command()
def main(args=None):
    """Console script for {{cookiecutter.project_slug}}"""
    click.echo("#"*50)
    click.echo(click.style("{{cookiecutter.project_name}}", fg='green', bold=True))
    click.echo("#"*50)


if __name__ == "__main__":
    main()
