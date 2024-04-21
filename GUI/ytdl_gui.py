import customtkinter as ctk
import Tools.ytdl as dl
import Tools.ffmpeg_encode as ff_e
import threading
import os
import glob


class YTDLFrame(ctk.CTkFrame):
    def __init__(self, parent, font, **kwargs):
        # Setup
        super().__init__(parent, **kwargs)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=2)
        self.grid_columnconfigure((1, 2), weight=1)
        self.font_to_use = font

        # Placing frame in parent
        self.pack(fill="both", expand=True)

        # Components
        self.url_entry = ctk.CTkEntry(self, placeholder_text="Enter your URL here!", font=self.font_to_use)
        self.ETA = ctk.CTkLabel(self, text="", font=self.font_to_use)
        self.download_button = ctk.CTkButton(self, text="Download Video!",
                                             font=self.font_to_use, command=self.run_download)

        # Placing Components
        self.url_entry.grid(row=0, column=0, sticky="ew")
        self.ETA.grid(row=0, column=1, sticky="ew")
        self.download_button.grid(row=0, column=2)

    def run_download(self):
        url = self.url_entry.get()
        self.download_button.configure(text="Downloading...")
        t = threading.Thread(target=dl.start_download, args=[url])
        t.start()
        self.update_download(t)
        return

    def update_download(self, t):
        if not t.is_alive():
            dl = glob.glob("ytdloutput.*")
            if (len(dl) < 1):
                self.ETA.configure(text="No Downloaded Output, try again!")
                self.download_button.configure(text="Download Video!")
                return
            self.ETA.configure(text="")
            dl_name = dl[0]
            output_path = ctk.filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=[("mp4 file", ".mp4")])
            t = threading.Thread(target=ff_e.convert_to_mp4, args=[dl_name, output_path])
            self.download_button.configure(text="Encoding to mp4...")
            t.start()
            self.update_encode(t)
        else:
            self.after(500, self.update_download, t)

    def update_encode(self, t):
        if not t.is_alive():
            self.ETA.configure(text="Done!")
            ff_e.progress = 0
            self.download_button.configure(text="Download Video!")
            dl_file = glob.glob("ytdloutput.*")[0]
            os.remove(dl_file)
        else:
            if ff_e.progress != 0:
                self.ETA.configure(text=f'{ff_e.progress:.2f}% complete...')
            self.after(500, self.update_encode, t)
