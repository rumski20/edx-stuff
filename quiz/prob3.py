# mid-term quiz | problem 3

def song_playlist(songs, max_size):
    """
    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit

    Start with the song first in the 'songs' list, then pick the next 
    song to be the one with the lowest file size not already picked, repeat

    Returns: a list of a subset of songs fitting in 'max_size' in the order 
             in which they were chosen.
    """

    # add first song to output list if it fits in output size
    if songs[0][2] > max_size:
        return []
    out_songs = [songs[0][0]]

    # running size total
    curr_size = songs[0][2]

    # sort remaining songs by song size
    # into a copy of the original song list
    key_func = lambda x: x[2]
    songs_copy = sorted(songs[1:], key=key_func)

    # loop through and add to output if there is space remaining
    for song in songs_copy:
        # check if next song will go over max size
        if (curr_size + song[2]) <= max_size:
            # add to output
            out_songs.append(song[0])
            # update current size of list
            curr_size += song[2]

    # return song list
    return out_songs

songs = [('Roar',4.4, 4.0),('Sail',3.5, 7.7),('Timber', 5.1, 6.9),('Wannabe',2.7, 1.2)]
print('song list:', song_playlist(songs, 3))