
current_movies = {'Sinners' : '11:00am', 
                  'Final Destinattion' : '12:00pm',
                  'Lilo & Stitch' : '1:00pm', 'Thunderbolts' : '2:00pm'}

print("We're showing the following movies:")
for key in current_movies:
    print(key)

movie = input ('What movie would you like the showtime for?\n')

showtime = current_movies.get(movie)

if showtime == None:
    print("Requested movie isn't playing")
else:
    print(movie,  'is playing at', showtime)