from tkinter import *
import tkinter as tk


class Note:
    def __init__(self, root_win):
        def save_note():
            note = note_text.get("1.0", "end-1c")
            with open("notes.txt", "a") as file:
                file.write(note + "\n")
            note_text.delete("1.0", tk.END)
            load_notes()
        def load_notes():
            notes_list.delete(0, tk.END)
            with open("notes.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                    notes_list.insert(tk.END, line)
        def delete_note():
            selected_index = notes_list.curselection()
            if selected_index:
                selected_line = notes_list.get(selected_index)
                notes = []
                with open("notes.txt", "r") as file:
                    lines = file.readlines()
                    for line in lines:
                        if line != selected_line:
                            notes.append(line)
                with open("notes.txt", "w") as file:
                    file.writelines(notes)
                load_notes()
        app = tk.Tk()
        app.title("Note")
        app.geometry("620x380+300+0")
        start_color = '#FFA500'
        end_color = '#FFE5B4'
        background_frame = tk.Frame(app, bg='white', height=200, width=400)
        background_frame.pack(fill='both', expand=True)
        canvas = tk.Canvas(background_frame, bg='white', height=200, width=400)
        canvas.pack(fill='both', expand=True)
        canvas.create_rectangle(0, 0, 1400, 1200, fill=start_color, tags='gradient')
        canvas.create_rectangle(0, 0, 400, 0, fill=end_color, tags='gradient')
        note_text = tk.Text(canvas, height=10, width=50)
        note_text.pack()
        save_button = tk.Button(canvas, text="Enregistrer", command=save_note)
        save_button.pack()
        notes_list = tk.Listbox(canvas, height=10, width=50)
        notes_list.pack()
        load_notes()
        delete_button = tk.Button(canvas, text="Suprimer", command=delete_note)
        delete_button.pack()

if __name__ == "__main__":
    root = Tk()
    system = Note(root)
    root.mainloop()
