"""
BrainE Cognitive Architecture — Public Interface Stub
"""

from __future__ import annotations
import torch
import torch.nn as nn
from braine.spatial.state import SpatialGraphState

class SpatialTracker:
    """Tracks allocentric position and orientation using MiniGrid-style transition rules."""
    def __init__(self):
        pass

    def reset(self, batch_size: int, device: torch.device):
        """Re-initialise tracker for a new episode batch."""
        pass

    def step(self, actions: torch.Tensor):
        """Advance one environment step and return the new allocentric state.

Action convention (matches BrainE primitive space):
  0 = turn left
  1 = turn right
  2 = move forward"""
        pass

    def get_current_state(self):
        """Build the 9-node allocentric spatial graph for the current frame."""
        pass
