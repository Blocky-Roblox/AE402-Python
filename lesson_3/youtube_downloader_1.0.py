from pytubefix import YouTube
import tkinter as tk

window = tk.Tk()
window.title("YouTube下載器 1.0")
window.geometry("500x150")
window.resizable(False, False)

label = tk.Label(window, text="請輸入YouTube影片網址")
label.pack()

var = tk.StringVar()
entry = tk.Entry(window, width=50)
entry.pack()

progress = 0
def showProgress(stream,chunk,bytes_remaining):

    size = stream.filesize
    
    global progress
    preProgress = progress
    
    currentProgress = (size - bytes_remaining)*100 // size
    progress = currentProgress
    
    if progress == 100:
        scale.set(progress)
        window.update()
        print("下載完成！")
        return
    
    if preProgress != progress:
        scale.set(progress)
        window.update()
        print("目前進度： " + str(progress) + "%")

def onClick():
    global var
    var.set(entry.get())
    yt = YouTube(var.get(), on_progress_callback=showProgress)
    stream = yt.streams.first()
    stream.download()

button = tk.Button(window, text="下載", command=onClick)
button.pack()

scale = tk.Scale(window, label="進度條", orient=tk.HORIZONTAL, length=200)
scale.pack()

window.mainloop()