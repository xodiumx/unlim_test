from characters import Villain, SuperHero


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
