import unittest
from unittest.mock import patch
from fastapi.testclient import TestClient
from main import app
from schemas import MenuItemCreate
from menu_model import MenuItem

client = TestClient(app)

class TestMenuAPI(unittest.TestCase):

    @patch("menu_crud.get_all_items")
    def test_get_menu(self, mock_get):
        print("\nRunning test: GET /menu")
        mock_get.return_value = [
            MenuItem(id=1, name="Burger", price=5.99),
            MenuItem(id=2, name="Fries", price=2.99)
        ]

        response = client.get("/menu")
        print("\nResponse Status:", response.status_code)
        print("\nResponse JSON:", response.json())

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)

    @patch("menu_crud.insert_or_update")
    def test_post_menu(self, mock_post):
        print("\nRunning test: POST /menu")
        item = MenuItem(id=1, name="Pizza", price=9.99)
        mock_post.return_value = item

        response = client.post("/menu", json=item.model_dump())
        print("\nRequest Body:", item.model_dump())
        print("\nResponse Status:", response.status_code)
        print("\nResponse JSON:", response.json())

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), item.model_dump())

    @patch("menu_crud.update_item")
    def test_put_existing_item(self, mock_put):
        print("\nRunning test: PUT /menu/1 (existing item)")
        item = MenuItem(id=1, name="Updated Pizza", price=11.99)
        mock_put.return_value = item

        response = client.put("/menu/1", json=item.model_dump())
        print("\nRequest Body:", item.model_dump())
        print("\nResponse Status:", response.status_code)
        print("\nResponse JSON:", response.json())

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["name"], "Updated Pizza")

    @patch("menu_crud.update_item")
    def test_put_nonexistent_item(self, mock_put):
        print("\nRunning test: PUT /menu/99 (nonexistent item)")
        mock_put.return_value = None
        item = MenuItem(id=99, name="Ghost", price=0.0)

        response = client.put("/menu/99", json=item.model_dump())
        print("\nRequest Body:", item.model_dump())
        print("\nResponse Status:", response.status_code)
        print("\nResponse JSON:", response.json())

        self.assertEqual(response.status_code, 404)

    @patch("menu_crud.delete_item")
    def test_delete_existing_item(self, mock_delete):
        print("\nRunning test: DELETE /menu/1 (existing item)")
        mock_delete.return_value = True

        response = client.delete("/menu/1")
        print("\nResponse Status:", response.status_code)
        print("\nResponse JSON:", response.json())

        self.assertEqual(response.status_code, 200)

    @patch("menu_crud.delete_item")
    def test_delete_nonexistent_item(self, mock_delete):
        print("\nRunning test: DELETE /menu/999 (nonexistent item)")
        mock_delete.return_value = False

        response = client.delete("/menu/999")
        print("\nResponse Status:", response.status_code)
        print("\nResponse JSON:", response.json())

        self.assertEqual(response.status_code, 404)

if __name__ == "__main__":
    print("\n==== Starting Menu API Unit Tests ====\n\n")
    unittest.main()
