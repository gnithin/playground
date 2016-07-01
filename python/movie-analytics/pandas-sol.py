import pandas as pd
# import numpy as np

# Not needed now atleast
# import matplotlib.pyplot as plt

# All constants
FILE_DIR = "movie-data/"


class Movie:
    def __init__(self):
        self.movies_data = None
        self.ratings_data = None
        self._pivot_table = None

    def fetch_data(self,
                   file_name,
                   sep="::",
                   header=None,
                   col_names=[],
                   set_index=None,
                   invalidate_cache=False
                   ):
        data = None
        # search if the pickled version is available
        if not invalidate_cache:
            pkl_file_name = file_name + ".pkl"
            try:
                data = pd.read_pickle(pkl_file_name)
                print "Successfully fetched!! " + pkl_file_name
            except IOError as ioe:
                print "ioe error"
                print ioe.message
                pass
            except Exception as e:
                print "exceptino"
                print e.message
                pass

        if data is not None or not len(data):
            data = pd.read_table(
                file_name,
                sep=sep,
                header=header,
                names=col_names,
                engine='python'
            )
            if set_index:
                data = data.set_index(set_index)
            data.to_pickle(pkl_file_name)
        return data

    def fetch_movies_data(self,
                          file_name,
                          sep='::',
                          header=None,
                          col_names=None,
                          set_index=None,
                          invalidate_cache=False,
                          print_info=False):
        self.movies_data = self.fetch_data(
            file_name,
            sep=sep,
            header=header,
            col_names=col_names,
            set_index=set_index,
            invalidate_cache=invalidate_cache
        )

        if print_info and self.movies_data is not None:
            print self.movies_data.info()

        return self.movies_data is not None

    def fetch_ratings_data(self,
                           file_name,
                           sep='::',
                           header=None,
                           col_names=None,
                           invalidate_cache=False,
                           print_info=False):
        self.ratings_data = self.fetch_data(
            file_name,
            sep=sep,
            header=header,
            col_names=col_names,
            invalidate_cache=invalidate_cache
        )

        if print_info and self.ratings_data is not None:
            print self.ratings_data.info()

        return self.ratings_data is not None

    def process_movies(self,
                       invalidate_cache=False
                       ):
        # create the pivot table
        self._pivot_table = pd.pivot_table(
            self.ratings_data,
            columns=['user_id'],
            index=['movie_id'],
            values=['rating'],
            fill_value=0.0
        )


if __name__ == "__main__":
    # Just writing down the sequence of things that need to be done
    movie_obj = Movie()

    movie_obj.fetch_movies_data(
        FILE_DIR + "movies.dat",
        print_info=True,
        col_names=['movie_id', 'title', 'genres'],
    )

    movie_obj.fetch_ratings_data(
        FILE_DIR + "ratings.dat",
        print_info=True,
        col_names=['user_id', 'movie_id', 'rating', 'timestamp']
    )

    movie_obj.process_movies()
