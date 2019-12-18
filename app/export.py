import pandas as pd
import os
from models import Application

applications = Application.objects()
data = [application.json().values() for application in applications]
df = pd.DataFrame(data, columns = applications.first().json().keys() if applications else [])

dirpath = os.getcwd()
output_path = os.path.join(dirpath, 'application.csv')
df.to_csv(output_path)
