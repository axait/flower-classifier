# class InvalidInput(Exception):
#     def __init__(self) -> None:
#         self.message = 'Enter INTEGERS value only '
#     def __str__(self):
#         return f"MESSAGE : {self.message}"


def importmodel():
    import pickle
    with open('model', 'rb') as file:   #.\irisTRAINEDmodel\
        model = pickle.load(file)
        return model


def floatinput():
    """
    ['sepal length (cm)',
    'sepal width (cm)',
    'petal length (cm)',
    'petal width (cm)']
        sepal length:   4.3  7.9   5.84   0.83    0.7826
        sepal width:    2.0  4.4   3.05   0.43   -0.4194
        petal length:   1.0  6.9   3.76   1.76    0.9490  (high!)
        petal width:    0.1  2.5   1.20   0.76    0.9565  (high!)
    """
    # SEPAL_LENGHT
    while True:
        sepal_length = input('Enter sepal length (cm) :  ')
        try:
            sepal_length =float(sepal_length)
            break
        except Exception as error:
            print(error)

    # SEPAL_WIDHT
    while True:
        sepal_width = input('Enter sepal width (cm) :  ')
        try:
            sepal_width =float(sepal_width)
            break
        except Exception as error:
            print(error)

    # PATEL_LENGHT
    while True:
        petal_length = input('Enter petal length (cm) :  ')
        try:
            petal_length =float(petal_length)
            break
        except Exception as error:
            print(error)

    # PATEL_WIDHT
    while True:
        petal_width = input('Enter petal_width (cm) :  ')
        try:
            petal_width =float(petal_width)
            break
        except Exception as error:
            print(error)

    #   return sepal_length, sepal_width, petal_length, petal_width values
    return sepal_length, sepal_width, petal_length, petal_width


def predictValue(model, sepal_length: str, sepal_width: str, petal_length: str, petal_width: str) -> str:
    predictions = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
    predictions = predictions[0]
    # 0 : 'setosa', 1 : 'versicolor', 2 : 'virginica'
    match predictions:
        case 0:
            return "setosa"
        case 1:
            return "versicolor"
        case 2:
            return "virginica"
        case _:
            ...


def main():
    Classifier = importmodel()
    sepal_length, sepal_width, petal_length, petal_width = floatinput()
    result = predictValue(Classifier, sepal_length,
                          sepal_width, petal_length, petal_width)
    print(result)


if __name__ == "__main__":
    main()
