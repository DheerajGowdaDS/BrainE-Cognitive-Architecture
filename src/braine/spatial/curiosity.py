"""
BrainE Cognitive Architecture — Public Interface Stub
"""


class CuriosityEngine:
    """Month 4 Module 1: Curiosity Engine.
Computes intrinsic reward based on map novelty to escape local traps."""
    def __init__(self, known_reward=0.0, frontier_reward=25.0, rare_visit_reward=10.0):
        pass

    def get_intrinsic_reward(self, is_known_node: bool, node_type: int, visit_count: float):
        """Known Node = 0
Unknown Frontier = High Positive
Rarely Visited Known = Mild Positive"""
        pass
