import yaml
import os
import rich
def buildnav():
    datafile = open(f'{os.getcwd()}/blog10.yaml')
    data = yaml.load(datafile.read(), Loader=yaml.Loader)
    #print(data) # debug
    try:
        os.mkdir(f'{os.getcwd()}/build')
        builtnav = open(f'{os.getcwd()}/build/nav.html', mode='x')
    except FileExistsError:
        builtnav = open(f'{os.getcwd()}/build/nav.html', mode='w')
    if data["theme"] == 'yellow':
        builtnav.write(f'<nav style="color: white; width: 100%; background: #e6e600; font-size: 25px; padding: 5px; position: sticky; top: 0; font-family: arial;">{data["name"]}</nav>')
    else:
        builtnav.write(f'<nav style="color: white; width: 100%; background: {data["theme"]}; font-size: 25px; padding: 5px; position: sticky; top: 0; font-family: arial;">{data["name"]}</nav>')
def run():
    rich.print("[yellow]Building Navbar...")
    buildnav()
