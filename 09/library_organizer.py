from typing import Dict, List, Tuple
from datetime import datetime
from collections import Counter

class LibraryOrganizer:
    def __init__(self) -> None:
        self.organized_books: List[Dict[str, str]] = []
        self.average_books_age: int = 0
        self.category_with_the_most_books: Tuple[str, int] =  ("", 0)

        self._some_books_age: int = 0
        self._valid_books_data: int = 0

    def process_data_set(self, dataset: List[str]) -> None:
        for data_string in dataset:
            self._organize_data(data_string)

        if self._valid_books_data > 0:
            self._set_average_books_age()
            self._find_category_with_the_most_books()
    
    def _organize_data(self, data_string: str) -> None:
        organized_data = {}
        data_list = data_string.split("|")

        data_keys = ["título", "autor", "ano", "categoria"]
        
        for index, value in enumerate(data_list):
            organized_data[data_keys[index]] = value.lower().strip()
        
        self._capture_book_age(organized_data)

        if self._valid_book_year(organized_data):
            print(f'Erro: O ano de lançamento do livro "{organized_data["título"]}" ({organized_data["ano"]}) é maior que o ano atual ({datetime.now().year})!')
            print(f'O cadastro do livro "{organized_data['título']}" foi considerado um erro. Cadastro rejeitado!')
            return
        
        self.organized_books.append(organized_data)
        self._valid_books_data += 1

    def _capture_book_age(self, organized_data: Dict[str, str]) -> None:
        actual_year = datetime.now().year
        book_age = actual_year - int(organized_data["ano"])
        self._some_books_age += book_age

    def _valid_book_year(self, organized_data: Dict[str, str]) -> bool:
        return int(organized_data["ano"]) > datetime.now().year
    
    def _find_category_with_the_most_books(self) -> None:
        filtered_categories = [book["categoria"] for book in self.organized_books]

        couter_categories = Counter(filtered_categories)

        info_common_category = couter_categories.most_common(1)[0]
        self.category_with_the_most_books = info_common_category

    def _set_average_books_age(self) -> None:
        self.average_books_age = int(self._some_books_age / self._valid_books_data)


