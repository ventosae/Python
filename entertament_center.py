import media
import fresh_tomatos

ip_man = media.Movie("Ip Man",
                     "During the Japanese invasion of 1937, when a wealthy martial artist is forced to leave his home and work to support his family, he reluctantly agrees to train others in the art of Wing Chun for self-defense.",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BNGZmYmQ2MTMtZTY2My00NmY2LTgwNDktNjRiZDBkOTdjNDEyL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyNDE3OTAyNDU@._V1_.jpg",
                     "https://www.youtube.com/watch?v=1AJxXQ7xojE",
                     "84%")
 
    
way_of_the_dragon = media.Movie("Way of the Dragon",
                     "A man visits his relatives at their restaurant in Italy and has to help them defend against brutal gangsters harassing them.",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BYTUyN2YyNTktYjJjZi00OWFkLTllZDAtZmRiNjY2ZWQxZWNkXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_SY1000_CR0,0,738,1000_AL_.jpg",
                     "https://www.youtube.com/watch?v=4lNDLaSWmhY",
                     "100%")

fearless = media.Movie("Fearless",
                     "Biography of Chinese Martial Arts Master Huo Yuanjia, who is the founder and spiritual guru of the Jin Wu Sports Federation.",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BZmIxOTg0NWUtYWI2NC00Y2Y3LTgyYzItOGUxNjE3ZTgwMGEyL2ltYWdlXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_SY1000_SX715_AL_.jpg",
                     "https://www.youtube.com/watch?v=42NWMluhlfk",
                     "73%")

 
 
movies = [ip_man, way_of_the_dragon, fearless]
print(media.Movie.__module__)
##fresh_tomatos.open_movies_page(movies)
