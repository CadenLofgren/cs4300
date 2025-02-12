import numpy as np

def calculate_mean(numbers):
    mean = np.mean(numbers)
    return mean


sample_data = [1, 2, 3, 4, 5]
print("Mean:", calculate_mean(sample_data))


def test_calculate_mean():
    data = [1, 2, 3, 4, 5]
    expected = sum(data) / len(data)  
    assert calculate_mean(data) == expected

