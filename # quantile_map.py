# quantile_map.py
import numpy as np
import xarray as xr
import pandas as pd
from scipy.interpolate import interp1d

def quantile_map(obs_hist, fcst_hist, fcst_future):
    """
    obs_hist: 1D array of historical observations (e.g., CHIRPS at pixel) - training period
    fcst_hist: 1D array of historical forecast outputs for same dates (ensemble mean or each member)
    fcst_future: array of raw forecast values to bias-correct
    Returns: bias-corrected fcst_future array
    """
    # empirical CDFs
    obs_sorted = np.sort(obs_hist)
    fcst_sorted = np.sort(fcst_hist)
    # quantile function (inverse CDF) of obs
    obs_q = lambda q: np.interp(q, np.linspace(0,1,len(obs_sorted)), obs_sorted)
    # map fcst value -> its quantile in fcst_hist -> value in obs_hist
    # compute fcst_hist empirical CDF
    def fcst_cdf(x):
        return np.searchsorted(fcst_sorted, x, side='right') / len(fcst_sorted)
    corrected = []
    for x in fcst_future:
        q = fcst_cdf(x)
        corrected.append(obs_q(q))
    return np.array(corrected)