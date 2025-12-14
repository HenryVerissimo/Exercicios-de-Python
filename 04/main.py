from typing import List, Dict, Tuple

class CountAnagramsByGroup:
    def __init__(self) -> None:
        self._group_of_words: Dict[str, List[str]] = {}
        self._number_groups: int = 0
        self._largest_number_of_words: int = 0

    def organize__group_of_words(self, words_list: List[str]) -> Tuple[Dict[str, List[str]], int, int]:
        for word in words_list:
            key = "".join(sorted(word.lower()))
            self._group_of_words.setdefault(key, []).append(word)
        
        self._number_groups = len(self._group_of_words)
        self._set__largest_number_of_words_in_a_group()

        return self._group_of_words, self._number_groups, self._largest_number_of_words

    def _set__largest_number_of_words_in_a_group(self) -> None:
        self._largest_number_of_words = max((len(group) for group in self._group_of_words.values()), default=0)

if __name__ == "__main__":

    list_words = ["eat", "tea", "tan", "ate", "nat", "bat", "AET", "cat"]
    test_class = CountAnagramsByGroup()
    result = test_class.organize__group_of_words(list_words)

    print(f"Grupos de palavras: {result[0]}")

    print(f"Número de grupos: {result[1]}")

    print(f"Maior número de palavras em um grupo: {result[2]}")