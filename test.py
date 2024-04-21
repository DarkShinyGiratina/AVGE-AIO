import threading
import glob
import customtkinter as ctk

import GUI.ytdl_gui

app = ctk.CTk()
DEFAULT_FONT_SIZE = 36
DYNAMIC_FONT = ctk.CTkFont("Arial", DEFAULT_FONT_SIZE)
DEFAULT_WIDTH = 1280
DEFAULT_HEIGHT = 720
app.geometry(f"{DEFAULT_WIDTH}x{DEFAULT_HEIGHT}")
app.title("AVGE All-in-One Suite")


def make_tab(tv: ctk.CTkTabview, name: str) -> ctk.CTkFrame:
    ret = tabview.add(name)
    return ret


def resize_font(event):
    global DYNAMIC_FONT
    new_height = app.winfo_height()
    new_size = int(DEFAULT_FONT_SIZE * (new_height / DEFAULT_HEIGHT))
    DYNAMIC_FONT.configure(family="Arial", size=new_size)


tabview = ctk.CTkTabview(master=app)
tabview.pack(fill="both", expand=1)

ytdl_tab = make_tab(tabview, "Download from YouTube")
sub_edit_tab = make_tab(tabview, "Edit Subtitles")
sub_burn_tab = make_tab(tabview, "Burn in Subtitles")
tabview._segmented_button.grid(sticky="W")


ytdl_main_frame = GUI.ytdl_gui.YTDLFrame(parent=ytdl_tab, font=DYNAMIC_FONT)

edit_label = ctk.CTkLabel(
    sub_edit_tab, text="Under Construction! This will let you edit subtitles.", font=DYNAMIC_FONT)
burn_label = ctk.CTkLabel(
    sub_burn_tab, text="Under Construction! This will let you burn in subtitles.", font=DYNAMIC_FONT)


edit_label.grid(row=0, column=0)
burn_label.grid(row=0, column=0)

app.bind("<Configure>", resize_font)
app.mainloop()


# output_file = glob.glob("ytdloutput.*")[0]

# t = threading.Thread(target=ff_e.convert_to_mp4, args=[output_file, "out.mp4"])
# t.start()
# while (t.is_alive()):
#     print(ff_e.progress)
#     time.sleep(0.1)
