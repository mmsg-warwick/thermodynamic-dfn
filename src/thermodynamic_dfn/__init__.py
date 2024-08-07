"""
Copyright (c) 2024 Ferran Brosa Planella. All rights reserved.

thermodynamic-dfn: A battery modelling project that implements the DFN model in a thermodynamically consistent framework.
"""
__version__ = "0.1.0"

import pybamm
from .entry_point import Model, parameter_sets, models

__all__ = [
    "__version__",
    "pybamm",
    "parameter_sets",
    "Model",
    "models",
]
