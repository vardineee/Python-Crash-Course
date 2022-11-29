def make_album(artist, title, song_number = None):
    album_dic = {
        'artis':artist.title(), 
        'title': title.title()}
    if song_number:
        album_dic['tracks'] = song_number
    return album_dic
        
title_prompt = "\nWhat album are you thinking of?"
artist_prompt = "Who's the artist? "

print("Enter 'quit' any time you want to stop")

while True:
    title = input(title_prompt)

    if title =='quit':
        break
    artist = input(artist_prompt)
    if artist == 'quit':
        break
    album = make_album(artist, title)
    print(album)
    


    


    