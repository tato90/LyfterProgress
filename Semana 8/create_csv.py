import csv

def ingress_videogames():
    my_games = []

    while True: 
        name = input("Type the video game name or type 'end' to exit: ")
        if name == "end":
            break
        genre = input("Type the genre of the game: ")
        developer = input ("Type the developer of the game: ")
        classification = input ("Type the classification ESRB of the game: ")


        my_games.append([name,genre,developer,classification])

    return my_games

def save_to_csv(my_games,filename):
    with open(filename,encoding="utf-8", mode='w', newline='') as file_csv:
        writer_csv = csv.writer(file_csv)
        writer_csv.writerow(['Name','Genre','Developer','Classification'])
        writer_csv.writerows(my_games)

def print_csv(filename):
    with open(filename,mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            print(', '.join(row))

def main():
    my_games = ingress_videogames()
    if my_games:
        filename = 'my_games.csv'  
        save_to_csv(my_games, filename)
        print(f"The data has been saved to '{filename}'.")
        print("Content of the CSV file:")
        print_csv(filename)
    else:
        print("No video games were added.")


if __name__ == "__main__":
    main()
