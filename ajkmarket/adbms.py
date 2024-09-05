from ajkmarket import db, bcrypt

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    budget = db.Column(db.Integer, nullable=False, default=1000)
    items = db.relationship('Item', backref='owner', lazy=True)

    @property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)


class Item(db.Model):
    __tablename__ = 'aitems'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    color = db.Column(db.String(50), nullable=False)
    length = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))


def create_tables_and_insert_data():
    try:
        db.drop_all()  # Be careful with this if you have existing data
        db.create_all()

        # Check if the table already has entries
        if not Item.query.first():
            items = [
                Item(name='Loom-Asooke', color='Gold', length=90, price=30000),
                Item(name='Plain Cotton Asooke', color='blue', length=70, price=22000),
                Item(name='Mettalic Asooke', color='pink', length=90, price=19000),
                Item(name='Ojutonsoro', color='yellow', length=80, price=19000)
            ]
            db.session.bulk_save_objects(items)
            db.session.commit()
            print("Inserted initial data.")
        else:
            print("Data already exists. No new data inserted.")

    except Exception as e:
        db.session.rollback()
        print(f"An error occurred: {e}")
    finally:
        db.session.close()


if __name__ == "__main__":
    create_tables_and_insert_data()

