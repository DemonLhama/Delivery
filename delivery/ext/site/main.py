from flask import render_template, current_app, Blueprint, redirect
from delivery.ext.auth.form import UserForm
from delivery.ext.auth.controller import create_user


bp = Blueprint("site", __name__)


@bp.route("/")
def index():
    return render_template("index.html")

@bp.route("/about")
def about():
    return render_template("about.html")

@bp.route("/registration", methods=["GET", "POST"])
def registration():
    form = UserForm()
    if form.validate_on_submit():
        create_user(
            email=form.email.data,
            passwd=form.password.data
        )
        
        
        # forçar login
        return redirect("/")

    return render_template("userform.html", form=form)

@bp.route("/restaurants")
def restaurants():
    return render_template("restaurants.html")

@bp.route("/categories")
def categories():
    return render_template("categories.html")