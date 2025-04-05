# 🍽️ Menu Project (FastAPI + Unit Testing)

This project is a backend API service built with **FastAPI** that handles CRUD operations on a restaurant menu. It is intended to serve as the backend for a frontend like VueJS. The project includes full unit testing using Python's `unittest` and `mock`.

---

## 📦 Tech Stack

- **FastAPI** - Web framework for APIs
- **Uvicorn** - ASGI server to serve the app
- **Pydantic v2** - For data models and validation
- **unittest + mock** - For unit testing

---

## 📁 Project Structure

```
menu_project/
├── main.py                # FastAPI app and route handlers
├── menu_model.py          # Pydantic model for MenuItem
├── menu_crud.py           # In-memory CRUD logic
├── test_menu.py           # Unit tests with unittest + mock
└── README.md              # You're reading this!
```

---

## 🔧 Requirements

You’ll need Python 3.11+ installed on your system.

Install dependencies using pip:

```bash
python -m pip install fastapi uvicorn requests
```

> 💡 Tip: Use a virtual environment to isolate dependencies:

```bash
python -m venv venv
venv\Scripts\activate  # For Windows
```

---

## 🚀 Running the FastAPI Server

Launch the server using Uvicorn:

```bash
uvicorn main:app --reload
```

Once it's running, open:

- Docs UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- OpenAPI schema: [http://127.0.0.1:8000/openapi.json](http://127.0.0.1:8000/openapi.json)

---

## 🧪 Running Unit Tests

Run this to execute all unit tests:

```bash
python test_menu.py
```

Each test mocks the underlying CRUD logic, so you don’t need a real database to run tests.

---

## 📌 API Endpoints

| Method | Endpoint           | Description                   |
|--------|--------------------|-------------------------------|
| GET    | `/menu`            | Fetch all menu items          |
| POST   | `/menu`            | Add or update a menu item     |
| PUT    | `/menu/{item_id}`  | Update an item by ID          |
| DELETE | `/menu/{item_id}`  | Delete an item by ID          |

---

## 🧾 Example Menu Item JSON

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

1. Fork the repo
2. Create a new branch (`git checkout -b feature/something`)
3. Commit your changes
4. Push to the branch
5. Open a pull request

---

## 📃 License

This project is licensed under the **MIT License** — use it freely for personal or commercial projects.

---

## 📍 Credits

Developed by [Harris Sheikh](https://github.com/Harris143) — built for learning and scaling backend services.
