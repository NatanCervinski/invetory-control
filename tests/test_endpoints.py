url = "http://127.0.0.1:5000"

headers = {"Content-Type": "application/json"}


class TestProduct:
    data = {"id": 1, "name": "product", "price": 12.5}

    def test_register_product_201(self, client):
        r = client.post(
            f"{url}/product", json=self.data, headers=headers
        )
        assert r.get_json() == {"message": "Success"}
        assert r.status_code == 201

    def test_register_product_409(self, client):
        r = client.post(
            f"{url}/product", json=self.data, headers=headers
        )
        assert r.get_json() == {"message": "Id already exists"}
        assert r.status_code == 409

    def test_product_get_200(self, client):
        r = client.get(f"{url}/product/{self.data['id']}")
        assert r.get_json() == self.data
        assert r.status_code == 200

    def test_product_get_404(self, client):
        r = client.get(f"{url}/product/{self.data['id']*4555}")
        assert r.get_json() == {"message": "Product not found"}
        assert r.status_code == 404
