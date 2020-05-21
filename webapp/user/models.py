from flask_login import UserMixin  # provides is_authenticated, is_active, is_anonymous, get_id methods
from werkzeug.security import generate_password_hash, check_password_hash

from webapp.db import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(57), index=True, unique=True)
    password = db.Column(db.String(130))
    role = db.Column(db.String(12), index=True)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @property  # this decorator allows to call method as an attribute, without brackets ()
    def is_admin(self):
        return self.role == 'admin'

    def __repr__(self):
        return '<User {} {}>'.format(self.username, self.role)