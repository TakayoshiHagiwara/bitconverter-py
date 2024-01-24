# -----------------------------------------------------------------------
# Author:   Takayoshi Hagiwara (KMD)
# Created:  2024/1/24
# Summary:  Converts basic data types to byte arrays and byte arrays to basic data types.
#           The BitConverter class in C# is used as a reference.
# -----------------------------------------------------------------------

import struct

def get_bytes_bool(arg: bool) -> bytes:
    """
    Returns the specified bool value as a bytes.

    Parameters
    ----------
    arg : bool
        The value to convert.
    
    Returns
    -------
    b : bytes
        A bytes object with length 1.
    """
    return struct.pack('<?', arg)

def get_bytes_char(arg: str) -> bytes:
    """
    Returns the specified Unicode character value as a bytes.

    Parameters
    ----------
    arg : str
        The value to convert.
    
    Returns
    -------
    b : bytes
        A bytes object with length 1.
    """
    if len(arg) != 1:
        raise ValueError('The length of the argument must be 1.')
    
    arg = bytes(arg, 'utf-8')
    return struct.pack('<c', arg)

def get_bytes_double(arg: float) -> bytes:
    """
    Returns the specified double-precision floating-point value as a bytes.

    Parameters
    ----------
    arg : float
        The value to convert.
    
    Returns
    -------
    b : bytes
        A bytes object with length 8.
    """
    return struct.pack('<d', arg)

def get_bytes_int16(arg: int) -> bytes:
    """
    Returns the specified 16-bit signed integer value as a bytes.

    Parameters
    ----------
    arg : int
        The value to convert.
    
    Returns
    -------
    b : bytes
        A bytes object with length 2.
    
    Notes
    -----
    Type comparison.

    C#: short
    .NET: System.Int16
    Python: int
    """
    return struct.pack('<h', arg)

def get_bytes_int32(arg: int) -> bytes:
    """
    Returns the specified 32-bit signed integer value as a bytes.

    Parameters
    ----------
    arg : int
        The value to convert.
    
    Returns
    -------
    b : bytes
        A bytes object with length 4.
    
    Notes
    -----
    Type comparison.
    
    C#: int
    .NET: System.Int32
    Python: int
    """    
    return struct.pack('<i', arg)

def get_bytes_int64(arg: int) -> bytes:
    """
    Returns the specified 64-bit signed integer value as a bytes.

    Parameters
    ----------
    arg : int
        The value to convert.
    
    Returns
    -------
    b : bytes
        A bytes object with length 8.
    
    Notes
    -----
    Type comparison.
    
    C#: long
    .NET: System.Int64
    Python: int
    """
    return struct.pack('<q', arg)

def get_bytes_single(arg: float) -> bytes:
    """
    Returns the specified single-precision floating-point value as a bytes.

    Parameters
    ----------
    arg : float
        The value to convert.
    
    Returns
    -------
    b : bytes
        A bytes object with length 4.
    
    Notes
    -----
    Type comparison.
    
    C#: float
    .NET: System.Single
    Python: float (Internally double precision)
    """
    return struct.pack('<f', arg)

def get_bytes_uint16(arg: int) -> bytes:
    """
    Returns the specified 16-bit unsigned integer value as a bytes.

    Parameters
    ----------
    arg : int
        The value to convert.
    
    Returns
    -------
    b : bytes
        A bytes object with length 2.
    
    Notes
    -----
    Type comparison.

    C#: ushort
    .NET: System.UInt16
    Python: int
    """
    return struct.pack('<H', arg)

def get_bytes_uint32(arg: int) -> bytes:
    """
    Returns the specified 32-bit unsigned integer value as a bytes.

    Parameters
    ----------
    arg : int
        The value to convert.
    
    Returns
    -------
    b : bytes
        A bytes object with length 4.
    
    Notes
    -----
    Type comparison.

    C#: uint
    .NET: System.UInt32
    Python: int
    """
    return struct.pack('<I', arg)

def get_bytes_uint64(arg: int) -> bytes:
    """
    Returns the specified 64-bit unsigned integer value as a bytes.

    Parameters
    ----------
    arg : int
        The value to convert.
    
    Returns
    -------
    b : bytes
        A bytes object with length 8.
    
    Notes
    -----
    Type comparison.

    C#: ulong
    .NET: System.UInt64
    Python: int
    """    
    return struct.pack('<Q', arg)

def to_bool(arg: bytes, start_index: int = 0) -> bool:
    """
    Returns a bool value converted from the byte at a specified position in a bytes.

    Parameters
    ----------
    arg : bytes
        A bytes object with length 1.
    start_index : int, optional
        The index of the byte within arg to convert.
    
    Returns
    -------
    value : bool
        True if the byte at start_index in arg is nonzero; otherwise, False.
    """
    b = struct.unpack('<B', arg[start_index:start_index+1])[0]
    return False if b == 0 else True

