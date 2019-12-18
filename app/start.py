import sys
from import_data import HelperImportClass

path = sys.argv[1]
print(f'STARTING LOAD FILE {path}')
HelperImportClass(path).process()
print(f'FINISHED LOAD FILE {path}')
