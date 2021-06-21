from dataclasses import dataclass

from tst.types.blockchain_format.sized_bytes import bytes32
from tst.util.ints import uint32
from tst.util.streamable import Streamable, streamable


@dataclass(frozen=True)
@streamable
class PoolTarget(Streamable):
    puzzle_hash: bytes32
    max_height: uint32  # A max height of 0 means it is valid forever
