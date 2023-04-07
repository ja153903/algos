from collections import defaultdict
from dataclasses import dataclass, field
from typing import Self


@dataclass
class TrieNode:
    is_word: bool = False
    children: defaultdict[str, Self] = field(default_factory=lambda: defaultdict(Self))

    def __contains__(self, key: str) -> bool:
        return key in self.children


class Trie:
    def __init__(self, words: list[str] | None = None) -> None:
        self._root = TrieNode()

        if words is not None:
            self._initialize_with(words)

    def _initialize_with(self, words: list[str]) -> None:
        for word in words:
            self._add_word(word)

    def _add_word(self, word: str) -> None:
        current = self._root

        for ch in word:
            if ch not in current:
                current.children[ch] = TrieNode()

            current = current.children[ch]

        current.is_word = True

    def search(self, word: str) -> bool:
        """
        Given some word, return whether that word is in the trie.
        """
        current = self._root

        for ch in word:
            if ch not in current:
                return False

            current = current.children[ch]

        return current.is_word

    def starts_with(self, prefix: str) -> bool:
        """
        Given some prefix string, return whether any string
        in the trie starts with that prefix.
        """
        current = self._root

        for ch in prefix:
            if ch not in current:
                return False

            current = current.children[ch]

        return True
