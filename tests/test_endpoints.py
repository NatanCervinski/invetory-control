url = "http://127.0.0.1:5000"

headers = {"Content-Type": "application/json"}


class TestProduct:
    data = {"id": 1, "name": "product", "price": 12.5}

    def test_register_product(self, client):
        r = client.post(
            f"{url}/product", json=self.data, headers=headers
        )
        assert r.get_json() == {"message": "Success"}
        assert r.status_code == 201

    def test_product_get(self, client):
        r = client.get(f"{url}/product/{self.data['id']}")
        assert r.get_json() == self.data
        assert r.status_code == 200
