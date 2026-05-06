# Description: Working with lists
# Author: Jonathan Loepz

movies = ["The Matrix", "Inception", "Interstellar", "The Dark Knight", "Pulp Fiction"]

print(f"The list of movies inclues my top {len(movies)} favorite movies:")
print(movies)

print(sorted(movies))
print(movies)

movies.sort()
print(movies)

movies.append("The Lord of the Rings")
print(movies)