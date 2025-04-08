import unittest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

class TestMenuIntegration(unittest.TestCase):

    def test_01_post_menu_item(self):
        print("===> Testing POST /menu (create new item)")
        item_data = {
            "id": 1,
            "name": "IntCheese Pizza",
            "price": 9.99,
            "description": "Cheesy and delicious"
        }

        response = client.post("/menu", json=item_data)
        print("Status:", response.status_code)
        print("Response:", response.json())

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), item_data)

    def test_02_get_menu(self):
        print("===> Testing GET /menu")
        response = client.get("/menu")
        print("Status:", response.status_code)
        print("Response:", response.json())

        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.json()), 1)

    def test_03_put_existing_item(self):
        print("===> Testing PUT /menu/1 (update item)")
        updated_item = {
            "id": 1,
            "name": "Updated Pizza",
            "price": 11.99,
            "description": "With extra toppings"
        }

        response = client.put("/menu/1", json=updated_item)
        print("Status:", response.status_code)
        print("Response:", response.json())

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["name"], "Updated Pizza")

    def test_04_put_nonexistent_item(self):
        print("===> Testing PUT /menu/999 (nonexistent item)")
        updated_item = {
            "id": 999,
            "name": "Ghost Dish",
            "price": 0.0,
            "description": "Invisible on the menu"
        }

        response = client.put("/menu/999", json=updated_item)
        print("Status:", response.status_code)
        print("Response:", response.json())

        self.assertEqual(response.status_code, 404)

    def test_05_delete_existing_item(self):
        print("===> Testing DELETE /menu/1")
        response = client.delete("/menu/1")
        print("Status:", response.status_code)
        print("Response:", response.json())

        self.assertEqual(response.status_code, 200)

    def test_06_delete_nonexistent_item(self):
        print("===> Testing DELETE /menu/999")
        response = client.delete("/menu/999")
        print("Status:", response.status_code)
        print("Response:", response.json())

        self.assertEqual(response.status_code, 404)

if __name__ == "__main__":
    print("==== Running Integration Tests on FastAPI ====")
    unittest.main()
