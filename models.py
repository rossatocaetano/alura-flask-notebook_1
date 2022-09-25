from app import db


class Foods(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    food = db.Column(db.String(50), nullable=False)
    expiration = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name


class Users(db.Model):
    nickname = db.Column(db.String(8), primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name