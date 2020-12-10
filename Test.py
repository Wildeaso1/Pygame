class Character :

    speed = 10
    lives = 5
    points = 0
    sprite = None
    weapon = None

    
    def Walk(self) :
        print('Character loopt met de snelheid', self.speed)

class Mario (Character) : 

    lives = 3
    weapon = "Hammer"
    
    #De constructor van Mario
    def __init__(self) :
        self.speed = 30

    def Jump(self) :
        print("Mario springt")

CharacterA = Character()
marioX = Mario()

CharacterA.Walk()
marioX.Walk()
marioX.Jump()

print(CharacterA.lives)
print(marioX.lives)

print(marioX)