from random import choice

from cities import CitiesInfo
from news import TV


def main():
    cities_list = ['Tokyo', 'NewYork', 'London', 'Paris', 'Moscow']
    cities = CitiesInfo(cities_list)
    cities.set_info_about_heroes_and_villains()

    show_must_go_on = TV(f'{choice(cities_list)} News', cities)
    info = show_must_go_on.get_information(choice(cities_list))
    print(info.get_message())


if __name__ == '__main__':
    main()
