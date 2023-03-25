from dataclasses import dataclass
from typing import Self


@dataclass
class ListNode:
    val: int = 0
    next: Self | None = None
