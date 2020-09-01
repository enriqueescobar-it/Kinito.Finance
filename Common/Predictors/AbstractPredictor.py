from abc import ABC


class AbstractPredictor(ABC):
    __span: int
    __column: str
    __name: str
