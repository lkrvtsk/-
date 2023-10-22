import numpy as np

N = 2
X = np.column_stack((np.ones(12), np.arange(N, N+12), np.random.randint(60, 83, 12)))

Y = np.random.uniform(13.5, 18.6,12)


A = np.linalg.inv(X.T @ X) @ X.T @ Y

Y_predicted = X @ A

print("оценки коэф \n", A) #оценки коэф
print("исходные \n", Y) #исходные
print("предсказаннные \n",Y_predicted) #предсказаннные
