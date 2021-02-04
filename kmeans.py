import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def Kmeans(k, data, limit):

    idx = np.random.choice(data.shape[0], k, replace=False)
    centers = data[idx, :]
    labeled = None
    labels = np.arange(len(centers))
    distances = np.zeros((len(labels), len(data)))

    for itr in range(limit):
        for label in labels:
            distances[label] = np.linalg.norm(data - centers[label], axis=1)
        labeled = np.argmin(distances, axis=0)
        for label in labels:
            di = data[np.where(labeled == label)]
            if di.any():
                centers[label] = np.mean(di, axis=0)

    return centers, labeled

