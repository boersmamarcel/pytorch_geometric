import copy

import torch

from torch_geometric.data import TemporalData


def get_temporal_data(num_events, msg_channels):
    return TemporalData(
        src=torch.arange(num_events),
        dst=torch.arange(num_events, num_events * 2),
        t=torch.arange(0, num_events * 1000, step=1000),
        msg=torch.randn(num_events, msg_channels),
        y=torch.randint(0, 2, (num_events, )),
    )

def test_train_val_test_split():
    data = get_temporal_data(num_events=100, msg_channels=16)

    # TODO: implement test
    assert False