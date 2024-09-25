import requests


class Darth_Vader():
    """Класс включающий сценарии по отправке запроса по персонажу Дарт Вейдер, с целью получения персонажей, которые были в фильмах с Дарт Вейдером,
    а также сохраняет в текстовый файл список персонажей"""

    darth_url = "https://swapi.dev/api/people/4/"

    def write_characters_name_from_url(self,name):  # Функция для записи в файл персонажей
        with open('Characters', 'a', encoding="utf-8") as new_file:
            new_file.writelines(f"{name}\n")

    def get_films_url(self):   # Функция для получения url фильмов
        print(f"Ссылка на информацию о Дарт Вейдере {self.darth_url}")
        result = requests.get(self.darth_url)
        return result.json()["films"]

    def get_characters_from_film(self):   # Функция для получения персонажей
        films = self.get_films_url()
        print (f"Ссылки на информацию о фильмах с Дарт Вейдером {films}")
        for i in films:
            result = requests.get(i)
            characters_url = (result.json()["characters"])
            for j in characters_url:
                result2 = requests.get(j)
                character = result2.json()["name"]
                self.write_characters_name_from_url(character)
        print ("Список персонажей из каждого фильма с Дарт Вейдером записан в текстовый файл")

    def del_dublicate_in_file(self):  # Функция удаления дубликатов из файла
        with open('Characters', 'r', encoding='utf-8') as file:
            lines = file.readlines()
        unique_lines = list(dict.fromkeys(lines))
        with open('Characters', 'w', encoding='utf-8') as file:
            file.writelines(unique_lines)
        print ("Список персонажей очищен от дубликатов")

start = Darth_Vader()
start.get_characters_from_film()
start.del_dublicate_in_file()