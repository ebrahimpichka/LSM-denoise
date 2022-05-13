# LSM-denoise
Denoising time series e.g. historical price data using Least Squares Method in python using NumPy.


## How to use:

The `denoise` function in `lsm-denoise.py` simply could be used by passing a 1-dim numpy array of time series data to the function.

**example:**

```
denoised_prices = denoise(
    price_vec,
    LAMBDA=100,
    plot=True
    )
```

## Intuition:

suppose `y` is the time series vector, `x` is the denoised vector and `v` is an unknown noise vector

![eq1](http://www.sciweavers.org/upload/Tex2Img_1630619351/render.png)

to find `x` we need to solve the following minimization problem using least squares method:

![eq2](http://www.sciweavers.org/upload/Tex2Img_1630619879/render.png)

this problem minimizes the noise factor `v` with the penalty of the difference between two consequetive `x` values become minimized.

the penalty term could be written as:

![eq3](http://www.sciweavers.org/upload/Tex2Img_1630620305/render.png)

where D is an (n-1)x(n) matrix like:

![eq4](http://www.sciweavers.org/upload/Tex2Img_1630620788/render.png)

and finally the main minimization problem could be re-written as"

![eq5](http://www.sciweavers.org/upload/Tex2Img_1630621183/render.png)


## Results:

an example of denoised time series by different LAMBDA valuse plotted below:


![plot](https://github.com/ebrahimpichka/LSM-denoise/blob/master/final_chart.png)

