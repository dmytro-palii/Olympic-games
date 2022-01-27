# Написать проект, который спрашивает у пользователя данные о годе олимпиады и стране. Нужно вывести всех золотых медалистов за этот год у этой страны и их количество. В формате:
# 1. {Имя Фамилия} - {Дисциплина} - {Золото}

from data import olympic_games_data
from pprint import pprint

class OlympicGames:
    def __init__(self, olympic_games_data : list):
        self.olympic_games_data = olympic_games_data

    def get_country_lst(self):
        country_lst = []

        for sport_data in self.olympic_games_data:
            if sport_data["NOC"] not in country_lst:
                country_lst.append(sport_data["NOC"])

        return country_lst
        
    def check_year(self, input_year: int):
        if int(input_year) in range(1900, 2017):
            if int(input_year) % 2 == 0:
                return True
        
        print("Wrong year")
        return False

    def check_country(self, input_country: str):
        country_lst = self.get_country_lst()

        if input_country in country_lst:
            return True

        print("Wrong country")
        return False

    def check_medal(self, input_medal: str):
        medal_type_lst = ["Gold", "Silver", "Bronze"]
        if input_medal in medal_type_lst:
            return True
        
        print("Wrong medal type")
        return False

    def info_print(self, input_year: str, input_country: str,  input_medal_type: str):
        number = 1

        for sport_data in self.olympic_games_data:
            if input_year == sport_data["Year"]:
                if input_country == sport_data["NOC"]:
                    if input_medal_type == sport_data["Medal"]:
                        name = sport_data["Name"]
                        sport = sport_data["Sport"]
                        print(f"#{number}. {name} - {sport} - {input_medal_type}")
                        number += 1


    def request(self):

        input_year = input("Input year: ")
        input_country = input("Input country: ")
        input_medal_type = input("Input medal type: ")
        if self.check_year(input_year):
            if self.check_country(input_country):
                if self.check_medal(input_medal_type):
                    self.info_print(input_year, input_country, input_medal_type)

    def program_run(self):
        self.request()
        


olympic_games_list = OlympicGames(olympic_games_data)

olympic_games_list.program_run()


# {'ID': '809', 
# 'Name': 'Brian Adams', 
# 'Sex': 'M', 
# 'Age': '27', 
# 'Height': '183', 
# 'Weight': '67', 
# 'Team': 'Great Britain', 
# 'NOC': 'GBR', 
# 'Games': '1976 Summer', 
# 'Year': '1976', 
# 'Season': 'Summer', 
# 'City': 'Montreal', 
# 'Sport': 'Athletics', 
# 'Event': "Athletics Men's 20 kilometres Walk", 
# 'Medal': 'NA'} # "Gold", "Silver", "Bronze"