import tkinter as tk
root = tk.Tk()
root.title = "Classification in data science"
root.geometry("700x500")
targetDF = ""
targetModel = ""
isFoldCorrect = False
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
    global targetDF
    selectionMessage = f"selected dataset is {dataset.get()}."
    selectedDatasetLabel.config(text = selectionMessage)
    targetDF = dataset.get()
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
    global targetModel
    selectionMessage = f"{classAlgName.get()} algorithm selected."
    selectedAlgorithmLabel.config(text=selectionMessage)
    targetModel = classAlgName.get()

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
# set default fold value to 3
fold = tk.StringVar(value="3") #can extract only string from entry
foldLabel = tk.Label(text= "number of folds : ")
foldLabel.place(x = 100, y = 200)

checkMessageDefault = "no check has been done yet"
checkMessage = tk.Text()
checkMessage.insert("end", checkMessageDefault)
checkMessage.place(width=500, height = 100)
checkMessage.place(x=100, y=250)

def check():
    global targetDF
    global targetModel
    global isFoldCorrect
    checkMessage.delete("1.0", "end")
    if int(int(fold.get())) <= 1:
        checkMessage.insert("end", f"Fold number has to be greater than 1, you selected {fold.get()}")
        isFoldCorrect = False
    else:
        checkMessage.insert("end", f"{targetDF} dataset selected.\n")
        checkMessage.insert("end", f"{targetModel} algorithm selected.\n")
        checkMessage.insert("end", f"{fold.get()} fold selected.")
        isFoldCorrect = True

# fold.trace_add("read", checkFold())

foldEntry = tk.Entry(textvariable=fold)
foldEntry.place(x=250, y=200)

loadButton = tk.Button(
    text = "Check",
    command = check
)
loadButton.place(x = 500, y = 200)

root.mainloop()