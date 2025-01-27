from functools import singledispatchmethod

class Vector2:
    def __init__(self, x: int=None, y: int=None, vector: ("Vector2", tuple)=None):
        if vector and (isinstance(vector, Vector2) or len(vector)==2):
            self.x = vector[0]
            self.y = vector[1]
        elif isinstance(x, int) and isinstance(y, int):
            self.x = x
            self.y = y
        else:
            raise ValueError("Pass in x=(int) and y=(int), or vector=(Vector2) or (tuple: length=2)")

    def __getitem__(self, index: int):
        if not isinstance(index, int):
            raise ValueError(f"Expected integer: found {type(index)} ({index})")
        elif not (0 <= index <= 1):
            raise IndexError(f"Expected 0 or 1: found {index}")

        return self.x if index == 0 else self.y
    
    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, vector2: "Vector2"):
        return Vector2(self.x+vector2.x, self.y+vector2.y)


class Rect:
    def __init__(self, size: Vector2, position: Vector2):

        self._size = Vector2(vector=size)
        self._width = self.size[0]
        self._height = self.size[1]

        # Top left
        self.pos = position
    
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, new_size: Vector2):
        self._size = new_size
        self._width = new_size[0]
        self._height = new_size[1]

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, new_width: int):
        self._width = new_width
        self.size[0] = new_width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, new_height: int):
        self._height = new_height
        self.size[1] = new_height

    def center_pos(self):
        x = self.pos.x + round(self._width/2)
        y = self.pos.y + round(self._height/2)

        return (x,y)

    def render(self):
        rendered = f"\033[{self.pos.y};{self.pos.x}H"
        for i in range(self._height):
            rendered += '#'*self._width+f"\033[{self.pos.y+i+1};{self.pos.x}H"
        return rendered


if __name__ == "__main__":
    import tGame
    tGame.init()
    tGame.screenClear()
    tGame.renderCopy()

    input (Vector2(9,8)+Vector2(9,8))

    myrect = Rect(Vector2(1,1),Vector2(10,10))
    yourrect = Rect(Vector2(9,8),Vector2(40,20))

    tGame.setCursor(*myrect.pos)
    tGame.render(myrect.render())
    tGame.renderCopy()
    input()

    tGame.screenClear()
    myrect.size = myrect.size + yourrect.size

    tGame.setCursor(*myrect.pos)
    tGame.render(myrect.render())
    tGame.renderCopy()

    tGame.setCursor(position=myrect.center_pos())
    tGame.renderCopy()
    input()
