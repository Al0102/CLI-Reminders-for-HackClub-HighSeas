

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
        self._pos = position
        self.previous_pos = position

    def __contains__(self, rect: "Rect"):
        if (self.pos.x + self.width > rect.pos.x and
            self.pos.x < rect.pos.x + rect.width and
            self.pos.y + self.height > rect.pos.y and
            self.pos.y < rect.pos.y + rect.height):
            return True
        return False
    
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

    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, new_position: Vector2):
        self.previous_pos = self.pos
        self._pos = new_position

    def center_pos(self):
        x = self.pos.x + round(self._width/2)
        y = self.pos.y + round(self._height/2)

        return (x,y)

    def render(self):
        rendered = f"\033[{self.previous_pos.y};{self.previous_pos.x}H"
        for i in range(self._height):
            rendered += ' '*self._width+f"\033[{self.previous_pos.y+i+1};{self.previous_pos.x}H"
        rendered += f"\033[{self.pos.y};{self.pos.x}H"
        for i in range(self._height):
            rendered += '#'*self._width+f"\033[{self.pos.y+i+1};{self.pos.x}H"
        return rendered


if __name__ == "__main__":
    import tGame
    import CONTROLS, KEY
    import os
    import threading
    import time

    tGame.init()
    tGame.screenClear()
    tGame.disableLineWrap()
    tGame.renderCopy()

    # Input
    Input = tGame.KeyboardInput()

    # Creation
    myrect = Rect(Vector2(5,10),Vector2(8,10))
    yourrect = Rect(Vector2(9,8),Vector2(10,10))

    # Threads
    def inputs():
        while Input.pressed != CONTROLS.ESCAPE:
            Input.keyIn()


    def main_loop():
        tGame.render("\033[=7l\033[?1049l")
        tGame.renderCopy()
        cooldown = 0
        while Input.keyIn() != CONTROLS.ESCAPE:
#            if not cooldown:
#                cooldown = 60
#            else:
#                cooldown -= 1
#                continue
            if not Input.pressed in (CONTROLS.UP,CONTROLS.DOWN,CONTROLS.LEFT,CONTROLS.RIGHT):
                continue
            match Input.pressed:
                #TODO
                # add setters for pos.x and pos.y 
                case CONTROLS.UP:
                    if myrect.pos.y > 1:
                        myrect.pos = Vector2(myrect.pos.x,myrect.pos.y-1)
                case CONTROLS.DOWN:
                    if myrect.pos.y + myrect.height-1 < os.get_terminal_size().lines:
                        myrect.pos = Vector2(myrect.pos.x,myrect.pos.y+1)
                case CONTROLS.RIGHT:
                    if myrect.pos.x + myrect.width-1 < os.get_terminal_size().columns:
                        myrect.pos = Vector2(myrect.pos.x+1,myrect.pos.y)
                case CONTROLS.LEFT:
                    if myrect.pos.x > 1:
                        myrect.pos = Vector2(myrect.pos.x-1,myrect.pos.y)
                case _:
                    pass

            # Display rects
            tGame.render("\033[32m")
            tGame.render(myrect.render())
            tGame.render("\033[31m")
            tGame.render(yourrect.render())
        
            # Reset colour 
            tGame.render("\033[0m")
        
            # Colliding test
            tGame.setCursor(100,100)
            tGame.render(myrect in yourrect)
            tGame.renderCopy()
    tGame.render("\033[?1049h")
    tGame.renderCopy()

    #loop_thread = threading.Thread(target=main_loop)
    #input_thread = threading.Thread(target=inputs)

    # Testing

    try:
        main_loop()
#        loop_thread.start()
#        input_thread.start()
#
#        loop_thread.join()
#        input_thread.join()

    # End
    finally:
        tGame.end()
    input()
