import sys

savedlist = 'Empty'


def search():
    import sys
    import requests

    global title

    search = input("(Type * to exit) Welcome to the movie database! Search for a movie: ")
    if search == "*":
        print("\nSee you next time!\n")
        sys.exit()

    api = 'https://api.themoviedb.org/3/search/movie?api_key=f06e670020e6ffd583c8c2ead08fa2da&query=' + search

    json = requests.get(api).json()

    fulldate = json['results'][0]['release_date']
    date = fulldate[0:4]
    r = "\n1. " + json['results'][0]['title'] + " (" + date + ")" + "\n" + json['results'][0]['overview']
    print(r)

    fulldate = json['results'][1]['release_date']
    date1 = fulldate[0:4]
    r1 = "\n2. " + json['results'][1]['title'] + " (" + date1 + ")" + "\n" + json['results'][1]['overview']
    print(r1)

    fulldate = json['results'][2]['release_date']
    date2 = fulldate[0:4]
    r2 = "\n3. " + json['results'][2]['title'] + " (" + date2 + ")" + "\n" + json['results'][2]['overview']
    print(r2)

    fulldate = json['results'][3]['release_date']
    date3 = fulldate[0:4]
    r3 = "\n4. " + json['results'][3]['title'] + " (" + date3 + ")" "\n" + json['results'][3]['overview']
    print(r3)

    choice = input("\n(Type * to exit) Type 1, 2, 3, or 4 for more information: ")
    if choice == "*":
        print("\nSee you next time!\n")
        sys.exit()

    if choice == '1':
        movie = 'http://www.omdbapi.com/?apikey=94e44bf0&t=' + json['results'][0]['title']
    elif choice == '2':
        movie = 'http://www.omdbapi.com/?apikey=94e44bf0&t=' + json['results'][1]['title']
    elif choice == '3':
        movie = 'http://www.omdbapi.com/?apikey=94e44bf0&t=' + json['results'][2]['title']
    elif choice == '4':
        movie = 'http://www.omdbapi.com/?apikey=94e44bf0&t=' + json['results'][3]['title']
    else:
        print("\nINVALID INPUT\n")
        sys.exit()

    json1 = requests.get(movie).json()

    title = "\n" + json1['Title']
    print(title)

    rating = "\n" + json1['Ratings'][0]['Source'] + " (" + json1['Ratings'][0]['Value'] + ")"
    print("\nRatings:", rating)

    released = "\n" + json1['Released']
    print("\nReleased:", released)

    genre = "\n" + json1['Genre']
    print("\nGenre:", genre)

    production = "\n" + json1['Production']
    print("\nProduction:", production)

    director = "\n" + json1['Director']
    print("\nDirector:", director)

    runtime = "\n" + json1['Runtime']
    print("\nRuntime:", runtime)

    plot = "\n" + json1['Plot']
    print("\nPlot: ", plot)

    actors = "\n" + json1['Actors']
    print("\nActors:", actors)

    rated = json1['Rated']
    print("\nRated", rated)

    boffice = "\n" + json1['BoxOffice']
    print("\nBox Office:", boffice)

    website = "\n" + json1['Website']
    print("\nWebsite:", website)

    awards = "\n" + json1['Awards']
    print("\nAwards:", awards)

    writer = "\n" + json1['Writer']
    print("\nWriter:", writer)

    language = "\n" + json1['Language']
    print("\nLanguage(s):", language, "\n")

    save()


def erase():
    global savedlist
    savedlist = "Empty"
    nxt()


def favlist():
    global savedlist
    print("\nFavourites:\n", savedlist, "\n")
    nxt()


def save():
    global savedlist

    save = input("(Type * to exit) Would you like to save this movie in favourites? (y/n)  ")

    if save == "*":
        print("\nSee you next time!\n")
        sys.exit()

    elif save == "y":
        savedlist = savedlist + title
        print("Saved to favourites!\n")

    elif save == "n":
        print(" ")

    else:
        print("INVALID INPUT")
        sys.exit()

    nxt()


def nxt():
    nxt = input(
        "(Type * to exit) What would you like to do next?\n - Type 'search' to search for another movie.\n - Type 'f'"
        " to access favourites list.\n - Type 'e' to erase favourites list.\n")

    if nxt == "*":
        print("\nSee you next time!\n")
        sys.exit()
    elif nxt == 'search':
        search()
    elif nxt == 'f':
        favlist()
    elif nxt == 'e':
        erase()
    else:
        print("INVALID INPUT")
        sys.exit()


search()
