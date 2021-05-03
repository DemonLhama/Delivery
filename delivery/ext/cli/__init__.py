import click
from delivery.ext.db import db
from delivery.ext.auth.models import User
from delivery.ext.db import models


def init_app(app):

    @app.cli.command()
    def create_db():
        db.create_all()

    @app.cli.command()
    @click.option("--email", "-e")
    @click.option("--passwd", "-p")
    @click.option("--admin", "-a", is_flag=True, default=False)
    def add_user(email, passwd, admin):
        user = User(
            email=email,
            passwd=passwd,
            admin=admin
        )
        db.session.add(user)
        db.session.commit()

        click.echo(f"User {email} sucessfully created ")


    @app.cli.command()
    def show_orders():
        click.echo("order list")
