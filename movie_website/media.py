import webbrowser
class Movie:
    ''' This class provides a way to store movie related informaton'''

    # Class variable
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    # Constructor
    def __init__(self, movie_title, movie_storyline, poster_image, trailer):
        # Instances variables
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_url = trailer

    # Instances methods
    def show_trailer(self):
        webbrowser.open(self.trailer_url)