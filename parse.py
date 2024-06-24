from libpytunes import Library

library = Library('/Users/mgaydash/Documents/Development/iTunes Library XML Parse/iTunes Music Library.xml')

# for id, song in library.songs.items():
  # print(song.name, song.rating)

playlist_names = library.getPlaylistNames()

for playlist_name in playlist_names:
  print(playlist_name)
  playlist = library.getPlaylist(playlist_name)
  for track in playlist.tracks:
    print("    " + track.artist + " - " + track.name)