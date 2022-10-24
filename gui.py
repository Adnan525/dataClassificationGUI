import tkinter as tk
import classification

# boolean checks to activate run button
isFoldCorrect = False
isDataLoaded = False
isClassSelected = False

# global var to keep track of chosen dataset and algorithm
targetDF = ""
targetModel = ""
targetFold = -1

def main():
    root = tk.Tk()
    root.title("Classification in data science")
    root.geometry("700x500")

    selectDatasetLabel = tk.Label(text="Select a dataset: ")
    selectDatasetLabel.place(x=100, y=20)

    dataset = tk.StringVar()
    selectedDatasetLabel = tk.Label(text="", fg="#ff0000")
    selectedDatasetLabel.place(x=100, y=80)

    def onClickDFRB():
        global targetDF
        global isDataLoaded
        selectionMessage = f"Selected dataset is {dataset.get()}."
        selectedDatasetLabel.config(text=selectionMessage)
        targetDF = dataset.get()
        isDataLoaded = True

    # adding radio buttons
    # value will be just small letter
    irisRB = tk.Radiobutton(
        text="Iris",
        variable=dataset,
        value='iris',
        command=onClickDFRB
    )
    irisRB.place(x=100, y=50)

    breastCancerRB = tk.Radiobutton(
        text="Breast Cancer",
        variable=dataset,
        value="breast-cancer",
        command=onClickDFRB
    )
    breastCancerRB.place(x=200, y=50)
    wineRB = tk.Radiobutton(
        text="Wine",
        variable=dataset,
        value="wine",
        command=onClickDFRB
    )
    wineRB.place(x=400, y=50)

    # classification algorithm
    selectClassifierLabel = tk.Label(text="Select a classifier: ")
    selectClassifierLabel.place(x=100, y=120)

    classAlgName = tk.StringVar()
    selectedAlgorithmLabel = tk.Label(text="", fg="#ff0000")
    selectedAlgorithmLabel.place(x=100, y=170)

    def onClickClassificationRB():
        global targetModel
        global isClassSelected
        selectionMessage = f"{classAlgName.get()} algorithm selected."
        selectedAlgorithmLabel.config(text=selectionMessage)
        targetModel = classAlgName.get()
        isClassSelected = True

    knnRB = tk.Radiobutton(
        text="KNN",
        variable=classAlgName,
        value='knn',
        command=onClickClassificationRB
    )
    knnRB.place(x=100, y=150)

    supportVectorRB = tk.Radiobutton(
        text="Support Vector Classification",
        variable=classAlgName,
        value="svm",
        command=onClickClassificationRB
    )
    supportVectorRB.place(x=200, y=150)
    # gaussianRB = tk.Radiobutton(
    #     text = "Gaussian Mixture Model",
    #     variable = classAlgName,
    #     value = "gmm",
    #     command = onClickClassificationRB
    # )
    # gaussianRB.place(x = 400, y  = 150)

    # set default fold value to 3
    fold = tk.StringVar(value="3")  # can extract only string from entry
    foldLabel = tk.Label(text="number of folds : ")
    foldLabel.place(x=100, y=200)

    checkMessageDefault = "No check has been done yet"
    checkMessage = tk.Text()
    checkMessage.insert("end", checkMessageDefault)
    checkMessage.place(width=500, height=200)
    checkMessage.place(x=100, y=250)

    def check():
        global targetDF
        global targetModel
        global isFoldCorrect
        checkMessage.delete("1.0", "end")
        checkMessage.insert("end", "======================================\n")
        if int(int(fold.get())) <= 1:
            checkMessage.insert("end", f"Fold number has to be greater than 1, you selected {fold.get()}\n")
            isFoldCorrect = False
        else:
            global targetFold
            checkMessage.insert("end", f"{targetDF} dataset selected.\n")
            checkMessage.insert("end", f"{targetModel} algorithm selected.\n")
            checkMessage.insert("end", f"{fold.get()} fold selected.\n")
            isFoldCorrect = True
            targetFold = int(fold.get())
        checkMessage.insert("end", "======================================\n")
        # activate run button
        if isClassSelected and isDataLoaded and isFoldCorrect:
            run.config(state="normal")

    # fold.trace_add("read", checkFold())

    foldEntry = tk.Entry(textvariable=fold)
    foldEntry.place(x=250, y=200)

    loadButton = tk.Button(
        text="Check",
        command=check
    )
    loadButton.place(x=500, y=200)

    # resultLabel = tk.Label(text= "")
    # resultLabel.place(x = 300, y = 450)

    def onCLickRun():
        classification.classification(targetDF, targetModel, targetFold, checkMessage)
        # bpStr = ("Best param : "+classification.bestParam)
        # print(bpStr)
        # checkMessage.insert("end", bpStr)
        # print("testing in gui best param " + classification.modelAccuracy)
        # checkMessage.insert("end", f"Best parameter : {classification.bestParam}")
        # checkMessage.insert("end", f"Accuracy : {classification.modelAccuracy}")

    run = tk.Button(
        text="Run",
        state="disabled",
        command=onCLickRun
    )
    run.place(x=100, y=450)
    root.mainloop()