import tkinter as tk
root = tk.Tk()
root.title = "Classification in data science"
root.geometry("700x500")

header = tk.Label(
    text = "Classification in Data Science",
    height = 1
)
header.place(x = root.winfo_reqwidth()/2, y = 5)

selectDatasetLabel = tk.Label(text="Select a dataset: ")
selectDatasetLabel.place(x = 100, y = 20)

dataset = tk.StringVar()
selectedDatasetLabel = tk.Label(text = "")
selectedDatasetLabel.place(x = 100, y = 80)

def foo():
    selectionMessage = f"selected dataset is {dataset.get()}."
    selectedDatasetLabel.config(text = selectionMessage)
irisRB = tk.Radiobutton(
    text="Iris",
    variable = dataset,
    value='iris',
    command=foo
)
irisRB.place(x=100, y=50)
breastCancerRB = tk.Radiobutton(
    text = "Breast Cancer",
    variable = dataset,
    value = "breast-cancer",
    command = foo
)
breastCancerRB.place(x=200, y=50)
wineRB = tk.Radiobutton(
    text = "Wine",
    variable = dataset,
    value = "wine",
    command = foo
)
wineRB.place(x = 400, y = 50)

selectClassifierLabel = tk.Label(text = "Select a classifier: ")
selectClassifierLabel.place(x = 100, y = 120)

classAlgName = tk.StringVar()
selectedAlgorithmLabel = tk.Label(text = "")
selectedAlgorithmLabel.place(x = 100, y  = 170)
def onClickClassificationRB():
    selectionMessage = f"{classAlgName.get()} algorithm selected."
    selectedAlgorithmLabel.config(text=selectionMessage)

knnRB = tk.Radiobutton(
    text="KNN",
    variable = classAlgName,
    value='KNN',
    command=onClickClassificationRB
)
knnRB.place(x=100, y=150)
supportVectorRB = tk.Radiobutton(
    text = "Support Vector Classification",
    variable = classAlgName,
    value = "Support Vector Classification",
    command = onClickClassificationRB
)
supportVectorRB.place(x=200, y=150)
gaussianRB = tk.Radiobutton(
    text = "Gaussian Mixture Model",
    variable = classAlgName,
    value = "Gaussian Mixture Model",
    command = onClickClassificationRB
)
gaussianRB.place(x = 400, y  = 150)
root.mainloop()