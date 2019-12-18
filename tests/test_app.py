

def test_api_client(api_client):
    response = api_client.get("/")
    assert response.status_code == 200
    assert response.json()['version'] == 'v1.0.0'


def test_load_data(api_client):
    response = api_client.post("/load/", json={'path': 'url_to_csv.csv'})
    assert response.status_code == 500

    response = api_client.post("/load/", json={'path': 'https://raw.githubusercontent.com/guilhermetavares/AppleStoreApi/b8260db765ceb8e083881989caa71be9154472f6/tests/BaseTests.csv'})
    assert response.status_code == 200


def test_api_genre(api_client):
    response = api_client.get("/genres/?prime_genre=Games,Games2&limit=1")
    response.json()[0]['prime_genre'] == 'Games'
    response.json()[0]['n_citacoes'] == 508808
