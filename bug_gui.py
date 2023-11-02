import tkinter as tk
from tkinter import ttk

import mysql.connector

config = {
    'user': 'root',
    'password': "root",
    'host': '127.0.0.1',
    'database': 'SE342'
}

connection = mysql.connector.connect(**config)
cursor = connection.cursor()

class BugGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Bug Test Results")

        # Creating Labels and Entry fields
        self.models = ["ChatGPT", "Cohere", "PALM"]
        self.entries = {}

        for index, model in enumerate(self.models):
            label = ttk.Label(root, text=f"Number to add to {model}:")
            label.grid(row=index, column=0, padx=10, pady=5, sticky=tk.W)
            
            entry = ttk.Entry(root)
            entry.grid(row=index, column=1, padx=10, pady=5)
            self.entries[model] = entry

        # Button to insert test results
        btn_insert = ttk.Button(root, text="Insert test results", command=self.add_to_database)
        btn_insert.grid(row=len(self.models), column=0, columnspan=2, pady=10)


    def add_to_database(self):

        chatgpt_bugs = self.entries["ChatGPT"].get()
        cohere_bugs = self.entries["Cohere"].get()
        palm_bugs = self.entries["PALM"].get()

        query = """
        INSERT INTO bugs (ChatGPT_Bugs, PALM_Bugs, Cohere_Bugs)
        VALUES (%s, %s, %s)
        """
        
        cursor.execute(query, (chatgpt_bugs, palm_bugs, cohere_bugs))
        connection.commit()

if __name__ == "__main__":
    root = tk.Tk()
    app = BugGUI(root)
    root.mainloop()
