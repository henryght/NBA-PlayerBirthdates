import basketball_reference_scraper
from basketball_reference_scraper.teams import get_roster
import pandas as pd
import xlrd
import re

# BR = basketball reference data
# EX = excel document data

# reads the excel file
df = pd.read_excel("NBAChampions.xlsx", sheet_name='ChampionshipList').to_dict() 

# looks for specific colummns within the excel file
year = df['Year']
team = df['Team']
date = df['Date']

# removes year from timestamp format
yearlessDates = re.compile(r'^.{5}(\d\d)-(\d\d)')

# finds matching month and day from yearlessDates
monthday = re.compile(r'\d\d')

# try and except due to years < 1958 have no team roster
try:

# finds the month and day of basketball players from the excel file and the date of the NBA championship
    for dates in year:
        print(str(year[dates]), str(team[dates]))
        roster = get_roster(team[dates], year[dates]).to_dict()
        player = roster['PLAYER']
        birthdate = roster['BIRTH_DATE']
        yearlessEX = yearlessDates.findall(str(date[dates]))
        monthdayEX = monthday.findall(str(yearlessEX))
        
# finds the month and day of basketball players from basketball reference
        for birthdays in birthdate:
            yearlessBR = yearlessDates.findall(str(birthdate[birthdays]))
            monthdayBR = monthday.findall(str(yearlessBR))

# compares the month and day of basketball players and the championship final date 
            if monthdayEX[0] == monthdayBR[0] and monthdayEX[1] == monthdayBR[1]:
                print(player[birthdays] + ' won a championship on their birthday')
            elif (int(monthdayEX[1])-1) <= int(monthdayBR[1]) <= (int(monthdayEX[1])) and monthdayEX[0] == monthdayBR[0]:
                print(player[birthdays] + ' was born a day early for a championship on their birthday')
            elif (int(monthdayEX[1])) <= int(monthdayBR[1]) <= (int(monthdayEX[1])+1) and monthdayEX[0] == monthdayBR[0]:
                print(player[birthdays] + ' was born a day late for a championship on their birthday')
except Exception:
    pass

