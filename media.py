# 5/27/15     Michael Cleeton     cleeton.m@gmail.com
# Generated from Udacity's Programming Fundamentals
# with Python Course and modified by me

# imports built-in python library webbrowser
import webbrowser


class Movie():

    """ This class provides a way to store movie related infomation."""

    def __init__(self, movie_title, movie_rating, movie_info_page,
                 movie_storyline, poster_image, trailer_youtube):
        """Properties:
        title: Title of movie
        rating: The MPAA movie rating (eg: R, PG-13, PG ...)
        info_page: Url to IMDB page
        storyline: Short plot synopsis
        poster_image: Url to movie poster
        trailer_youtube_url: Url to youtube trailer
        """
        self.title = movie_title
        self.rating = movie_rating
        self.info_page = movie_info_page
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Provides class Movie with a function to open
        a web browser window and show its trailer.
        """
        webbrowser.open(self.trailer_youtube_url)
