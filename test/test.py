import bitconverter

if __name__ == '__main__':
    ##### any type -> bytes #####
    b_bool      = bitconverter.get_bytes_bool(True)                     # b'\x01'
    b_char      = bitconverter.get_bytes_char('?')                      # b'?'
    b_double    = bitconverter.get_bytes_double(1.2345678901234567)     # b'\xfbY\x8cB\xca\xc0\xf3?'
    b_int16     = bitconverter.get_bytes_int16(-1000)                   # b'\x18\xfc'
    b_int32     = bitconverter.get_bytes_int32(2147483647)              # b'\xff\xff\xff\x7f'
    b_int64     = bitconverter.get_bytes_int64(9223372036854775807)     # b'\xff\xff\xff\xff\xff\xff\xff\x7f'
    b_single    = bitconverter.get_bytes_single(3.4028235E+038)         # b'\xff\xff\x7f\x7f'
    b_uint16    = bitconverter.get_bytes_uint16(32767)                  # b'\xff\x7f'
    b_uint32    = bitconverter.get_bytes_uint32(2147483647)             # b'\xff\xff\xff\x7f'
    b_uint64    = bitconverter.get_bytes_uint64(9223372036854775807)    # b'\xff\xff\xff\xff\xff\xff\xff\x7f'

    ##### bytes -> any type #####
    bool    = bitconverter.to_bool(b_bool)      # True
    char    = bitconverter.to_char(b_char)      # ?
    double  = bitconverter.to_double(b_double)  # 1.2345678901234567
    int16   = bitconverter.to_int16(b_int16)    # -1000
    int32   = bitconverter.to_int32(b_int32)    # 2147483647
    int64   = bitconverter.to_int64(b_int64)    # 9223372036854775807
    single  = bitconverter.to_single(b_single)  # 3.4028235e+38
    uint16  = bitconverter.to_uint16(b_uint16)  # 32767
    uint32  = bitconverter.to_uint32(b_uint32)  # 2147483647
    uint64  = bitconverter.to_uint64(b_uint64)  # 9223372036854775807