import unittest
from unittest.mock import patch
from fastapi.testclient import TestClient
from main import app
from menu_model import MenuItem

client = TestClient(app)

class TestMenuAPI(unittest.TestCase):

    @patch("menu_crud.get_menu_items")
    def test_get_menu(self, mock_get):
        mock_items = [
            MenuItem(id=1, name="Burger", price=5.99),
            MenuItem(id=2, name="Fries", price=2.99)
        ]
        mock_get.return_value = mock_items

        print("Testing GET /menu")
        response = client.get("/menu")
        print("Response JSON:", response.json())

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)

    @patch("menu_crud.add_or_update_menu_item")
    def test_post_menu(self, mock_post):
        item = MenuItem(id=1, name="Pizza", price=9.99)
        mock_post.return_value = item

        print("Testing POST /menu with:", item)
        response = client.post("/menu", json=item.model_dump())
        print("Response JSON:", response.json())

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), item.model_dump())

    @patch("menu_crud.update_menu_item")
    def test_put_menu_success(self, mock_put):
        item = MenuItem(id=1, name="Pasta", price=7.49)
        mock_put.return_value = item

        print("Testing PUT /menu/1 with:", item)
        response = client.put("/menu/1", json=item.model_dump())
        print("Response JSON:", response.json())

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), item.model_dump())

    @patch("menu_crud.update_menu_item")
    def test_put_menu_not_found(self, mock_put):
        mock_put.return_value = None
        item = MenuItem(id=99, name="Ghost", price=0.0)

        print("Testing PUT /menu/99 with item that doesn't exist")
        response = client.put("/menu/99", json=item.model_dump())
        print("Response status:", response.status_code)

        self.assertEqual(response.status_code, 404)

    @patch("menu_crud.delete_menu_item")
    def test_delete_menu_success(self, mock_delete):
        mock_delete.return_value = True

        print("Testing DELETE /menu/1 (should succeed)")
        response = client.delete("/menu/1")
        print("Response JSON:", response.json())

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"ok": True})

    @patch("menu_crud.delete_menu_item")
    def test_delete_menu_not_found(self, mock_delete):
        mock_delete.return_value = False

        print("Testing DELETE /menu/99 (should fail)")
        response = client.delete("/menu/99")
        print("Response status:", response.status_code)

        self.assertEqual(response.status_code, 404)

if __name__ == "__main__":
    unittest.main()
