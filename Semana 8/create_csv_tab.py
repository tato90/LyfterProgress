import csv

def ingress_videogames():
    my_games_tab = []

    while True: 
        name = input("Type the video game name or type 'end' to exit: ")
        if name == "end":
            break
        genre = input("Type the genre of the game: ")
        developer = input ("Type the developer of the game: ")
        classification = input ("Type the classification ESRB of the game: ")

        my_games_tab.append([name, genre, developer, classification])

    return my_games_tab

def save_to_csv(my_games_tab, filename):
    with open(filename, encoding="utf-8", mode='w', newline='') as file_csv:
        writer_csv = csv.writer(file_csv, delimiter='\t')
        writer_csv.writerow(['Name', 'Genre', 'Developer', 'Classification'])
        writer_csv.writerows(my_games_tab)

def print_csv(filename):
    with open(filename, mode='r', encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t')
        for row in csv_reader:
            print('\t'.join(row))  

def main():
    my_games_tab = ingress_videogames()
    if my_games_tab:
        filename = 'my_games.tsv'
        save_to_csv(my_games_tab, filename)
        print(f"The data has been saved to '{filename}'.")
        print("Content of the CSV file:")
        print_csv(filename)
    else:
        print("No video games were added.")

if __name__ == "__main__":
    main()