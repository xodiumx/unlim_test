from dataclasses import dataclass
from datetime import datetime

from cities import CitiesInfo


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
