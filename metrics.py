import numpy as np

"""
Metrics.py

Methods to evaluate the accuracy of predicted values from expected

@author: Robbie Cook
"""

"""
Method to get "goodness" of a network, proposed by Roger Ratcliff

@param predicted: a 2d array of the generated values (generated by the network)
@param expected: a 2d array of the expected values

@return: a value representing the goodness of the network
"""
def getGoodness(predicted, expected):
    assert len(predicted) == len(expected), "Predicted and expected must be the same length"

    # operations cannot be done in place
    transformedPredicted = [list(range(len(i))) for i in predicted]
    transformedExpected = [list(range(len(i))) for i in expected]
    sumDot = 0 # Running total of the sum of the goodnesses

    for i in range(len(predicted)):
        assert len(predicted[i]) == len(expected[i]), "Predicted and expected must be the same length"
        for j in range(len(predicted[i])):
            transformedPredicted[i][j] = predicted[i][j]*2-1
            transformedExpected[i][j] = expected[i][j]*2-1
        sumDot += np.dot(transformedPredicted[i], transformedExpected[i]) / len(transformedPredicted[i])

    return sumDot / len(predicted) # return mean goodness

"""
Method which gets the goodness of the network 
"""
def getTaskGoodness(model, tasks):
    X = np.array([tasks[i]['input'] for i in range(len(tasks))]) # Inputs
    Y = np.array([tasks[i]['teacher'] for i in range(len(tasks))]) # Teaching outputs

    return getGoodness(predicted=model.predict(X), expected=Y)
