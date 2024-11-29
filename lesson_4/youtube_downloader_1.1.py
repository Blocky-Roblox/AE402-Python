from pytubefix import YouTube
import tkinter as tk
import threading

progress = 0
def showProgress(stream,chunk,bytes_remaining):

    size = stream.filesize
    
    global progress
    preProgress = progress
    
    currentProgress = (size - bytes_remaining)*100 // size
    progress = currentProgress
    
    if progress == 100:
        # scale.set(progress)
        # window.update()
        print("下載完成！")
        return
    
    if preProgress != progress:
        # scale.set(progress)
        # window.update()
        print("目前進度： " + str(progress) + "%")


window = tk.Tk()
window.title("YouTube下載器 1.1")
window.geometry("500x150")
window.resizable(False, False)

label = tk.Label(window, text="請輸入YouTube影片網址")
label.pack()

var = tk.StringVar()
entry = tk.Entry(window, width=50)
entry.pack()

def onClick():
    global var
    var.set(entry.get())
    button.config(state=tk.DISABLED)
    yt = YouTube(var.get(), on_progress_callback=showProgress)
    if onlyMusic.get():
        stream = yt.streams.filter(only_audio=True).first()
    else:
        stream = yt.streams.first()
    stream.download()
    button.config(state=tk.NORMAL)

def thread():
    threading.Thread(target=onClick).start()

onlyMusic = tk.BooleanVar()
check = tk.Checkbutton(window, text="只有音樂", variable=onlyMusic, onvalue=True, offvalue=False)
check.pack()

button = tk.Button(window, text="下載", command=thread)
button.pack()

# scale = tk.Scale(window, label="進度條", orient=tk.HORIZONTAL, length=200)
# scale.pack()

window.mainloop()