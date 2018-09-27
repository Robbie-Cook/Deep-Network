import numpy as np
import math
import settings

"""
Metrics.py

Methods to evaluate the accuracy of predicted values from expected

@author: Robbie Cook
"""



"""
Method which gets the MAE of the network -- takes the same inputs as getGoodness
"""
def getMAE(predicted, expected):
    assert len(predicted) == len(expected), "Predicted and expected must be the same length"

    sum = 0
    for i in range(len(predicted)): # Get mean MAE

        local_sum = 0
        assert len(predicted[i]) == len(expected[i]), \
        "Rows of predicted and expected must be the same length"

        for j in range(len(predicted[i])): # get actual MAE
            local_sum += abs(predicted[i][j]-expected[i][j])
        sum += local_sum/len(predicted[i])
    
    return sum/len(predicted) # Return the mean MAE

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
Method which gets the metric of the network
"""
def getTaskQuality(model, tasks):
    X = np.array([tasks[i]['input'] for i in range(len(tasks))]) # Inputs
    Y = np.array([tasks[i]['teacher'] for i in range(len(tasks))]) # Teaching outputs
    print("----------")
   
    [print(t['teacher']) for t in tasks]
    
    print("----------")
    if settings.metric == 'goodness':
        return getGoodness(predicted=model.predict(X), expected=Y)
    else:
        return_value = model.evaluate(X,Y)
        return return_value[1]
