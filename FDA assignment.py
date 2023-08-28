import pandas as pd
import matplotlib.pyplot as plt

movies = pd.read_csv("imdb_top_1000.csv")

pd.set_option('display.max_columns', None)  # Display all columns
pd.set_option('display.max_rows', None)  # Display all rows

# Columns to be removed
unwanted_columns = ['Poster_Link', 'Series_Title', 'Released_Year', 'Certificate', 'Runtime', 'Overview', 'Director',
                    'Star2', 'Star3', 'Star4', 'Gross']

# Drop the unwanted columns
movies.drop(unwanted_columns, axis=1, inplace=True)

print(movies.head())

different_genres = set()
for row in movies["Genre"]:
    genres_of_movies = row.split(", ")
    different_genres.update(genres_of_movies)

print(different_genres)

for genre in different_genres:
    movies[genre] = movies["Genre"].str.contains(genre,case=False).astype(int)

print(movies.head())

genre_counts = {}
for genre in different_genres:
    count = (movies[genre] == 1).sum()
    genre_counts[genre] = count

print(genre_counts)
print( "OOOOOOOK")

# Calculate pure drama movies
not_related_to_pure_drama_genres = ["Comedy", "Family", "Musical", "Animation", "Adventure", "Western", "Sci-Fi"]

movies["Pure_Drama"] = (movies["Drama"] == 1) & (~movies[not_related_to_pure_drama_genres].any(axis=1))

drama_movies = movies[movies["Pure_Drama"] == True]
print(drama_movies)
print("The number of pure drama movies is:" , len(drama_movies))

# Calculate pure comedies
not_related_to_pure_comedy_genres = ['History', 'Romance', 'Crime', 'Horror', 'Musical', 'War', 'Thriller', 'Drama',
                                     'Film-Noir']
movies["Pure_Comedy"] = (movies["Comedy"] == 1) & (~movies[not_related_to_pure_comedy_genres].any(axis=1))
comedy_movies = movies[movies["Pure_Comedy"] == True]
print("The number of pure comedy movies is:" , len(comedy_movies))

# Calculate pure adventure
not_related_to_pure_adventure_genres = ['Romance', 'Musical', 'Drama', 'Film-Noir', 'Family', 'Music', 'Sport']
movies["Pure_Adventure"] = (movies["Adventure"] == 1) & (~movies[not_related_to_pure_adventure_genres].any(axis=1))
adventure_movies = movies[movies["Pure_Adventure"] == True]
print("The number of pure adventure movies is:" , len(adventure_movies))

# Calculate pure romance
not_related_to_pure_romance_genres = ['Film-Noir', 'Family', 'Music', 'Fantasy', 'War', 'History', 'Horror', 'Crime',
                                      'Sci-Fi', 'Biography', 'Mystery', 'Thriller', 'Action']
movies["Pure_Romance"] = (movies["Romance"] == 1) & (~movies[not_related_to_pure_romance_genres].any(axis=1))
romance_movies = movies[movies["Pure_Romance"] == True]
print("The number of pure romance movies is:" , len(romance_movies))


#Calculate pure thrillers
not_related_to_pure_thriller_genres = ['Romance', 'Musical', 'Family', 'Music', 'Sport', 'Biography', 'History', 'Western']
movies["Pure_Thriller"] = (movies["Thriller"] == 1) & (~movies[not_related_to_pure_thriller_genres].any(axis=1))
thriller_movies = movies[movies["Pure_Thriller"] == True]
print("The number of pure thriller movies is:" , len(thriller_movies))