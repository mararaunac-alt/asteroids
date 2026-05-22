import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
      

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # create two smaller asteroids
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        new_1 = self.velocity.rotate(angle)
        new_2 = self.velocity.rotate(-angle)
        smaller_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_1 = Asteroid(self.position.x, self.position.y, smaller_radius)
        asteroid_2 = Asteroid(self.position.x, self.position.y, smaller_radius)
        asteroid_1.velocity = new_1 * 1.2
        asteroid_2.velocity = new_2 * 1.2


