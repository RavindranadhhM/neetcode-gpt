import numpy as np
from numpy.typing import NDArray


class Solution:
    def forward(self, x: NDArray[np.float64], w: NDArray[np.float64], b: float, activation: str) -> float:
        z = np.dot(x,w)+b
        if activation == 'sigmoid':
            out=1/(1+np.exp(-z))
        if activation == 'relu':
            out=np.maximum(0,z)
        return round(out,5)
