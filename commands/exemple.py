import click


@click.command()
def initdb():
    click.echo('Initialized the database')


@click.command()
def dropdb():
    click.echo('Dropped the database')


