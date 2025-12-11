import requests

BASE_URL = "http://127.0.0.1:8000"


def test_api():
    print("Testing Book Collection API...")

    # Test 1: Create book
    print("\n1. Creating a book...")
    book_data = {"title": "Test Book", "author": "Test Author", "year": 2023}
    response = requests.post(f"{BASE_URL}/books/", json=book_data)
    print(f"   Status: {response.status_code}")
    if response.status_code == 200:
        book_id = response.json()["id"]
        print(f"   Created book ID: {book_id}")

    # Test 2: Get all books
    print("\n2. Getting all books...")
    response = requests.get(f"{BASE_URL}/books/")
    print(f"   Status: {response.status_code}")
    print(f"   Number of books: {len(response.json())}")

    # Test 3: Search books
    print("\n3. Searching books...")
    response = requests.get(f"{BASE_URL}/books/search/?author=Test")
    print(f"   Status: {response.status_code}")
    print(f"   Search results: {len(response.json())}")

    # Test 4: Delete book
    print("\n4. Deleting book...")
    response = requests.delete(f"{BASE_URL}/books/{book_id}")
    print(f"   Status: {response.status_code}")
    print(f"   Message: {response.json()}")

    print("\nAll tests completed!")


if __name__ == "__main__":
    test_api()
