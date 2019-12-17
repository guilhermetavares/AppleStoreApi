from app.models import Application as MongoApplication


def test_application_create():
    tot_ = len(MongoApplication.objects())
    application = MongoApplication(**{
        'apple_id': '1',
        'prime_genre': 'News',
        'track_name': 'Track News',
        'size_bytes': 10000,
        'price': 100.0,
        'n_citacoes': 100,
    })
    application.save()
    assert MongoApplication.objects(**{'apple_id': '1'}).first().apple_id == application.apple_id
    assert len(MongoApplication.objects()) == tot_ + 1
