#!/usr/bin/python3
import pytest
import prob_dist
from numpy import zeros, array


def test_distance_positive_integer_integer():
    value = zeros((2,3), dtype=float)
    value = array([[1,3,6],[2,5,8]])
    assert prob_dist.distance(value) == 3

def test_distance_positive_integer_float():
    value = zeros((2, 3), dtype=float)
    value = array([[1, 5, 9], [3, 7, 2]])
    assert prob_dist.distance(value) == 7.54983443527075

def test_distance_positive_float_float():
    value = zeros((2, 3), dtype=float)
    value = array([[1.2, 5.6, 9.3], [3.7, 7.8, 2.0]])
    assert prob_dist.distance(value) == 8.023714850367005