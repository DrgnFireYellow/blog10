import yaml
import os
import rich
def newblog(name):
    os.mkdir(f"{os.getcwd()}/{name}")
    config = open(f"{os.getcwd()}/{name}/blog10.yaml", mode="x")
    config.write(yaml.dump({'name': name}))
    config.close()
    os.mkdir(f"{os.getcwd()}/{name}/posts")
def run(name):
    rich.print("[yellow]Creating Blog...[/yellow]", end="")
    newblog(name)
    rich.print("[green4]done[/green4]")
