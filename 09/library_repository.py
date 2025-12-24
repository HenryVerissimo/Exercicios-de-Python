from typing import List, Dict
from library_organizer import LibraryOrganizer

class LibraryRepository:
    def __init__(self, library: LibraryOrganizer) -> None:
        self._library = library

    def select_all_books(self) -> List[Dict[str, str]]:
        return self._library.organized_books

    def select_books_by_category(self, category: str) -> List[Dict[str, str]]:
        selected_books = []

        for book in self._library.organized_books:
            if category.lower() in book["categoria"].lower():
                self._organize_book_by_age(selected_books, book)

        return selected_books
    
    def select_books_by_author(self, author: str) -> List[Dict[str, str]]:
        selected_books = []

        for book in self._library.organized_books:
            if author.lower() in book["autor"].lower():
                self._organize_book_by_age(selected_books, book)

        return selected_books
    
    def _organize_book_by_age(self, selected_books: List[Dict[str, str]], book: Dict[str, str]) -> None:
        if not selected_books:
            selected_books.append(book)
            return

        for index, selected_book in enumerate(selected_books):
            if book["ano"] > selected_book["ano"]:
                selected_books.insert(index, book)
                return

            elif index == len(selected_books) -1:
                selected_books.append(book)
                return