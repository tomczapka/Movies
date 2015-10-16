#Class listing all properties to be defined for Movie object

class Movie():
    def __init__(self, movie_title, movie_story, poster_image,
               trailer_youtube):
        self.title = movie_title
        self.story = movie_story
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
