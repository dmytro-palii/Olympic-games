# Написать проект, который спрашивает у пользователя данные о годе олимпиады и стране. Нужно вывести всех золотых медалистов за этот год у этой страны и их количество. В формате:
# 1. {Имя Фамилия} - {Дисциплина} - {Золото}

# Написать проект, который спрашивает у пользователя данные о годе олимпиады. Нужно вывести на экран информацию о количестве золотых медалистов за этот год у каждой страны и их количество:
# 1. {Страна} - {Количество золотых медалей}

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

    def part2_info_input(self):
        gold_medals_countries = {}
        gold_medal_count = 0
        input_year = input("Input year: ")
        if self.check_year(input_year):
            country_lst = self.get_country_lst()
            for olympic_info in self.olympic_games_data:
                if olympic_info["Medal"] == "Gold":
                    country = olympic_info["NOC"]
                    year = olympic_info["Year"]
                    for some_country in country_lst:
                        if country == some_country and input_year == year:
                            if country not in gold_medals_countries:
                                gold_medals_countries[country] = {"Gold" : 0}

                            gold_medals_countries[country]["Gold"] += 1
        
        for country, medals in gold_medals_countries.items():
            gold_num = medals["Gold"]
            print(f"# {country} - {gold_num}")
 
# {Страна1 : {"Gold" : количество золотых}, 
#  Страна2 : {"Gold" : количество золотых},
# ....
# }


                
# {Страна1 : {"Bronze" : количество бронзовых, "Bronze" : количество серебрянных, "Gold" : количество золотых}, 
#  Страна2 : {"Bronze" : количество бронзовых, "Bronze" : количество серебрянных, "Gold" : количество золотых},
# ....
# }


            
# 1. {Страна} - {Количество золотых медалей}

    def part1_info_input(self):

        input_year = input("Input year: ")
        input_country = input("Input country: ")
        input_medal_type = input("Input medal type: ")
        if self.check_year(input_year):
            if self.check_country(input_country):
                if self.check_medal(input_medal_type):
                    self.info_print(input_year, input_country, input_medal_type)

    def program_run(self):
        choice = int(input("What part of the project do you want to check? (1/2): "))
        if choice == 1:
            self.part1_info_input()
        else:
            self.part2_info_input()
        


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