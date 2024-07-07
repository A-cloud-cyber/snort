
import tkinter as tk
from tkinter import ttk, scrolledtext
from PIL import ImageTk, Image

def about_window():
    snort = tk.Tk()
    snort.title('ABOUT')
    snort.geometry('600x515')

    tc = '''
SNORT-GUI is a Open Source Application developed by SnortAymaneelmazani  for enterprise intrusion detection systems and cyber-forensic analysis.
                -------------------------------------------------
                Using libpcap version 1.10.1 (with TPACKET_V3)
                Using PCRE version: 8.39 2016-06-14
                Using ZLIB version: 1.2.11
'''  # Restez le texte de description ici

    # Création d'un canvas pour afficher l'image de fond
    canvas = tk.Canvas(snort, width=600, height=515)
    canvas.pack(fill=tk.BOTH, expand=True)

    # Charger et afficher l'image de fond
    img = Image.open('../assets/images/snort_about.jpg')
    img = img.resize((600, 515), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    canvas.create_image(0, 0, image=img, anchor=tk.NW)

    # Texte déroulant
    T = scrolledtext.ScrolledText(snort, width=69, height=28)
    T.insert(tk.INSERT, tc)
    T.config(state='disabled')
    canvas.create_window(15, 10, anchor=tk.NW, window=T)

    snort.resizable(False, False)
    snort.mainloop()

if __name__ == "__main__":
    about_window()
