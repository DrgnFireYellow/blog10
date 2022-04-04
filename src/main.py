import click
import buildposts
import newblog
import buildnav
import os
import builddb
import rich
import rich.traceback
from rich.progress import track
@click.group()
@click.option("--debug", "-d", type=click.BOOL, default=False)
def cli(debug):
    if debug == True:
        rich.print("[dark_red]Debug mode: on[/dark_red]")
        rich.traceback.install()

@cli.command()
def build():
    for task in track([builddb, buildnav, buildposts], description="building"):
        task.run()
@cli.command()
@click.argument("name", type=click.STRING)
def new(name):
    newblog.run(name)
@cli.command(help="Start a server to display the blog on.")
@click.option("--port", "-p", default="8080", help="The port on which the server will run.", type=click.INT)
def serve(port):
    build()
    os.system(f"python3 -m http.server {port} --directory {os.getcwd()}/build")

if __name__ == '__main__':
    cli(prog_name="blog10")