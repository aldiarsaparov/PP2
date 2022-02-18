movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Help", "imdb": 8.0, "category": "Drama"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
    {"name": "Colonia", "imdb": 7.4, "category": "Romance"},
    {"name": "Love", "imdb": 6.0, "category": "Romance"},
    {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
    {"name": "AlphaJet", "imdb": 3.2, "category": "War"},
    {"name": "Ringing Crime", "imdb": 4.0, "category": "Crime"},
    {"name": "Joking muck", "imdb": 7.2, "category": "Comedy"},
    {"name": "What is the name", "imdb": 9.2, "category": "Suspense"},
    {"name": "Detective", "imdb": 7.0, "category": "Suspense"},
    {"name": "Exam", "imdb": 4.2, "category": "Thriller"},
    {"name": "We Two", "imdb": 7.2, "category": "Romance"},
]


def task1(movies):
    lst = []

    for d in movies:
        if d["imdb"] > 5.5:
            lst.append(d["name"])

    print("\n".join(lst))


def task2(movies):
    for d in movies:
        if d["imdb"] > 5.5:
            print(d["name"], " => ", "True")
        else:
            print(d["name"], " => ", "False")


def task3(movies):
    c = input("Enter the category: ")
    lst = []

    for d in movies:
        if d["category"] == c:
            lst.append(d["name"])

    print(f"\nMovies with category {c}:")
    print("\n".join(lst))


def task4(movies):
    avg_imdb = 0

    for d in movies:
        avg_imdb += d["imdb"]

    print(f"AVERAGE IMDB SCORE = {avg_imdb / 14}")


def task5(movies):
    c = input("Enter the category to calculate AVG IMDB score: ")
    avg_imdb = 0
    cnt = 0

    for d in movies:
        if d["category"] == c:
            cnt += 1
            avg_imdb += d["imdb"]

    return f"Average IMDB score of movies of category {c} = {avg_imdb / cnt}"


# task1(movies)
# task2(movies)
# task3(movies)
# task4(movies)
# task5(movies)