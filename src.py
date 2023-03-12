from random import seed
from random import randint
from ursina import * 

app = Ursina()

seed(4)
obstacle_x = randint(0, 4)

def update():
    if held_keys["a"]:
        player.x -= 4 * time.dt
    elif held_keys["d"]:
        player.x += 4 * time.dt
    
    obstacle.y -= 3 * time.dt


class Player(Entity):
    def __init__(self):
        super().__init__(
            model = "quad",
            position = (0, -3),
            scale = .75
        )

class Obstacle(Entity):
    def __init__(self):
        super().__init__(
            model = "quad",
            position = (obstacle_x, 3),
            scale = .75
        )

player = Player()
obstacle = Obstacle()

app.run()