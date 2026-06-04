"""
BrainE Cognitive Architecture — Public Interface Stub
"""

from __future__ import annotations
from dataclasses import dataclass

class FeatureIndex:
    """Canonical index registry for the 128-dim BrainE node feature vector.

The node feature vector produced by NodeFactory is laid out as::

    [0:64]    concept_embeddings  64-dim weighted sum of 8 concept vectors
    [64:70]   properties           6 sigmoid-bounded semantic properties
    [70:72]   coordinates          normalized (x, y) in [0, 1]
    [72:75]   temporal             visit_count, memory_decay, prediction_belief
    [75:128]  padding              zero-filled to reach output_dim

Property sub-offsets (0-based within the ``[64:70]`` block):

    Offset  Name            Meaning
    0       traversability  Movement possibility
    1       utility         Usefulness / goal relevance
    2       risk            Danger / hazard level
    3       uncertainty     Epistemic uncertainty / confidence
    4       visibility      Observability / fog-of-war
    5       motion          Dynamic behaviour probability"""
    def traversability(self):
        pass

    def utility(self):
        pass

    def risk(self):
        pass

    def uncertainty(self):
        pass

    def visibility(self):
        pass

    def motion(self):
        pass
