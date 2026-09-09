import numpy as np

vector1 = [1, 2, 3]
vector2 = [1, 2, 3]
vector3 = [10, 2, 1]

similarity1 = np.dot(vector1, vector2) / (
    np.linalg.norm(vector1) * np.linalg.norm(vector2)
)

similarity2 = np.dot(vector1, vector3) / (
    np.linalg.norm(vector1) * np.linalg.norm(vector3)
)

print("Similarity 1:", similarity1)
print("Similarity 2:", similarity2)