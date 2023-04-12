
from pytube import YouTube


print("Fça um download de um vídeo no youtube")

url = input("Digite o link: ")

video = YouTube(url)

#Mudar tipo de video
#streams = yt.streams.filter(file_extension='mp4') você pode mudar a extenção aqui

#Download de audio
#streams = video.streams.filter(only_audio=True)
#stream = streams.order_by('abr').last()

stream = video.streams.get_highest_resolution()
#video.streams.get_lowest_resolution()  resolução menor
#video.streams.get_highest_resolution() resolução maior
#video.streams.get_by_resolution() primeira resolução que aparecer


stream.download()
