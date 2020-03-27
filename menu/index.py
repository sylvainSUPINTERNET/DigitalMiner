import click

from commands.pull import pull
from commands.exemple import initdb, dropdb


@click.group()
def menu():
    pass


menu.add_command(initdb)
menu.add_command(dropdb)
menu.add_command(pull)
