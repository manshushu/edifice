from math import hypot


class Vector:
    def __init__(self,x,y) -> None:
        self.x=x
        self.y=y

    def __repr__(self) -> str:
        return