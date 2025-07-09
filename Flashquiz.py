import tkinter as tk
from tkinter import simpledialog, messagebox

class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Flashcard Quiz App")
        self.root.geometry("400x300")

        self.flashcards = [{"question": "What is the capital of France?", "answer": "Paris"}]
        self.current_index = 0
        self.showing_answer = False

        self.card_label = tk.Label(root, text="", font=("Helvetica", 16), wraplength=380, justify="center")
        self.card_label.pack(pady=30)

        self.show_button = tk.Button(root, text="Show Answer", command=self.toggle_answer)
        self.show_button.pack()

        nav_frame = tk.Frame(root)
        nav_frame.pack(pady=10)

        tk.Button(nav_frame, text="Previous", command=self.prev_card).grid(row=0, column=0, padx=10)
        tk.Button(nav_frame, text="Next", command=self.next_card).grid(row=0, column=1, padx=10)

        edit_frame = tk.Frame(root)
        edit_frame.pack(pady=10)

        tk.Button(edit_frame, text="Add", command=self.add_card).grid(row=0, column=0, padx=5)
        tk.Button(edit_frame, text="Edit", command=self.edit_card).grid(row=0, column=1, padx=5)
        tk.Button(edit_frame, text="Delete", command=self.delete_card).grid(row=0, column=2, padx=5)

        self.update_card()

    def update_card(self):
        if self.flashcards:
            card = self.flashcards[self.current_index]
            text = card["answer"] if self.showing_answer else card["question"]
            self.card_label.config(text=text)
        else:
            self.card_label.config(text="No flashcards available.")

    def toggle_answer(self):
        self.showing_answer = not self.showing_answer
        self.update_card()

    def next_card(self):
        if self.flashcards:
            self.current_index = (self.current_index + 1) % len(self.flashcards)
            self.showing_answer = False
            self.update_card()

    def prev_card(self):
        if self.flashcards:
            self.current_index = (self.current_index - 1) % len(self.flashcards)
            self.showing_answer = False
            self.update_card()

    def add_card(self):
        question = simpledialog.askstring("Add Flashcard", "Enter question:")
        if question:
            answer = simpledialog.askstring("Add Flashcard", "Enter answer:")
            if answer:
                self.flashcards.append({"question": question, "answer": answer})
                self.current_index = len(self.flashcards) - 1
                self.showing_answer = False
                self.update_card()

    def edit_card(self):
        if not self.flashcards:
            return
        current = self.flashcards[self.current_index]
        question = simpledialog.askstring("Edit Flashcard", "Edit question:", initialvalue=current["question"])
        if question:
            answer = simpledialog.askstring("Edit Flashcard", "Edit answer:", initialvalue=current["answer"])
            if answer:
                self.flashcards[self.current_index] = {"question": question, "answer": answer}
                self.update_card()

    def delete_card(self):
        if not self.flashcards:
            return
        if messagebox.askyesno("Delete", "Are you sure you want to delete this flashcard?"):
            del self.flashcards[self.current_index]
            self.current_index = max(0, self.current_index - 1)
            self.showing_answer = False
            self.update_card()

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()
# This code implements a simple flashcard quiz application using Tkinter.
# Users can add, edit, delete, and navigate through flashcards.
# The application displays a question and allows users to toggle the answer.
# It also includes basic error handling and user prompts for actions.
# The flashcards are stored in a list of dictionaries, each containing a question and an answer.
# The app is designed to be user-friendly and intuitive, making it easy to manage flashcards.
# The main functionalities include showing the current card, navigating through cards, and modifying the flashcards.
# The app is initialized with a sample flashcard and can be expanded by the user.