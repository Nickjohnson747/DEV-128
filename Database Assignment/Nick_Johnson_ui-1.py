"""
Assignment: Database
Class: DEV 128
Date: 03/01/2024
Author: Nick Johnson
Description: Program to view movies from a SQL table
"""
import Nick_Johnson_db
from objects import Movie


def display_welcome():
    print("The Movie List program")
    print()
    display_menu()


def display_menu():
    print("COMMAND MENU")
    print("cat  - View movies by category")
    print("year - View movies by year")
    print("add  - Add a movie")
    print("del  - Delete a movie")
    print("min - View movies by minutes")
    print("exit - Exit program")
    print()


def display_categories():
    print("CATEGORIES")
    categories = Nick_Johnson_db.get_categories()
    for category in categories:
        print(str(category.id) + ". " + category.name)
    print()


def display_movies_by_category():
    category_id = int(input("Category ID: "))
    print()
    category = Nick_Johnson_db.get_category(category_id)
    movies = Nick_Johnson_db.get_movies_by_category(category_id)
    display_movies(movies, category.name.upper())


def display_movies(movies, title_term):
    print("MOVIES - " + title_term)
    line_format = "{:3s} {:37s} {:6s} {:5s} {:10s}"
    print(line_format.format("ID", "Name", "Year", "Mins", "Category"))
    print("-" * 64)
    for movie in movies:
        print(
            line_format.format(
                str(movie.id),
                movie.name,
                str(movie.year),
                str(movie.minutes),
                movie.category.name,
            )
        )
    print()


def display_movies_by_year():
    year = int(input("Year: "))
    print()
    movies = Nick_Johnson_db.get_movies_by_year(year)
    display_movies(movies, str(year))


def display_movies_by_minutes():
    minutes = int(input("Minutes: "))
    print()
    movies = Nick_Johnson_db.get_movies_by_minutes(minutes)
    display_movies(movies, "LESS THAN " + str(minutes) + " MINUTES")


def add_movie():
    name = input("Name: ")
    year = int(input("Year: "))
    minutes = int(input("Minutes: "))
    category_id = int(input("Category ID: "))

    category = Nick_Johnson_db.get_category(category_id)
    movie = Movie(name=name, year=year, minutes=minutes, category=category)
    Nick_Johnson_db.add_movie(movie)
    print(name + " was added to database.\n")


def delete_movie():
    movie_id = int(input("Movie ID: "))
    movie_name = Nick_Johnson_db.get_movie(movie_id).name
    del_conf = input("Are you sure you want to delete '" + movie_name + "'? (y/n)")
    if del_conf == "y":
        Nick_Johnson_db.delete_movie(movie_id)
        print("{} was deleted from database.\n".format(movie_name))
    else:  # very simple catching
        print("Movie was not deleted")


def main():
    Nick_Johnson_db.connect()
    display_welcome()
    display_categories()
    while True:
        command = input("Command: ")
        if command == "cat":
            display_movies_by_category()
        elif command == "year":
            display_movies_by_year()
        elif command == "min":
            display_movies_by_minutes()
        elif command == "add":
            add_movie()
        elif command == "del":
            delete_movie()
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
            display_menu()
    Nick_Johnson_db.close()
    print("Bye!")


if __name__ == "__main__":
    main()
