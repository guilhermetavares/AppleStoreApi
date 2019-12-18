from fastapi import FastAPI
from starlette.responses import JSONResponse

from schemas import Path
from import_data import HelperImportClass
from models import Application

app = FastAPI()


@app.get("/")
def api_version():
    return {
        "version": "v1.0.0",
        "docs": "To see the docs access the url /docs",
    }


@app.post("/load/")
def load_data(*, path: Path):

    helper = HelperImportClass(path.path)

    try:
        helper.process()
    except FileNotFoundError:
        return JSONResponse(status_code=500, content={'message': f'FileNotFoundError for {path.path}'})

    return {
        'message': f'File import correctly for {path.path}',
    }


@app.get("/genres/")
def get_prime_genre(prime_genre: str = None, limit: int = None):

    params = {}

    if prime_genre:
        params['prime_genre__in'] = prime_genre.split(',')

    applications = Application.objects(**params).order_by('-n_citacoes')

    if limit:
        applications = applications[:limit]

    return [application.json() for application in applications]