def to_char(arg: bytes, start_index: int = 0) -> str:
    """
    Returns a char value converted from the byte at a specified position in a bytes.

    Parameters
    ----------
    arg : bytes
        A bytes object.
    start_index : int, optional
        The index of the byte within arg to convert.
    
    Returns
    -------
    value : str
        The char value formed by 1 byte beginning at start_index.
    """
    c = struct.unpack('<c', arg[start_index:start_index+1])[0]
    return c.decode()

def to_double(arg: bytes, start_index: int = 0) -> float:
    """
    Returns a double-precision floating-point value converted from 8 bytes at a specified position in a bytes.

    Parameters
    ----------
    arg : bytes
        A bytes object.
    start_index : int, optional
        The index of the byte within arg to convert.
    
    Returns
    -------
    value : float
        A double-precision floating-point value formed by 8 bytes beginning at start_index.
    """
    return struct.unpack('<d', arg[start_index:start_index+8])[0]

def to_int16(arg: bytes, start_index: int = 0) -> int:
    """
    Returns a 16-bit signed integer value converted from 2 bytes at a specified position in a bytes.

    Parameters
    ----------
    arg : bytes
        A bytes object.
    start_index : int, optional
        The index of the byte within arg to convert.
    
    Returns
    -------
    value : int
        A 16-bit signed integer value formed by 2 bytes beginning at start_index.
    """
    return struct.unpack('<h', arg[start_index:start_index+2])[0]

def to_int32(arg: bytes, start_index: int = 0) -> int:
    """
    Returns a 32-bit signed integer value converted from 4 bytes at a specified position in a bytes.

    Parameters
    ----------
    arg : bytes
        A bytes object.
    start_index : int, optional
        The index of the byte within arg to convert.
    
    Returns
    -------
    value : int
        A 32-bit signed integer value formed by 4 bytes beginning at start_index.
    """
    return struct.unpack('<i', arg[start_index:start_index+4])[0]

def to_int64(arg: bytes, start_index: int = 0) -> int:
    """
    Returns a 64-bit signed integer value converted from 8 bytes at a specified position in a bytes.

    Parameters
    ----------
    arg : bytes
        A bytes object.
    start_index : int, optional
        The index of the byte within arg to convert.
    
    Returns
    -------
    value : int
        A 64-bit signed integer value formed by 8 bytes beginning at start_index.
    """
    return struct.unpack('<q', arg[start_index:start_index+8])[0]

def to_single(arg: bytes, start_index: int = 0) -> float:
    """
    Returns a single-precision floating-point value converted from 4 bytes at a specified position in a bytes.

    Parameters
    ----------
    arg : bytes
        A bytes object.
    start_index : int, optional
        The index of the byte within arg to convert.
    
    Returns
    -------
    value : float
        A single-precision floating-point value formed by 4 bytes beginning at start_index.
    """
    f = struct.unpack('<f', arg[start_index:start_index+4])[0]
    return float('{:.7e}'.format(f))

def to_uint16(arg: bytes, start_index: int = 0) -> int:
    """
    Returns a 16-bit unsigned integer value converted from 2 bytes at a specified position in a bytes.

    Parameters
    ----------
    arg : bytes
        A bytes object.
    start_index : int, optional
        The index of the byte within arg to convert.
    
    Returns
    -------
    value : int
        A 16-bit unsigned integer value formed by 2 bytes beginning at start_index.
    """
    return struct.unpack('<H', arg[start_index:start_index+2])[0]

def to_uint32(arg: bytes, start_index: int = 0) -> int:
    """
    Returns a 32-bit unsigned integer value converted from 4 bytes at a specified position in a bytes.

    Parameters
    ----------
    arg : bytes
        A bytes object.
    start_index : int, optional
        The index of the byte within arg to convert.
    
    Returns
    -------
    value : int
        A 32-bit unsigned integer value formed by 4 bytes beginning at start_index.
    """
    return struct.unpack('<I', arg[start_index:start_index+4])[0]

def to_uint64(arg: bytes, start_index: int = 0) -> int:
    """
    Returns a 64-bit unsigned integer value converted from 8 bytes at a specified position in a bytes.

    Parameters
    ----------
    arg : bytes
        A bytes object.
    start_index : int, optional
        The index of the byte within arg to convert.
    
    Returns
    -------
    value : int
        A 64-bit unsigned integer value formed by 8 bytes beginning at start_index.
    """
    return struct.unpack('<Q', arg[start_index:start_index+8])[0]