from typing import List
from typing import Union
from typing import Any

binary_type: Any
binary_type = bytes


def indent(text: str, prefix: str = ...) -> str:
    ...


def codeblock(text: str) -> str:
    ...


def paragraph(text: str) -> str:
    ...


def hzcat(args: List[str], sep: str = ...):
    ...


def ensure_unicode(text: Union[str, bytes]):
    ...
