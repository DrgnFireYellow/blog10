import click
import buildposts
import newblog
import buildnav
@click.group()
def cli():
    pass
@cli.command()
def build():
    buildnav.run()
    buildposts.run()
@cli.command()
@click.argument("name", type=click.STRING)
def new(name):
    newblog.run(name)


if __name__ == '__main__':
    cli(prog_name="blog10")