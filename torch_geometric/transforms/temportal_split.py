import warnings
from copy import copy
from typing import List, Optional, Union

import torch
from torch import Tensor

from torch_geometric.transforms import BaseTransform

@functional_transform('random_temporal_split')
class RandomTemporalSplit(BaseTransform):

    def __init__(
            self,
            val_ratio: float = 0.15,
            test_ratio: float = 0.15
    ):
        self.val_ratio = val_ratio
        self.test_ratio = test_ratio

    def forward(self,
                data: Data) -> Data:
        pass

    def _split(self):
        pass
    
    
    def __repr__(self) -> str:
        pass
    
