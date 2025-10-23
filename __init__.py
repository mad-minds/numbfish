# mad-minds's numbfish package.
# This makes the numbfish submodule importable as a proper Python package
__version__ = "0.1.0"
__author__ = "numbfish"
__email__ = "mad@madminds.ai"

# Relative imports from the subpackage (avoids conflicts)
from . import numbfish as _numbfish_module
from . import tools as _tools_module
from . import nnue_eval as _nnue_eval_module

# Make the modules available at package level
numbfish = _numbfish_module
tools = _tools_module
nnue_eval = _nnue_eval_module

# Make the main classes and functions available at package level
Searcher = _numbfish_module.Searcher
Position = _numbfish_module.Position
Entry = _numbfish_module.Entry
pst = _numbfish_module.pst
piece = _numbfish_module.piece
render = _numbfish_module.render

__all__ = [
    # Main modules
    "numbfish",
    "tools",
    "nnue_eval",
    # Main classes
    "Searcher",
    "Position",
    "Entry",
    # Constants
    "pst",
    "piece",
    "render",
]
