from .swap_elements import SwapElements
from .swap_rows import SwapRows
from .swap_columns import SwapColumns
from .transpose import Transpose
from .shuffle_row import ShuffleRow
from .shuffle_column import ShuffleColumn
from .swap_diagonals import SwapDiagonals
from .swap_oddEven import SwapOddEven
from .reverse_row import ReverseRow
from .reverse_column import ReverseColumn


LLH_CLASSES = [
    SwapElements(),
    SwapRows(),
    SwapColumns(),
    Transpose(),
    ShuffleRow(),
    ShuffleColumn(),
    SwapDiagonals(),
    SwapOddEven(),
    ReverseRow(),
    ReverseColumn(),
]
