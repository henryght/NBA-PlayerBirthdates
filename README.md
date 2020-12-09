# NBA-PlayerBirthdates
This python program looks through NBA final end dates and the winning roster player's birthday. It compares the month and date to see if a player has won an NBA championship on their birthday.

Used this scraper tool to look through basketball references : 
https://github.com/vishaalagartha/basketball_reference_scraper/blob/master/API.md

One thing to note, in order to get the program to work, I had to go into 

\Lib\site-packages\basketball_reference_scraper\teams 

and delete the line 

:df['NATIONALITY'] = df['NATIONALITY'].apply(lambda x: x.upper())
