import os
import rich
import shutil
def buildpost(post):
    # Open Post
    postfile = open(f'{os.getcwd()}/posts/{post}/post.txt')
    postcontent = postfile.read()
    # Format into html
    postcontent = postcontent.replace("h-", "<h2>")
    postcontent = postcontent.replace("-h", "</h2>")
    
    try:
        os.makedirs(f"{os.getcwd()}/build/posts/{post}")
        builtpost = open(f"{os.getcwd()}/build/posts/{post}/index.html", mode='x')
    except FileExistsError:
        builtpost = open(f"{os.getcwd()}/build/posts/{post}/index.html", mode='w')
    shutil.copy2(f"{os.getcwd()}/posts/{post}/cover.png", f"{os.getcwd()}/build/posts/{post}/cover.png")
    builtpost.write(f"<h1>{post}</h1>")
    builtpost.write(f'<img src="cover.png">')
    builtpost.write(postcontent)
    builtpost.close()
def run():
    rich.print("[yellow]Building Posts...[/yellow]", end="")
    posts = os.listdir(f'{os.getcwd()}/posts')
    for post in posts:
        buildpost(post)
    rich.print("[green]done[/green]")
if __name__ == "__main__":
    run()