from collections import defaultdict
from dataclasses import dataclass, field
from typing import Self


@dataclass
class Trie:
    is_word: bool = False
    children: defaultdict[str, Self] = field(default_factory=lambda: defaultdict(Self))

    def __contains__(self, item: str) -> bool:
        return item in self.children


class WordDictionary:
    """
    This problem needs an augmented trie
    """

    def __init__(self):
        self._trie = Trie()

    def addWord(self, word: str) -> None:
        current = self._trie

        for char in word:
            if char not in current:
                current.children[char] = Trie()

            current = current.children[char]

        current.is_word = True

    def search(self, word: str) -> bool:
        return self._dfs(word, self._trie, 0)

    def _dfs(self, word: str, current: Trie, index: int) -> bool:
        for i in range(index, len(word)):
            char = word[i]

            match char:
                case ".":
                    for key, node in current.children.items():
                        if self._dfs(word, node, i + 1):
                            return True
                    return False
                case _:
                    if char not in current:
                        return False

                    current = current.children[char]

        return current.is_word
