from tqdm import tqdm
import pandas as pd

from models import Application


class HelperImportClass(object):

    def __init__(self, path):
        self.path = path

    def dataframe(self):
        data = pd.read_csv(self.path, delimiter=',')
        dataframe = pd.DataFrame(data, columns=data.keys())
        return dataframe

    def create_application(self, row):
        Application(**{
            'apple_id': str(row['id']),
            'track_name': row['track_name'],
            'size_bytes': row['size_bytes'],
            'prime_genre': row['prime_genre'],
            'price': row['price'],
            'n_citacoes': row['rating_count_tot'],
        }).save()

    def process(self):
        data_csv = self.dataframe()

        # clear data
        Application.objects.delete()

        for index, row in tqdm(data_csv.iterrows()):
            self.create_application(row)

        return data_csv
