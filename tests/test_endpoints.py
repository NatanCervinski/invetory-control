import copy
from flask_jwt_extended import create_access_token

url = "http://127.0.0.1:5000"


def create_headers():
    token = create_access_token("test")
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",
    }
    return headers


class TestProduct:

    data = {"id": 1, "name": "product", "price": 12.5}

    def test_register_product_201(self, client):
        r = client.post(
            f"{url}/product",
            json=self.data,
            headers=create_headers(),
        )
        assert r.get_json() == {"message": "Success"}
        assert r.status_code == 201

    def test_register_product_409(self, client):
        r = client.post(
            f"{url}/product",
            json=self.data,
            headers=create_headers(),
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


class TestUser:
    data = {"user": "test", "name": "test", "password": "123"}

    def test_register_user_201(self, client):
        r = client.post(
            f"{url}/user_register",
            json=self.data,
            headers=create_headers(),
        )
        assert r.get_json() == {"message": "Success"}
        assert r.status_code == 201

    def test_register_user_409(self, client):
        r = client.post(
            f"{url}/user_register",
            json=self.data,
            headers=create_headers(),
        )
        assert r.get_json() == {"message": "User already exists"}
        assert r.status_code == 409

    def test_register_user_400(self, client):
        data_without_user = copy.deepcopy(self.data)
        data_without_user.pop("user")
        r = client.post(
            f"{url}/user_register",
            json=data_without_user,
            headers=create_headers(),
        )
        assert r.status_code == 400

    def test_login_200(self, client):
        login = {}
        login["user"], login["password"] = (
            self.data["user"],
            self.data["password"],
        )
        r = client.post(
            f"{url}/login", json=login, headers=create_headers()
        )
        assert r.status_code == 200
        assert "access_token" in r.get_json()

    def test_login_401(self, client):
        login = {"user": "a", "password": "123"}
        r = client.post(
            f"{url}/login", json=login, headers=create_headers()
        )
        assert r.status_code == 401
        assert r.get_json() == {"error": "User or password incorrect"}

    def test_login_401_2(self, client):
        login = {"user": "test", "password": "1234"}
        r = client.post(
            f"{url}/login", json=login, headers=create_headers()
        )
        assert r.status_code == 401
        assert r.get_json() == {"error": "User or password incorrect"}

    def test_login_400(self, client):
        login = {"use": "test", "password": "123"}
        r = client.post(
            f"{url}/login", json=login, headers=create_headers()
        )
        assert r.status_code == 400
