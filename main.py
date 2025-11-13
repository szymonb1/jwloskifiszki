import tkinter as tk 
import random
import json
from PIL import ImageTk, Image

root = tk.Tk()
json_data = ""


def window_settings():
    root.configure(background="gray")
    root.minsize(640, 480)
    root.maxsize(1920, 1080)
    window_position_x = (root.winfo_screenwidth() - 640)//2
    window_position_y = (root.winfo_screenheight() - 480)//2
    root.geometry(f"300x300+{window_position_x}+{window_position_y}")

def load_json():
    global json_data
    with open("baza.json", mode="r", encoding="utf-8") as read_file:
        json_data = json.load(read_file) 

def display_excercise():
    # losowanie numerów potrzebnych do wyświetlania głównego zdjęcia i przycisków
    random_numbers = [random.randint(0, len(json_data)-1)]
    while len(random_numbers) < 5:
        random_number = random.randint(0,len(json_data)-1)
        if random_number not in random_numbers:
            random_numbers.append(random_number)
    print(random_numbers)
    
    # wyświetlanie głównego zdjęcia
    image = Image.open(json_data[random_numbers[0]]["image_path"])
    resized_image = image.resize((500,400))
    tkimage = ImageTk.PhotoImage(resized_image)
    label = tk.Label(root, image=tkimage)
    label.image = tkimage
    label.pack(pady=20)

    """italian_text = json_data[random_numbers[0]]["italian_translation"]
    tk.Label(root, text=italian_text).pack()"""

    # przyciski
    buttons = []
    for num in range(1, 5):
        buttons.append(tk.Button(root, text=json_data[random_numbers[num]]["italian_translation"]))
        buttons[num-1].pack(padx=20, pady=20)

    
def main():
    load_json() # ładuje liste z pliku json
    root.title("j. włoski fiszki")
    window_settings() # można później zmienić, żeby więcej argumentów było
    
    display_excercise()

    root.mainloop()

if __name__ == "__main__":
    main()

