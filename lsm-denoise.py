
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
from pandas_datareader import data as pdr
plt.style.use('ggplot')


def denoise(time_series_vector, LAMBDA=100, plot=True):
    """reduces noise (volatility) of a given time serires by factor of LAMBDA 

    Args:
        time_series_vector (nd.Array): one dimentional time series vector
        LAMBDA (int): The penalty factor of the least squares equation which declares how much 
        should the difference between two time series entries be reducted (how strict should the denoising be done). Defaults to 100.
        higher the LAMBDA value results in more noise reduction
        plot (bool, optional): wether to plot the denoised deries. Defaults to True.
    
    Returns:
        x (nd.Array): one dimentional denoised time series vector
    """
    vec = time_series_vector.reshape(-1,1)
    n = vec.shape[0]

    D = np.zeros((n-1 , n))
    for i in range(n-1):
        D[i,i] = 1
        D[i,i+1] = -1

    # Ax = B --> min||Ax-b||^2
    A = np.vstack([np.eye(n), (LAMBDA**0.5)*D])
    b = np.vstack([vec, np.zeros((n-1,1))])

    # Least squares
    # x = INV(X.T* X) * X.T * b
    x = np.matmul(np.linalg.inv(np.matmul(A.T,A)),  np.matmul(A.T,b))


    if plot:
        plt.figure(figsize=(12,8))
        plt.plot(list(range(len(vec))), vec, label='price')
        plt.plot(list(range(len(vec))), x , label=f'Denoised lambda={LAMBDA}', lw=2.5)
        plt.title('Denoising BTC Price with LS')
        plt.xlabel('Time')
        plt.ylabel('Price')
        plt.legend()
        plt.show()
    
    return(x)


if __name__ == '__main__':
    # getting bitcoin historical price data from yahoo finance using pandas_datareader api
    price_data = pdr.get_data_yahoo('BTC-USD', start=datetime(2020,1,1), end=datetime.now())
    price_vec = price_data['Adj Close'].values
    date_vec = price_data.index

    denoised = denoise(price_vec, LAMBDA=100, plot=True)
    print('denoised time series:\n',denoised)





