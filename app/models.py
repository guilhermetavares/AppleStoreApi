import mongoengine
import os

MONGO_HOST = os.environ.get('MONGO_HOST', None)
MONGO_USER = os.environ.get('MONGO_USER', None)
MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD', None)
MONGO_DATABASE = os.environ.get('MONGO_DATABASE', None)


mongoengine.connect(
    db=MONGO_DATABASE,
    username=MONGO_USER,
    password=MONGO_PASSWORD,
    host='{}?authSource=admin'.format(MONGO_HOST),
)


class Application(mongoengine.Document):
    apple_id = mongoengine.StringField(unique=True)
    prime_genre = mongoengine.StringField()
    track_name = mongoengine.StringField()
    size_bytes = mongoengine.LongField()
    price = mongoengine.FloatField()
    n_citacoes = mongoengine.IntField()
