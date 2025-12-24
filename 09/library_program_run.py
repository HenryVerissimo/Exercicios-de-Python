import os
import subprocess
from time import sleep  

from library_organizer import LibraryOrganizer
from library_repository import LibraryRepository

def library_program_run(library: LibraryOrganizer, repository: LibraryRepository) -> None:
    while True:
        subprocess.run(["bash", "user_interface.sh"])

        if not os.path.exists("./user_interface_option.txt"):
            print("Erro: Arquivo 'user_interface_option.txt' não encontrado! Verifique a path e o arquivo 'user_interface.sh'.")
            break

        with open("user_interface_option.txt", "r") as file:
            option: int = int(file.readline())
        
        os.remove("./user_interface_option.txt")
        
        subprocess.run("clear")

        match option:
            case 1:  
                response = repository.select_all_books()
                print("Todos os livros cadastrados:\n")

                counter = 1
                for book in response:
                    print(f"{counter}. {book["título"]} - {book["autor"]} - {book["ano"]} - {book["categoria"]}")
                    counter += 1

                input("\n(Digite ENTER para sair)")

            case 2:
                category = input("Digite uma categoria: ")
                response = repository.select_books_by_category(category)

                if not response:
                    subprocess.run("clear")
                    print(f'Nenhum livro com a categoria "{category}" foi encontrado no sistema.')
                    sleep(2)
                    continue
                
                counter = 1
                for book in response:
                    print(f"{counter}. {book["título"]} - {book["autor"]} - {book["ano"]} - {book["categoria"]}")
                    counter += 1

                input("\n(Digite ENTER para sair)")

            case 3:
                author = input("Digite um autor: ")
                response = repository.select_books_by_author(author)

                if not response:
                    subprocess.run("clear")
                    print(f'Nenhum livro escrito pelo autor "{author}" foi encontrado no sistema.')
                    sleep(2)
                    continue

                counter = 1
                for book in response:
                    print(f"{counter}. {book["título"]} - {book["autor"]} - {book["ano"]} - {book["categoria"]}")
                    counter += 1

                input("\n(Digite ENTER para sair)")

            case 4:
                print("Relatório estatístico:\n")
                print(f"Média de idade dos livros: {library.average_books_age} anos")
                print(f"A categoria com mais livros é '{library.category_with_the_most_books[0]}' com: {library.category_with_the_most_books[1]} livro(s)")

                input("\n(Digite ENTER para sair)")

            case 5:
                break
    
    subprocess.run("clear")
    print("Programa finalizado :)")
    sleep(2)
    subprocess.run("clear")