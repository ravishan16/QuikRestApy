from quikrestapy.models.usermodel import User
from quikrestapy.models import db

def create():
    db.create_all()
    admin = User('admin', 'admin@example.com')
    db.session.add(admin)
    admin = User('admin2', 'admin2@example.com')
    db.session.add(admin)
    db.session.commit()

if __name__ == "__main__":
    create()