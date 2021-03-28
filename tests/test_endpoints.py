url = "http://127.0.0.1:5000"

headers = {"Content-Type": "application/json"}


def test_register_product(client):
    data = {"id": 1, "name": "product", "price": 12.5}
    r = client.post(f"{url}/product", json=data, headers=headers)
    assert r.get_json() == {"message": "Success"}
    assert r.status_code == 201
