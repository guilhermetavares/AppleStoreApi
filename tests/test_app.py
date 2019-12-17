

def test_api_client(api_client):
    response = api_client.get("/")
    assert response.status_code == 200
    assert response.json()['version'] == 'v1.0.0'


def test_load_data(api_client):
    response = api_client.post("/load/", json={'path': 'url_to_csv.csv'})
    assert response.status_code == 500

    
