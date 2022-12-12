import pandas as pd
import matplotlib.pyplot as plt

#Import the data
df = pd.read_csv("fifa_data.csv", delimiter=",")


########################################################################################################################
#Preferred Foot
########################################################################################################################

#Create 2 sorted dataframes with preferred foot
right = df.loc[df["preferred_foot"] == "Right"]
left = df.loc[df["preferred_foot"] == "Left"]

#Get the length of the dataframes
right_foot_count = len(right.index)
left_foot_count = len(left.index)

#Labels for the pie chart
labels = ["Right Foot", "Left Foot"]

#Set plot style
plt.style.use("ggplot")

#Create figure
plt.figure()

#Create pie chart
plt.pie([right_foot_count, left_foot_count], labels=labels, autopct="%1.2f%%")
plt.title("Comparison preferred foot")


########################################################################################################################
#Best fieldplayer as a goalkeeper
########################################################################################################################

#Define the dataframe with all players exclude the goalkeepers
fieldplayer = df.loc[df["player_positions"] != "GK"]
#Sum all goalkeeping ratings in a new column
fieldplayer["gk_ges"] = fieldplayer["goalkeeping_diving"] + fieldplayer["goalkeeping_handling"] + \
                        fieldplayer["goalkeeping_kicking"] + fieldplayer["goalkeeping_positioning"] + \
                        fieldplayer["goalkeeping_reflexes"]

#Define the highst gk-rating and get the player with these stats
highest_gk_rating = fieldplayer["gk_ges"].max()
best_gk = fieldplayer.loc[fieldplayer["gk_ges"] == highest_gk_rating]

#Define the variables for the output string
players_name = best_gk["long_name"].to_string().strip("4593 ")
players_height = best_gk["height_cm"].to_string().strip("4593 ")
players_club = best_gk["club_name"].to_string().strip("4593 ")
players_league = best_gk["league_name"].to_string().strip("4593 ")

#Output
print("The best fieldplayer as a goalkeeper is " + players_name + ". He is " + players_height +
      " cm tall and plays for " + players_club + " in the " + players_league + ".")


########################################################################################################################
#Player with the highest potential
########################################################################################################################

#Add a new column with the difference of the potential an overall rating to get the maximum possible potential
df["potential_dif"] = df["potential"] - df["overall"]
#Define the highest potential difference and get the player with these value
highest_dif = df["potential_dif"].max()
high_potential_player = df.loc[df["potential_dif"] == highest_dif]

#Define Variables for the output string
p_name = high_potential_player["long_name"].to_string(index=False)
p_age = high_potential_player["age"].to_string(index=False)
p_club = high_potential_player["club_name"].to_string(index=False)
p_league = high_potential_player["league_name"].to_string(index=False)
p_potential = high_potential_player["potential"].to_string(index=False)
p_rating = high_potential_player["overall"].to_string(index=False)

print("The player with the highest potential is " + p_name + ". He is " + p_age + " years old and plays for " + p_club +
      " in the " + p_league + ". His potential is " + p_potential + " with a rating of " + p_rating + ".")


########################################################################################################################
#Barchart of the average rating ot the goalkeepers in relation to the height
########################################################################################################################

#Create a Dataframe with all goalkeepers
goalkeepers = df.loc[df["player_positions"] == "GK"]

#Create classes by body height
#Until 170cm
gk170 = df.loc[df["height_cm"] < 170]
rating_170 = gk170["overall"].mean()

#Between 170cm and 180cm
gk180 = df.loc[(df["height_cm"] >= 170) & (df["height_cm"] < 180)]
rating_180 = gk180["overall"].mean()

#Between 180cm and 190cm
gk190 = df.loc[(df["height_cm"] >= 180) & (df["height_cm"] < 190)]
rating_190 = gk190["overall"].mean()

#Between 190cm and 200cm
gk200 = df.loc[(df["height_cm"] >= 190) & (df["height_cm"] <= 200)]
rating_200 = gk200["overall"].mean()

#Over 200cm
gk201 = df.loc[df["height_cm"] > 200]
rating_201 = gk201["overall"].mean()

#Define the values in a list to use them in the plot
y_values = [rating_170, rating_180, rating_190, rating_200, rating_201]
x_values = ["< 170cm", "170 - 179 cm", "180 - 189cm", "190 - 200cm", "> 200cm"]

