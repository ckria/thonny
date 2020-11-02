"""Manipulation of c-style data

This module implements a subset of the corresponding CPython module,
as described below. For more information, refer to the original CPython
documentation: struct.

Supported size/byte order prefixes: *@*, *<*, *>*, *!*.

Supported format codes: *b*, *B*, *x*, *h*, *H*, *i*, *I*, *l*, *L*, *q*, *Q*,
*s*, *P*, *f*, *d* (the latter 2 depending on the floating-point support)."""

def calcsize(fmt: str) -> int:
    """Return the number of bytes needed to store the given fmt."""
    ...

def pack(fmt: Any, *values: Any) -> Any:
    """Pack the values according to the format string fmt.
    The return value is a bytes object encoding the values."""
    ...

def pack_into(fmt: Any, buffer: Any, offset: Any, *values: Any) -> Any:
    """Pack the values according to the format string fmt into a buffer
    starting at offset. offset may be negative to count from the end of buffer."""
    ...

def unpack(fmt: Any, data: Any) -> Any:
    """Unpack from the data according to the format string fmt. The return value
    is a tuple of the unpacked values. The buffer size must match the size
    required by the format."""
    ...

def unpack_from(fmt: Any, data: Any, offset: Any = 0) -> Any:
    """Unpack from the data starting at offset according to the format string fmt.
    offset may be negative to count from the end of buffer. The return value is
    a tuple of the unpacked values. The buffer size must be at least as big
    as the size required by the form."""
    ...
