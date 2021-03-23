import click


@click.group()
def cli():
    pass


@click.command()
def boot_up():
    click.echo("boot up started!")


cli.add_command(boot_up)