#Create the bar plot
plt.figure()
plt.bar(x_values, y_values)
plt.xlabel("Body height")
plt.ylabel("Average overall rating")
plt.title("Comparison average gk rating in relation to body height")


########################################################################################################################
#How many players of the game play in the top 5 european leagues?
########################################################################################################################

#Create different dataframes sorted by top 5 european leaues and the rest of the world
spanish_players = df.loc[df["league_name"] == "Spain Primera Division"]
german_players = df.loc[df["league_name"] == "German 1. Bundesliga"]
french_players = df.loc[df["league_name"] == "French Ligue 1"]
english_players = df.loc[df["league_name"] == "English Premier League"]
italian_players = df.loc[df["league_name"] == "Italian Serie A"]
rest_of_players = df.loc[(df["league_name"] != "Spain Primera Division") &
                         (df["league_name"] != "German Bundesliga 1") & (df["league_name"] != "French Ligue 1") &
                         (df["league_name"] != "English Premier League") &
                         (df["league_name"] != "Italian Serie A")]

#Get the amount of players in each dataframe
num_spanish_players = len(spanish_players.index)
num_german_players = len(german_players.index)
num_french_players = len(french_players.index)
num_english_players = len(english_players.index)
num_italian_players = len(italian_players.index)
num_rest_of_players = len(rest_of_players.index)

#Set the labels for the pie chart
league_labels = ["La Liga", "Bundesliga", "Ligue 1", "Prem. League", "Serie A", "Rest of Game"]
#Set the explode values to separate the main data a little bit for a better look
explode = (0.2, 0.2, 0.2, 0.2, 0.2, 0)

#Create the figure and the plot
plt.figure()
plt.pie([num_spanish_players, num_german_players, num_french_players, num_english_players, num_italian_players,
         num_rest_of_players],explode=explode, labels=league_labels, autopct="%1.1f%%")
plt.title("How many of the players play in the 5 top european leagues?")


########################################################################################################################
#Frequency distribution of the body height
########################################################################################################################

#Create a dataframe with all body heights
body_heights = df["height_cm"]

#Create a figure and a histgram with the body height of the players
plt.figure()
plt.hist(body_heights)
plt.title("Frequency distribution of the body height")
plt.ylabel("Amount of players")
plt.xlabel("Body height in cm")
#Change the values/lables of the scale
plt.xticks([160, 165, 170, 175, 180, 185, 190, 195, 200])


########################################################################################################################
#Fastest Team in Game by average player pace
########################################################################################################################

#Grouping the data by the clubname and get the mean pace of each club
average_pace = df.groupby("club_name")["pace"].mean().sort_values(ascending=False)
#Transform the series into a dataframe for better working
pace_df = average_pace.to_frame()

#Output
print("The Club with the fastest average pace is " + pace_df.iloc[0].name + " with a value of " +
      str(pace_df.iloc[0][0]) + ".")



########################################################################################################################
#League with the most skills
########################################################################################################################

#Create a Dataframe with all 4*/5* skill players
skill_player = df.loc[df["skill_moves"] >= 4]

#Grouping the players by league name and get the amount of skill players of each league
average_skills = skill_player.groupby("league_name")["skill_moves"].count()
#Slicing the data to the top 5
sorted_result = average_skills.sort_values(ascending=False).head()
#Transform the series into a dataframe for better working
sorted_df = sorted_result.to_frame()

#Define variables with the values for the plot
value_spain = sorted_df.iloc[0][0]
value_england = sorted_df.iloc[1][0]
value_italia = sorted_df.iloc[2][0]
value_france = sorted_df.iloc[3][0]
value_turkish = sorted_df.iloc[4][0]

#Create a list the the labels for the plot
skill_labels = [sorted_df.iloc[0].name, sorted_df.iloc[1].name,  sorted_df.iloc[2].name, sorted_df.iloc[3].name,
                sorted_df.iloc[4].name]

#Create the figure and the bar plot
plt.figure(figsize=(10,5))
plt.bar(skill_labels, [value_spain, value_england, value_italia, value_france, value_turkish])
plt.title("Top 5 most 4*/5* skill player per league")
plt.xlabel("Leagues")
plt.ylabel("Amount of players")

#Show the plots *Output*
plt.show()