from pytubefix import YouTube

def showProgress(stream, chunk, bytes_remaining):
    size = stream.filesize
    currentProgress = (size - bytes_remaining) * 100 // size
    print("progress:", str(currentProgress), "%")

yt = YouTube("https://www.youtube.com/watch?v=btPv0-d3NbE", on_progress_callback=showProgress)
stream = yt.streams.first()
stream.download("")