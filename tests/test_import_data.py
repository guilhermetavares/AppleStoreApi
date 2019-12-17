from app.import_data import HelperImportClass
from app.models import Application as MongoApplication


def test_import_data():
    assert len(MongoApplication.objects()) == 0

    helper = HelperImportClass('tests/BaseTests.csv')
    data_count, _ = helper.dataframe().shape
    assert data_count == 100

    helper.process()
    assert len(MongoApplication.objects()) == 100

    
