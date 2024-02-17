import heroes
import villains
from random import choice


class Name(str): ...
class Gun(str): ...


class PersonСharacteristics:

    def __init__(self) -> None:
        self.guns = ['laser', 'ak-47', 'blaster', 'fireball', 'magic']

    def get_name(self) -> None:
        raise NotImplementedError('Override the method')

    def get_random_gun(self) -> Gun:
        return choice(self.guns)


class Villain(PersonСharacteristics):

    def get_name(self) -> Name:
        """Get random villain name."""
        return villains.gen()


class SuperHero(PersonСharacteristics):

    def get_name(self) -> Name:
        """Get random superhero name."""
        return heroes.gen()
