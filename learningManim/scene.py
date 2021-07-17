from manim import *

class SquareToCircle(Scene):
    
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)
        
        square = Square()
        square.rotate(PI / 4)
        
        triangle2 = Triangle()
        triangle2.rotate(PI / 16)
        triangle2.shift(LEFT)

        triangle = Triangle()

        self.play(Create(square))
        
        for x in range(100):
            self.play(Create(triangle2))
            self.play(Transform(square, circle))
            self.play(Transform(circle, triangle))
            self.play(Transform(triangle, square))
            self.play(FadeOut(triangle))


