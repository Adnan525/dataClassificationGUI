import tkinter as tk
root = tk.Tk()
root.title = "Classification in data science"
root.geometry("700x500")

header = tk.Label(
    text = "Classification in Data Science",
    height = 1
)
header.place(x = 10, y = 10)
dataset = tk.StringVar()
selectedDatasetLabel = tk.Label(text = "")
selectedDatasetLabel.place(x = 100, y = 80)
def foo():
    selectedMessage = f"selected dataset is {dataset.get()}."
    selectedDatasetLabel.config(text = selectedMessage)
irisRadioButton = tk.Radiobutton(
    text="Iris",
    variable = dataset,
    value='iris',
    command=foo
)
irisRadioButton.place(x=100, y=50)
breastCancerRadioButton = tk.Radiobutton(
    text = "Breast Cancer",
    variable = dataset,
    value = "breast-cancer",
    command = foo
)
breastCancerRadioButton.place(x=200, y=50)
wineRadioButton = tk.Radiobutton(
    text = "Wine",
    variable = dataset,
    value = "wine",
    command = foo
)
wineRadioButton.place(x = 400, y = 50)
root.mainloop()