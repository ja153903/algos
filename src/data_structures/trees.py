from dataclasses import dataclass
from typing import Self


@dataclass
class TreeNode:
    val: int = 0
    left: Self | None = None
    right: Self | None = None
