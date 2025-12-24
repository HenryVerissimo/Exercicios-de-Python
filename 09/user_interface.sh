#! usr/bin/env bash

while true; do
    clear
    
    echo -e "Escolha uma das opções a baixo:\n"
    echo "1 - Listar todos os livros"
    echo "2 - Listar livros por categoria"
    echo "3 - Listar livros por autor"
    echo "4 - Relatório estatístico"
    echo -e "5 - sair\n"

    read -p "Digite um número 1-5: " option

    [[ ($option < 1) || ($option > 5) ]] && clear && echo -n "Valor digitado é inválido! Digite um número entre 1-5. " && sleep 2 && continue

    echo $option > user_interface_option.txt
    exit 0

done