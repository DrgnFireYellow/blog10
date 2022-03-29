import os
import rich
import shutil
def buildpost(post):
    # Open Post
    postfile = open(f'{os.getcwd()}/posts/{post}/post.txt')
    postcontent = postfile.read()
    # Get navbar
    navbarfile = open(f'{os.getcwd()}/build/nav.html')
    navbar = navbarfile.read()
    # Format into html
    postcontent = postcontent.replace("h-", "<h2>")
    postcontent = postcontent.replace("-h", "</h2>")
    postcontent = postcontent.replace("-br-", "<br>")
    postcontent = postcontent.replace("b-", "<b>")
    postcontent = postcontent.replace("-b", "</b>")
    postcontent = postcontent.replace("i-", "<i>")
    postcontent = postcontent.replace("-i", "</i>")
    postcontent = postcontent.replace("code-", '<code style="background: black; color: white;">')
    postcontent = postcontent.replace("-code", "</code>")
    coverexists = True
    try:
        os.makedirs(f"{os.getcwd()}/build/posts/{post}")
        builtpost = open(f"{os.getcwd()}/build/posts/{post}/index.html", mode='x')
    except FileExistsError:
        builtpost = open(f"{os.getcwd()}/build/posts/{post}/index.html", mode='w')
    try:
        shutil.copy2(f"{os.getcwd()}/posts/{post}/cover.png", f"{os.getcwd()}/build/posts/{post}/cover.png")
    except FileNotFoundError:
        coverexists = False
    builtpost.write(navbar)
    builtpost.write(f"<h1>{post}</h1>")
    if coverexists == True:
        builtpost.write(f'<img src="cover.png" style="width: 100%; height: auto;">')
    builtpost.write(postcontent)
    builtpost.close()
def run():
    rich.print("[yellow]Building Posts...[/yellow]", end="")
    posts = os.listdir(f'{os.getcwd()}/posts')
    for post in posts:
        buildpost(post)
    rich.print("[green4]done[/green4]")
if __name__ == "__main__":
    run()