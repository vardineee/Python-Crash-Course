def make_album(artist, title, song_number = None):
     if song_number:
           album = {'name': artist.title(), 'title': title.title(), 'song_number': song_number}
     else:
         
       album = {'name': artist.title(), 'title': title.title()}

     return album

artist_album = make_album('shakira', 'loca', 8)
print(artist_album)

artist_album = make_album('beethoven', 'ninth symphony')
print(artist_album)    


    


    