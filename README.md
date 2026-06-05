
# Brain — Unified Cognitive Architecture for Grid World AI

![](https://img.shields.io/badge/python-3.12-blue.svg) ![](https://img.shields.io/badge/framework-PyTorch%20%7C%20MiniGrid-orange.svg) ![](https://img.shields.io/badge/architecture-8--Phase%20Decoupled-brightgreen.svg)

Brain is an enterprise-grade cognitive engine engineered to navigate, reason, and adapt within complex, sparse-reward, and procedurally generated grid world environments. By breaking away from traditional flat end-to-end reinforcement learning policies, BrainE introduces a decoupled, multi-layered processing loop. It isolates raw sensory processing from internal topological tracking and hierarchical spatial planning, allowing AI agents to solve extreme long-horizon bottlenecks systematically.

---

## 📂 Core Architecture & Package Specifications

Brain organizes distinct cognitive responsibilities into a highly decoupled `src/` layout package tree. Each module represents an isolated phase of the agent's structural runtime:

- [x] **`perception`** — Processes raw environment matrix grids into semantic object feature layers.
- [x] **`grounding`** — Coordinates multi-modal state representations with active action spaces.
- [x] **`spatial`** — Dynamically builds topology graphs, tracking relative motion vectors and frontiers.
- [x] **`world_model`** — Maintains an evolving belief state of hidden environmental mechanics.
- [x] **`cognition`** — Manages in-memory context persistence, graph queries, and cross-prompt role tracking.
- [x] **`planning`** — Executes hierarchical subgoal generation and semantic utility scoring.
- [x] **`learning`** — Controls policy refinement loops, intrinsic curiosity rewards, and skill-memory commits.

---

## 🎨 Architecture Diagrams

The orchestration framework decouples execution into synchronous, highly predictable pipelines. Data transitions smoothly from raw observation tensors to targeted motion vectors.

### 1. Unified Cognitive Loop Dataflow
The flow diagram below outlines how environment states pass through the perception engine, update internal spatial tracking graphs, and resolve down into the hierarchical action planner:

```text
       ┌────────────────────────┐
       │  MiniGrid Environment  │
       └───────────┬────────────┘
                   │  (Observation Tensor)
                   ▼
       ┌────────────────────────┐
       │    perception Layer    │
       └───────────┬────────────┘
                   │  (Semantic Feature Map)
                   ▼
       ┌────────────────────────┐
       │   spatial Topology     │ ◄───► ┌────────────────────────┐
       │     Tracker Graph      │       │     cognition Node     │
       └───────────┬────────────┘       │     Memory Graph       │
                   │                    └────────────────────────┘
                   │  (Frontier & Wavefront Paths)
                   ▼
       ┌────────────────────────┐
       │  planning Subsystem    │
       └───────────┬────────────┘
                   │  (Hierarchical Subgoals)
                   ▼
       ┌────────────────────────┐
       │  grounding & Actions   │ ───►  [ Execute Primitive Action ]
       └────────────────────────┘

```

### 2. Pipeline Execution Sequence

This sequence outlines the frame-by-frame orchestration matrix managed by the core runtime pipeline:

```text
Observation Engine         Perception Layer          Tracker/Memory            Action Planner
       │                           │                        │                         │
       │─── Observation Tensors ───│                        │                         │
       │                           │── Semantic States ─────│                         │
       │                           │                        │── Dynamic Topologies ───│
       │                           │                        │                         │── Subgoal Selection ──┐
       │                           │                        │                         │                       │
       │──────────────────────────────────────────────────────────────────────────────│◄──────────────────────┘
       │     Executed Primitive

```

---

## 🚀 The Demo Video

Experience the Brain cognitive system actively navigating hazard-dense, sparse-reward maps in real time. This demonstration highlights the live synchronization between the agent's spatial frontier mappings and the tracking diagnostics panel.

https://github.com/user-attachments/assets/3c085b33-d906-46e6-932b-cb02cb614e1b

> 🎬 **What to Look For in the Demo:**
> * **Real-Time Frontier Expansion:** Watch the agent build tracking node maps in real-time as it explores dark regions.
> * **Dynamic Sequence Execution:** Notice how the engine paths back to collect hidden key targets once a door obstruction is observed.
> 
> 

---

## 📊 Final Validation — Unseen Gauntlet Results

The completed unified architecture was rigorously evaluated across an automated execution gauntlet containing completely unseen, long-horizon procedural configurations. Brain demonstrated absolute zero-shot generalization advantages:

| Environment | Success Rate | Avg Steps | Avg Nodes | Pickups | Toggles |
| --- | --- | --- | --- | --- | --- |
| **DoorKey-8x8** | 🌟50.0% | 102.7 | 47.1 | 9 | 9 |
| **LavaCrossingS9N3** | 🌟 60.0% | 90.6 | 42.6 | 0 | 0 |
| **MultiRoom-N2-S4** | 0.0% | 40.0 | 13.5 | 0 | 0 |
| **Unlock** | 🌟 90.0% | 49.0 | 32.0 | 9 | 9 |
| **KeyCorridorS3R1** | 0.0% | 250.0 | 9.0 | 0 | 0 |
| **SimpleCrossingS9N2** | 🌟 70.0% | 94.5 | 54.0 | 0 | 0 |
| **OVERALL AVERAGE** | **45.0%** | — | — | — | — |

### 📈 Empirical Performance Highlights

* **Unlock (90.0% Success):** Validates near-perfect environmental multi-object tracking and target interaction sequences.
* **SimpleCrossing & LavaCrossing (70% / 60% Success):** Proves the robust spatial tracking framework allows for safe trajectory navigation around high-hazard, immediate-termination cells.
* **KeyCorridor (0.0% Active Baseline):** Represents a highly complex multi-stage tracking layout, acting as the primary target for our next iterative multi-phase training sprint.

---

*Copyright © 2026 DheerajGowdaDS / Brain Project. Proprietary and Confidential. All Rights Reserved.*

