import tkinter as tk
from datetime import datetime
import time
from PIL import Image, ImageTk
import numpy as np
from screeninfo import get_monitors

def set_popout(monitor_index, target):
    if monitor_index < len(monitors):
        monitor = monitors[monitor_index]
        target.geometry(f"{monitor.width}x{monitor.height}+{monitor.x}+{monitor.y}")
        target.attributes("-fullscreen", True)
    else:
        print(f"Monitor index {monitor_index} is out of range. Using primary monitor instead.")
        target.attributes("-fullscreen", True)    

def animate_gif(label, frames, delay, frame_index=0):
    frame = frames[frame_index]
    label.configure(image=frame)
    frame_index = (frame_index + 1) % len(frames)
    label.after(delay, animate_gif, label, frames, delay, frame_index)

# Added for quality of life improvement
def terminate_program(event=None):
    finT = time.time()
    elapse = finT - iniT
    if elapse < 60:
        print(f"time: {elapse} s")
    elif elapse > 60 and elapse < 3600:
        elapse2 = np.trunc(elapse / 60)
        remain = elapse - (60 * elapse2)
        print(f"time: {elapse2} m, {remain} s")
    else:
        elapse3 = np.trunc(elapse / 3600)
        checkE = elapse - (3600 * elapse3)
        remain2 = 0.0
        remain3 = 0
        if checkE > 60:
            remain2 = np.trunc(checkE / 60)
            remain3 = checkE - (60 * remain2)
            print(f"time: {elapse3} hr, {remain2} m, {remain3} s")
        else:
            print(f"time: {elapse3} hr, {remain2} m, {checkE} s")
    root.destroy()
    exit()

def run_koala():
    global root
    #global top
    global iniT
    global monitors
    root = tk.Tk()
    root.title("YOU ARE LATE")
    #root.attributes("-fullscreen", True)
    iniT = time.time()

    # Get the monitor information
    monitors = get_monitors()

    set_popout(1, root)

    root.bind('<Control-w>', terminate_program)
    root.bind('<Control-q>', terminate_program)
    root.bind('<Escape>', terminate_program)

    label = tk.Label(root, text="DONT MIND ME IM JUST DANCING", font=("Helvetica", 64))
    label.pack(padx=20, pady=20)

    # make sure that the gif and the python code are in the same directory
    gif_path = "./taniecK.gif" 
    gif_image = Image.open(gif_path)
    gif_frames = []

    try:
        while True:
            frame = ImageTk.PhotoImage(gif_image.copy().convert("RGBA"))
            gif_frames.append(frame)
            gif_image.seek(len(gif_frames))  # next frame
    except EOFError:
        pass

    delay = int(gif_image.info['duration'])
            
    gif_label = tk.Label(root)
    gif_label.pack()

    label = tk.Label(root, text="絶賛 寝坊中!!!", font=("Helvetica", 64))
    label.pack(padx=20, pady=20)
            
    animate_gif(gif_label, gif_frames, delay)
    poptime = 3600 #seconds
    root.after(poptime*1000, takeover_koala)

    root.mainloop()

def takeover_koala():
    top = tk.Toplevel()
    top.title("YOU ARE LATE LATE")

    set_popout(0, top)

    top.bind('<Control-w>', terminate_program)
    top.bind('<Control-q>', terminate_program)
    top.bind('<Escape>', terminate_program)

    label2 = tk.Label(top, text="IM STILL DANCING IN MY DREAM", font=("Helvetica", 64))
    label2.pack(padx=20, pady=20)

    # make sure that the gif and the python code are in the same directory
    gif2_path = "./taniecK.gif" 
    gif2_image = Image.open(gif2_path)
    gif2_frames = []

    try:
        while True:
            frame = ImageTk.PhotoImage(gif2_image.copy().convert("RGBA"))
            gif2_frames.append(frame)
            gif2_image.seek(len(gif2_frames))  # next frame
    except EOFError:
        pass

    delay2 = int(gif2_image.info['duration'])
            
    gif2_label = tk.Label(top)
    gif2_label.pack()

    label = tk.Label(top, text="絶賛 寝坊中!!!", font=("Helvetica", 64))
    label.pack(padx=20, pady=20)
            
    animate_gif(gif2_label, gif2_frames, delay2)

    top.mainloop()

def time_keeper():
    while True:
        current_time = datetime.now().strftime("%H:%M")
        if current_time == "13:00":
            run_koala()
            return
        time.sleep(60)

if __name__ == "__main__":
    time_keeper()