import requests

def search_books(keyword):

    url = (
        "https://www.googleapis.com/books/v1/volumes"
        f"?q={keyword}"
    )

    response = requests.get(url)

    return response.json()

def save_books(data, filename):

    with open(filename, "w") as file:

        for book in data.get("items", []):

            info = book["volumeInfo"]

            title = info.get("title", "Unknown")
            authors = info.get("authors", ["Unknown"])

            file.write(f"Title: {title}\n")
            file.write(f"Authors: {', '.join(authors)}\n")
            file.write("-" * 40 + "\n")