import unittest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

class TestMenuIntegration(unittest.TestCase):

    def test_01_post_valid_menu_item(self):
        print("\n--- Test 01: POST /menu with valid data ---")
        item_data = {
            "id": 1,
            "name": "Pizza",
            "price": 9.99,
            "description": "Cheesy and delicious"
        }
        print("Sending:", item_data)
        response = client.post("/menu", json=item_data)
        print("Response:", response.status_code, response.json())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), item_data)

    def test_02_post_missing_name(self):
        print("\n--- Test 02: POST /menu with missing 'name' field ---")
        invalid_data = {
            "id": 2,
            "price": 5.00,
            "description": "Invalid menu entry"
        }
        print("Sending:", invalid_data)
        response = client.post("/menu", json=invalid_data)
        print("Response:", response.status_code, response.json())
        self.assertEqual(response.status_code, 400)
        self.assertIn("missing field", str(response.json()))

    def test_03_get_all_items(self):
        print("\n--- Test 03: GET /menu to retrieve all items ---")
        response = client.get("/menu")
        print("Response:", response.status_code, response.json())
        self.assertEqual(response.status_code, 200)
        self.assertIn("msg", response.json())
        self.assertEqual(response.json()["msg"], "Success")

    def test_04_get_item_by_id(self):
        print("\n--- Test 04: GET /menu/item by ID ---")
        response = client.get("/menu/item", params={"id": 1})
        print("Response:", response.status_code, response.json())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["name"], "Pizza")

    def test_05_get_item_by_name(self):
        print("\n--- Test 05: GET /menu/item by name ---")
        response = client.get("/menu/item", params={"name": "Pizza"})
        print("Response:", response.status_code, response.json())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["id"], 1)

    def test_06_get_item_bad_request(self):
        print("\n--- Test 06: GET /menu/item with no parameters ---")
        response = client.get("/menu/item")
        print("Response:", response.status_code, response.json())
        self.assertEqual(response.status_code, 400)

    def test_07_put_non_existing_item(self):
        print("\n--- Test 07: PUT /menu/999 for non-existing item ---")
        data = {
            "id": 999,
            "name": "Ghost Dish",
            "price": 0.0,
            "description": "Not on the menu"
        }
        print("Sending:", data)
        response = client.put("/menu/999", json=data)
        print("Response:", response.status_code, response.json())
        self.assertEqual(response.status_code, 404)
        self.assertIn("Failed to update", str(response.json()))

    def test_08_delete_existing_item(self):
        print("\n--- Test 08: DELETE /menu/1 to remove an item ---")
        response = client.delete("/menu/1")
        print("Response:", response.status_code, response.json())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"ok": True})

    def test_09_delete_non_existing_item(self):
        print("\n--- Test 09: DELETE /menu/999 for non-existing item ---")
        response = client.delete("/menu/999")
        print("Response:", response.status_code, response.json())
        self.assertEqual(response.status_code, 404)
        self.assertIn("Failed to delete", str(response.json()))

if __name__ == "__main__":
    print("========== Running FastAPI Integration Tests ==========")
    unittest.main()
