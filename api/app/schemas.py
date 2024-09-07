from dataclasses import dataclass

@dataclass
class Request:
    query: str


@dataclass
class Responce:
    text: str
