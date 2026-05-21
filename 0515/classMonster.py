class Monster:
    WEAK = 0
    NORMAL = 10
    STRONG = 20
    VERY STRONG = 30

    def__init__(self):
       self._health = Monster.NORMAL
    
    def eat(self):
        self._health = Monster.STRONG

    def attack(self):
        self._health = Monster.WEAK