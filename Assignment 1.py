"""
This Program is for loading, adding and completing songs
Name: Fei Teng
Date: Dec 2nd,2018


"""

#CSV function#
import csv

list = []
csv_reader = csv.reader(open("song.csv"))
for row in csv_reader:
    list.append(row)


for index, element in enumerate(list):
    if element[3] =="y" :
       element[3] =="*"
    else:
        element[3] = ""

def main():
    print("Welcome to Songs to learn Ver 1.0 - Fei Teng ")
    menu = display_menu()
    print("Please enter your choice.")
    choice = input("Enter your choice"). upper()
    while choice != "Q" :
        if choice == "L":
            for i, item in enumerate(list):
                print("{:2}".format(i), "{:2}{:<30s}{:<20s}{:>20s}".format
                (item[3], item[0], item[1], item[2]))
            menu = display_menu()
            choice = input("Enter your choice:").upper()
        elif choice == "A":
            choice = added_song()
            menu = display_menu()
            choice = input("Enter your choice.").upper()
        elif choice == "C":
            choice = completed_song()
            menu = display_menu()
            choice = input("Enter your choice.").upper()
        else:
            print("Sorry, the choice you have entered is invalid, please enter a valid choice.")
            menu = display_menu()
            choice = input("Enter your choice.").upper()

        if choice == "Q":
            print("Songs updated to song.csv, have a nice day.")


#menu function#
def display_menu():
    print("Menu:")
    print("L","-","Songs listed")
    print("A","_","Add new song")
    print("C","_","Complete song")
    print("Q","_","Quit")


#add song function#
def added_song():

    added = []
    title = input("Please enter the title of the song, your input should not be blank:")

    while title == "":
        title = input("Your input should not be blank, please enter a valid title:")
    added.append(title)
    artist = input("Please enter the artist of the song:")
    while artist =="":
        artist = input("Your input should not be blank, please enter a valid artist:")
    added.append(artist)
    while True:
        try:
            year = int(input("Please enter the year:"))
        except ValueError:
            print("Sorry, the value you have entered is incorrect, please enter a valid number")
        else:
            break
    while year <= 0:
        print("The number you have entered should be no less than 0")
        year = input("Please enter the year:")
        added.append(year)
        require = "*"
        added.append(require)
        list.append(added)


# completed song function#
def completed_song():

    while True:
        try:
            completed = int(input("Please enter the number of the song to be marked as learned:"))
        except ValueError:
             print("Sorry, The number you have entered is invalid, please enter a valid number.")
        else:
                break
        while completed < 0:
            print("Entered number must >= 0")
            completed = int(input("Please enter the number of the song to be marked as learned:"))

        if list[completed][3] == " ":
            print("You have already learned {}".format(list[completed][0]))
        else:
            list[completed][3] == " "
            print("{} by {} learned".format(list[completed][0],list[completed][1]))

main()





