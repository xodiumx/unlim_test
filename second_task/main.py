import heroes
import villains
from random import choice
from dataclasses import dataclass
from datetime import datetime


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


class CitiesInfo:

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


@dataclass
class Message:
    type_show: str
    show_name: str
    city: str
    date: datetime
    villain: str
    villain_gun: str
    superhero: str
    superhero_gun: str

    def get_message(self):
        return (
            f'Today {self.date} - <{self.villain}>\n'
            f'Stands near a skyscraper in {self.city} and attack with {self.villain_gun}\n'
            f'After PIU PIU of <{self.superhero}> with {self.superhero_gun}, city was saved\n'
            f'Watch today on {self.type_show} - {self.show_name}'
        )


class Media:

    @staticmethod
    def get_date() -> datetime:
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def get_information(self, city_name: str) -> None:
        raise NotImplementedError('Override the method')


class TV(Media):

    def __init__(self, tv_name: str, cities_info: CitiesInfo) -> None:
        self.type = 'TV'
        self.show_name = tv_name
        self.city = cities_info

    def get_information(self, city_name: str) -> str:
        villain = self.city.cities_info.get(city_name).get('villain')
        superhero = self.city.cities_info.get(city_name).get('superhero')
        return Message(
            self.type,
            self.show_name,
            city_name,
            self.get_date(),
            villain.get('name'),
            villain.get('gun'),
            superhero.get('name'),
            superhero.get('gun')
        )
    

class Newspaper(Media):
    ...


cities_list = ['Tokyo', 'NewYork', 'London', 'Paris', 'Moscow']
cities = CitiesInfo(cities_list)
cities.set_info_about_heroes_and_villains()

show_must_go_on = TV(f'{choice(cities_list)} News', cities)
info = show_must_go_on.get_information(choice(cities_list))
print(info.get_message())
