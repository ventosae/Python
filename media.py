import webbrowser

class Movie():
    """This calss gives you some movie infor"""
    VALID_RATINGS = ["G","R"]
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube,
            rotten_tomatos):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.rotten_tomatos_rating = rotten_tomatos
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
