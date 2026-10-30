import numpy as np

def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	

	

	eigen_values=np.linalg.eigvals(matrix)
	return eigen_values.tolist()