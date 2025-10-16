from Fakepinterest import database, app
from Fakepinterest.models import Usuario, Post

with app.app_context():
    database.create_all()