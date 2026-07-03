import numpy as np
from numpy.typing import NDArray


class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array of logits
        # Hint: subtract max(z) for numerical stability before computing exp
        # return np.round(your_answer, 4)
        top_z = max(z)
        total = sum([np.exp(i-top_z)  for i in z])
        
        output = []
        for i in z:
            output.append(round(np.exp(i - top_z) / total, 4))

        return output