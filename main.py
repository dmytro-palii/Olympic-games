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
        
    

    def request(self):
        country_lst = self.get_country_lst()
        medal_type_lst = ["Gold", "Silver", "Bronze"]
        number = 1

        input_year = input("Input year: ")
        if int(input_year) in range(1900, 2017):
            if int(input_year) % 2 == 0:

                input_country = input("Input country: ")
                if input_country in country_lst:
                    input_medal_status = input("Input medal type: ")

                for sport_data in self.olympic_games_data:
                    year = sport_data["Year"]
                    country = sport_data["NOC"]
                    if input_year == year and input_country == country:
                        if sport_data['Medal'] in medal_type_lst:
                            if input_medal_status == sport_data['Medal']:
                                name = sport_data["Name"]
                                sprot = sport_data["Sport"]
                
                                print(f"{number}. {name} - {sprot} - {input_medal_status}")
                                number += 1

        


olympic_games_list = OlympicGames(olympic_games_data)

olympic_games_list.request()


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