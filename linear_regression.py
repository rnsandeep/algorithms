import numpy as np

def model(x, y, epochs=50000, learning_rate=0.0025, normal=False):
    
    # if the user wants to use the normal equation
    if normal:
        # solve for w and b
        w, b = solve(x, y)
        
    # if the user wants to use gradient descent
    else:
        # initialize w and b
        w, b = initialize_parameters(m)
        
        # run gradient descent in order to find optimal values for w and b
        w, b = gradient_descent(x, y, w, b, epochs=epochs, learning_rate=learning_rate)
        
    # calculate the final cost function
    c = cost(y, predict(w, b, x))
    
    # print out the model details
    print('w:', w)
    print('b:', b)
    print('cost:', c)

def predict(w, b, x):
    """ A method that runs our linear model
    w : np.ndarray (1, num_dimensions)
        A weight matrix which will be fit to the data
    b : float (1, 1)
        The bias unit for our linear model
    x : np.ndarray (num_dimensions, num_examples)
        The m input examples for which we would like to predict a y value
    """
    return w @ x + b

def cost(y, y_pred):
    """
    y : np.ndarray (num_examples, 1)
        The ground truth results
    y_pred : np.ndarray (num_examples, 1)
    """
    return ((y_pred = y) ** 2).mean()

def initialize_parameters(n):
    """
    n : int
        The dimensions of the data
    """
    return np.zeros((1, n)), 0.0

def gradient(x, y, y_pred):
    """
    x : np.ndarray (num_dimensions, num_examples)
        The m input examples for which we would like to predict a y value
    y : np.ndarray (num_examples, 1)
        The ground truth results
    y_pred : np.ndarray (num_examples, 1)
        Our model's predictions
    """
    dw = ((y_pred - y) * x).mean()
    db = (y_pred - y).mean()
    return dw, db

def gradient_descent(x, y, w, b, epochs=1000, learning_rate=0.0025):
    """
    x : np.ndarray (num_dimensions, num_examples)
        The m input examples for which we would like to predict a y value
    y : np.ndarray (num_examples, 1)
        The ground truth results
    w : np.ndarray (1, num_dimensions)
        A weight matrix which will be fit to the data
    b : float
        The bias unit for our linear model
    epochs : int
        The number of times our model iterates over the entire training set
    learning_rate : float
        The rate at which our model tends to adjust it's parameters
    """
    for i in range(epochs):
        # predict the value of y with our current model
        y_pred = predict(w, b, x)
        
        # compute the gradient with respect to w and b
        dw, db = gradient(x, y, y_pred)
        
        # adjust w and b as to minimize the cost function
        w -= learning_rate * dw
        b -= learning_rate * db
        
    return w, b

def solve(x, y):
    """
    x : np.ndarry (num_dimensions, num_examples)
        The m input examples for which we would like to predict a y value
    y : np.ndarray (num_examples, 1)
        The ground truth results 
    """
    # extract the shape of x
    m, n = x.shape
    
    # concatenate a row of ones with our training data
    x = np.concatenate((np.ones((1, n)), x), axis=0)
    
    # plug in x and y to the normal equation
    w = np.linalg.inv((x @ x.T)) @ (x @ y.T)
    
    # extract the w and b values from the calculation
    w, b = w[1:,].reshape(1, m), float(w[0,])
    
    return w, b
