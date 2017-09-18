class Movie():
    '''
    This class is for Moive class. To show this, do media.Movie.__doc__
    '''
    valid_ratings = ['G', 'PG-13'] #class variable
    def __init__(self, title, storyline, poster_image, trailer_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_url

    def show_trailer(self):
        import webbrowser
        webbrowser.open(self.trailer_youtube_url)
        
