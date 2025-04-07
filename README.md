# 🍽️ Menu Project (FastAPI + Unit Testing)

This is a modular, production-style backend API built with **FastAPI**, designed to manage a restaurant menu with full **CRUD functionality** and **unit tests**. It simulates a backend service for a VueJS frontend and emphasizes clean code organization, testing, and separation of concerns.

---

## 🧩 Features

- CRUD operations for menu items
- Pydantic v2 with separate schemas
- Mocked unit tests for isolated logic testing
- In-memory fake database (easy to replace with real DB later)
- Auto-generated Swagger docs

---

## 🛠 Tech Stack

- **FastAPI** - API development
- **Uvicorn** - ASGI server for FastAPI
- **Pydantic v2** - Data validation and modeling
- **Unittest + Mock** - Standard Python testing tools

---

## 📁 Project Structure

```
menu_project/
├── main.py                # FastAPI app and route handlers
├── database.py            # In-memory mock database
├── menu_model.py          # Pydantic model for menu item
├── schemas.py             # Separate request/response schemas
├── menu_crud.py           # Core business logic
├── test_menu.py           # Unit tests with mocking
└── README.md              # Project documentation
```

---

## 🔧 Installation

Ensure Python 3.11+ is installed, then run:

```bash
python -m pip install fastapi uvicorn requests
```

> 💡 Use a virtual environment (optional but recommended):

```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

---

## 🚀 Running the FastAPI App

To launch the API service:

```bash
uvicorn main:app --reload
```

API will be available at:

- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- OpenAPI schema: [http://127.0.0.1:8000/openapi.json](http://127.0.0.1:8000/openapi.json)

---

## 🧪 Running Unit Tests

Run all tests using:

```bash
python test_menu.py
```

Tests use `unittest.mock` to patch the business logic layer (`menu_crud.py`), ensuring fast and isolated testing.

---

## 📌 API Endpoints

| Method | Endpoint           | Description                   |
|--------|--------------------|-------------------------------|
| GET    | `/menu`            | Fetch all menu items          |
| POST   | `/menu`            | Add or update a menu item     |
| PUT    | `/menu/{item_id}`  | Update an item by ID          |
| DELETE | `/menu/{item_id}`  | Delete an item by ID          |

---

## 🔄 Example Menu Item JSON

```json
{
  "id": 1,
  "name": "Pizza",
  "price": 9.99,
  "description": "Cheesy and delicious"
}
```

---

## 🤝 Contributing

1. Fork this repo
2. Create a new branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m 'Add new feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

---

## 📃 License

This project is licensed under the **MIT License** — feel free to use, modify, and distribute.

---

## 🙌 Credits

Built by [Harris Sheikh](https://github.com/Harris143) for learning, scaling, and real-world backend architecture prototyping.
