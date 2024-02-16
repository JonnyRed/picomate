"""Microcontroller machine independent services.

The following classes and functions provide machine independent services
for microcontrollers.
"""
# TODO Make an abstract class for all average calculations


class RollingAverage:
    """Compute a rolling average over a range of incoming value."""

    def __init__(self, width):
        """Initialise the class with the number of values to average.

        Initialise the running average with the total number of values to form the average over

        Args:
            width (numeric): >0 indicating the number of integers to evaluate over
        """
        assert isinstance(width, int)
        assert width > 0
        self.width = width
        self.partial_list = True
        self.oldest_index = 0
        self.sum = 0
        self.values = [0] * width
        self.last_average = 0

    def compute_rolling_average(self, value):
        """Compute the rolling average over width values.

        If there are less than width values that have been passed then
        the rolling average is the same as the average.

        Args:
            value (numeric): next value that forms part of the rolling
            sum of width values

        Returns:
            integer: rolling average include the last width values
        """

        self.sum -= self.values[self.oldest_index]
        self.sum += value
        self.values[self.oldest_index] = value

        self.oldest_index += 1
        if self.partial_list:
            self.partial_list = self.oldest_index < self.width

        if self.partial_list:
            self.last_average = self.sum / self.oldest_index
            return self.last_average

        self.oldest_index = self.oldest_index % self.width
        self.last_average = self.sum / self.width
        return self.last_average

    def get_average(self):
        return self.last_average
