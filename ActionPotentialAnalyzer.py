import numpy as np
# import scipy as sp
import scipy.signal as sig
import pandas as pd
# import stfio


class ActionPotentialAnalyzer:
    """

    """

    def __init__(self, action_potential_data, sampling_freq, resample_freq):
        """

        """
        self.original_data = action_potential_data
        self.sampling_freq = sampling_freq
        self.resample_freq = resample_freq
        self.resample_data = sig.resample(self.original_data, self.sampling_freq, self.resample_freq)

    @staticmethod
    def resample(data, original_freq, desired_freq):
        """

        :param data:
        :param original_freq:
        :param desired_freq:
        :return:
        """
        number_of_data_points = len(data)
        number_of_resampled_data_points = number_of_data_points * desired_freq / original_freq
        return sig.resample_poly(data, number_of_resampled_data_points, number_of_data_points)
