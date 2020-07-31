import numpy as np

m = np.array([[1, 2], [3, 4]])
print("Original Matrix:")
print(m)

result = np.linalg.inv(m)
print("Inverse Matrix:")
print(result)
