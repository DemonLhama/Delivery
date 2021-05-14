from werkzeug.security import generate_password_hash, check_password_hash
from delivery.ext.auth.models import User
from delivery.ext.db import db


#To create a user: You will need the class User created in models and the db (SQLachemy)
# In password use werkzeug hashing to add an algorithm with 
# generate_password_hash and his values to hinder user password (SECURITY!)    

def create_user(email:str, passwd:str, admin:bool = False) -> User:
    user = User(
        email = email, 
        passwd = generate_password_hash(passwd, method="pbkdf2:sha256", salt_length=8),
        admin = admin,
        )
    db.session.add(user)
    db.session.commit()
    return user

