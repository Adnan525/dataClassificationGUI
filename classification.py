from sklearn import datasets, neighbors, metrics, mixture, svm
from sklearn.model_selection import train_test_split, GridSearchCV
import matplotlib.pyplot as plt
import numpy as np
def loadDS(name):
    # we have 3 values here iris, breast-cancer, wine
    # no else block required cause we use radio button and each RB has associated value
    if name == "iris":
        return datasets.load_iris
    if name == "breast-cancer":
        return datasets.load_breast_cancer
    if name == "wine":
        return datasets.load_wine

def classification(name, alg, fold, bestParam, accuracy):
    #loading selected dataset
    df = loadDS(name)

    # target and training data
    X = df.data
    y = df.target
    class_names = df.target_names

    # train test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

    # will check for knn and svm algorithms
    if alg == "knn":
        classAlg = neighbors.KNeighborsClassifier()
        param = [{"n_neighbors" : range(20)}]
        xLabel = "KNN"
    elif alg == "svm":
        classAlg = svm.SVC()
        param = [{"gamma" : [0.0001, 0.001, 0.01, 0.1, 1]}]
        xLabel = "SVC"

    # creating a gridsearchcv object and passing classification alg, fold value and parameter
    gscv_classifier = GridSearchCV(
        estimator= classAlg,
        param_grid= param,
        cv = fold,
        scoring= "accuracy"
    )

    #using the gscv classifier to train the training data
    gscv_classifier.fit(X_train, y_train)

    #taking from tutorial
    print("Grid scores on validation set")
    print()
    means = gscv_classifier.cv_results_["mean_test_score"]
    stds = gscv_classifier.cv_results_["std_test_score"]
    results = gscv_classifier.cv_results_["params"]

    for mean, std, param in zip(means, stds, results):
        print("Parameter: %r, accuracy: %0.3f (+/-%0.03f)" % (param, mean,
                                                              std * 2))
    print()
    print("Best parameter: ", gscv_classifier.best_params_)

    #using trhe gscv classfier on test dataset
    y_pred = gscv_classifier.predict(X_test)

    #plotting confusion matrix and accuracy
    accuracy = metrics.accuracy_score(y_test, y_pred) * 100
    plotcm = metrics.plot_confusion_matrix(gscv_classifier, X_test, y_test, display_labels = class_names)
    plotcm.ax_.set_title("Accuracy = {0:.2f}%".format(accuracy))
    plt.show()