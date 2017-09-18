import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy7 and his toys that come to life",
                        "https://lumiere-a.akamaihd.net/v1/images/toy_story_that_time_forgot_keyart_300x450_fc2d5997.jpeg?region=0%2C0%2C300%2C450",
                        "https://www.youtube.com/watch?v=SgoiKLFBA3Q")
#print toy_story.storyline

#toy_story.show_trailer()

movies = [toy_story]
#fresh_tomatoes.open_movies_page(movies)

#print media.Movie.valid_ratings

print media.Movie.__doc__
