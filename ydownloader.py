import tkinter as tk
from tkinter import messagebox
from pytube import YouTube

def download():
    url= entry_url.get()
    try:
        video = YouTube(url)
        stream = video.streams.get_highest_resolution()
        stream.download()
        messagebox.showinfo("Success", "Video downloaded successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Error in downloading videp {e}")

# Create a window
root = tk.Tk()
root.title("YouTube Downloader Lukitas :)")

#
label_url = tk.Label(root, text="Enter the URL of the video")
label_url.pack(pady=10)

entry_url = tk.Entry(root, width=50)
entry_url.pack(pady=10)

button_download = tk.Button(root, text="Download", command=download)
button_download.pack(pady=10)


root.mainloop()