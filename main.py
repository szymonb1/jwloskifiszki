import tkinter as tk
import random
import json

root = tk.Tk()

images = {
     
}


def window_settings():
    root.configure(background="gray")
    root.minsize(640, 480)
    root.maxsize(1920, 1080)
    window_position_x = (root.winfo_screenwidth() - 640)//2
    window_position_y = (root.winfo_screenheight() - 480)//2
    root.geometry(f"300x300+{window_position_x}+{window_position_y}")

def display_excercise():
    

    # wyświetlić obrazek
    
    print("sus")
    tk.Label(root, image=image1).pack()

    # wyświetlić 4 opcje losowe w tym jedna prawidłowa
    italian_text = json_data[0]["italian_translation"]
    tk.Label(root, text=italian_text).pack()

    
    
def main():
    
    with open("baza.json", mode="r", encoding="utf-8") as read_file:
        json_data = json.load(read_file)
    
    image_path = json_data[0]["image_path"]
    image1 = tk.PhotoImage(file=image_path)
    root.title("j. włoski fishki")
    window_settings() # można później zmienić, żeby więcej argumentów było
    display_excercise()
    
    
    root.mainloop()

if __name__ == "__main__":
    main()

