import numpy as np

arr = np.array([3,5,1,2])
srtd = np.sort(arr)

print(f"The new sorted array returns: {srtd}")

con = np.concatenate([arr, srtd])

print(f"The new concatenated array returns: {con}")