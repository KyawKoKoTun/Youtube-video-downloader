import pytube


while True:
    url = input('video url: ')
    try:
        youtube = pytube.YouTube(url)
        while True:
            try:
                resolution = input('Enter resolution: ')
                video = youtube.streams.filter(res=resolution+'p').first()
                video.download('downloads/')
                print('Done!\n')
                break
            except:
                print('Resolution is not available, try another!')
    except:
        print('Invaild URL or No connection:(\n')
