import click
from delivery.ext.auth.controller import create_user
from delivery.ext.auth.models import User
  
    

def list_users():
    users = User.query.all()
    click.echo(f"users list {users}")


@click.option("--email", "-e")
@click.option("--passwd", "-p")
@click.option("--admin", "-a", is_flag=True, default=False)
def add_user(email, passwd, admin):
    create_user(
        email=email,
        passwd=password,
        admin=admin
    )

    click.echo(f"User {email} sucessfully created ")

