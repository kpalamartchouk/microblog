from app import db

TABLE_ID = db.Sequence('table_id_seq',
                       metadata=db.metadata, 
                       start=1000)


class User(db.Model):
    __metadata__ = db.metadata

#    id = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.Integer,
                   #TABLE_ID,
                   primary_key=True,
                   server_default=TABLE_ID.next_value()
                   )

    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    another_field = db.Column(db.String)

    def __repr__(self):
        return '<User {}>'.format(self.username)
