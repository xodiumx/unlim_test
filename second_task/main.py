import heroes
import villains
from random import choice


class Name(str): ...
class Gun(str): ...
class Info(str):...


class Сharacteristics:

    def __init__(self):
        self.guns = ['laser', 'ak-47', 'blaster', 'fireball', 'magic']

    def get_name(self) -> Name:
        raise NotImplementedError('Override the method')

    def get_random_gun(self):
        return choice(self.guns)


class Villain(Сharacteristics):

    def get_name(self) -> Name:
        """Get random villain name."""
        return villains.gen()


class SuperHero(Сharacteristics):

    def get_name(self) -> Name:
        """Get random villain name."""
        return heroes.gen()


class City:

    def __init__(self, cities: list[str]) -> None:
        self.cities_list = cities
        self.cities_info = {}
        self.villain = Villain()
        self.superhero = SuperHero()

    def set_info_about_heroes_and_villains(self) -> None:
        """Set information abot villains and superheroes"""
        for city in self.cities_list:
            self.cities_info[city] = {
                'villain': {
                    'name': self.villain.get_name(),
                    'gun': self.villain.get_random_gun()
                },
                'superhero': {
                    'name': self.superhero.get_name(),
                    'gun': self.superhero.get_random_gun()
                }
            }


class Media:

    def get_information(self, city_name: str):
        raise NotImplementedError('Override the method')


class TV(Media):

    def __init__(self, tv_name, cities):
        self.type = 'TV'
        self.tv_name = tv_name
        self.city = City(cities)
        self.city.set_info_about_heroes_and_villains()

    def get_information(self, city_name: str) -> str:
        villain = self.city.cities_info.get(city_name).get("villain")
        superhero = self.city.cities_info.get(city_name).get("superhero")
        return (
            f'{villain.get("name")} '
            f'stands near a skyscraper in {city_name} and attack with {villain.get("gun")}\n'
            f'After PIU PIU of {superhero.get("name")} with {superhero.get("gun")} city was saved\n'
            f'Watch today on {self.tv_name}'
        )


cities_list = ['Tokyo', 'NewYork', 'London', 'Paris', 'Moscow']
show_must_go_on = TV('Moscow News', cities_list)
print(show_must_go_on.get_information(choice(cities_list)))
