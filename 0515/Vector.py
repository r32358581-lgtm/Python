class Vector2D
    def__init___(self, x, y):
       self.x = x
       self.y = y
    
    def__add__(self, other):
       return Vector2D(self.x + other.x, self,y + other.y)

    def__sub__(self, other):
       return Vector2D(self.x - other.x, self.y - other.y)

    def__eq__(self, other):
       return self.x == other.x and self.y == other.y

    def__str__(self):
        return '(%g, %g)'% (self.x, self.y)

u = Vector2D(0,1)
v = VEctor2D(1,0)