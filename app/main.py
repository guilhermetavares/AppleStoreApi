from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def api_version():
    return {
        "version": "v1.0.0",
        "docs": "To see the docs access the url /docs",
    }
