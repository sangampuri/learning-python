# for loop in lists in Python allows you to iterate over the elements of a list and perform operations on each element. Here's an example of how to use a for loop to iterate through a list:

players = ["Messi", "Ronaldo", "Neymar", "Mbappe", "Lewandowski","Raphinha","Lamine Yamal","Kylian Mbappe","Erling Haaland","Robert Lewandowski"]

for player in enumerate(players):
    print(player)


for index, player in enumerate(players,1):
    print(f"Player {index }: {player}")