from typing import Tuple

def process_string(text: str) -> Tuple[str, int]:
    inverted_text = text[::-1]

    reference = {"a", "e", "i", "o", "u"}
    set_text = set(text.lower())
    vowels_present = set_text.intersection(reference)

    return inverted_text, len(vowels_present)


if __name__ == "__main__":

    test1 = process_string("sequoia")
    print(f"Palavra invertida: {test1[0]}")
    print(f"Contagem de vogais unícas: {test1[1]}")

    test2 = process_string("A Casa Amarela")
    print(f"Palavra invertida: {test2[0]}")
    print(f"Contagem de vogais unícas: {test2[1]}")   
