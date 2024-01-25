# bitconverter-py<!-- omit in toc -->
<img src="https://img.shields.io/badge/Python-3.9.5 or Later-blue?&logo=Python"> <img src="https://img.shields.io/badge/License-MIT-green">

C#における[BitConverterクラス](https://learn.microsoft.com/en-us/dotnet/api/system.bitconverter?view=net-8.0)に相当する一部の機能をPythonでも使用するためのパッケージです。
一部のよく使用するであろう機能のみ作成しています。
また、一部の関数は表現方法がC#とは異なります (内容は同じです)。


# Table Of Contents <!-- omit in toc -->
<details>
<summary>Details</summary>

- [Environment](#environment)
- [Installation](#installation)
- [Description](#description)
  - [Cheat sheet: Any type -\> Bytes](#cheat-sheet-any-type---bytes)
  - [Cheat sheet: Bytes -\> Any type](#cheat-sheet-bytes---any-type)
- [References](#references)
- [Troubleshooting](#troubleshooting)
- [Versions](#versions)
- [Author](#author)
- [License](#license)
</details>


# Environment
- Python 3.9.5 or later

# Installation
追加で必要なパッケージ等はありません。

# Description
structモジュールを使用しているだけです。
以下のテーブルを参照し、必要なものだけを自身のスクリプトに組み込んでも問題ありません。

## Cheat sheet: Any type -> Bytes
| C# type | .NET type | Python type | To byte array C# | To bytes Python | this package |
| ---- | ---- | ---- | ---- | ---- | ---- |
| bool | System.Boolean | bool | `BitConverter.GetBytes(Boolean)` | `struct.pack('<?', value)` | `get_bytes_bool(value)` |
| char | System.Char | 長さ1のバイト列 | `BitConverter.GetBytes(Char)` | `struct.pack('<c', value)` | `get_bytes_char(value)` |
| double | System.Double | float | `BitConverter.GetBytes(Double)` | `struct.pack('<d', value)` | `get_bytes_double(value)` |
| short | System.Int16 | int (64ビットなので等価ではない) | `BitConverter.GetBytes(Int16)` | `struct.pack('<h', value)` | `get_bytes_int16(value)` |
| int | System.Int32 | int (64ビットなので等価ではない) | `BitConverter.GetBytes(Int32)` | `struct.pack('<i', value)` | `get_bytes_int32(value)` |
| long | System.Int64 | int | `BitConverter.GetBytes(Int64)` | `struct.pack('<q', value)` | `get_bytes_int64(value)` |
| float | System.Single | float (64ビットなので等価ではない) | `BitConverter.GetBytes(Single)` | `struct.pack('<f', value)` | `get_bytes_single(value)` |
| ushort | System.UInt16 | int (64ビットなので等価ではない) | `BitConverter.GetBytes(UInt16)` | `struct.pack('<H', value)` | `get_bytes_uint16(value)` |
| uint | System.UInt32 | int (64ビットなので等価ではない) | `BitConverter.GetBytes(UInt32)` | `struct.pack('<I', value)` | `get_bytes_uint32(value)` |
| ulong | System.UInt64 | int (符号付き) | `BitConverter.GetBytes(UInt64)` | `struct.pack('<Q', value)` | `get_bytes_uint64(value)` |

## Cheat sheet: Bytes -> Any type
| C# type | .NET type | Python type | To any type C# | To any type Python | this package |
| ---- | ---- | ---- | ---- | ---- | ---- |
| bool | System.Boolean | bool | `BitConverter.ToBoolean(ReadOnlySpan<Byte>)` | `struct.unpack('<?', value)` | `to_bool(value, start_index)` |
| char | System.Char | 長さ1のバイト列 | `BitConverter.ToChar(ReadOnlySpan<Byte>)` | `struct.unpack('<c', value)` | `to_char(value, start_index)` |
| double | System.Double | float | `BitConverter.ToDouble(ReadOnlySpan<Byte>)` | `struct.unpack('<d', value)` | `to_double(value, start_index)` |
| short | System.Int16 | int (64ビットなので等価ではない) | `BitConverter.ToInt16(ReadOnlySpan<Byte>)` | `struct.unpack('<h', value)` | `to_int16(value, start_index)` |
| int | System.Int32 | int (64ビットなので等価ではない) | `BitConverter.ToInt32(ReadOnlySpan<Byte>)` | `struct.unpack('<i', value)` | `to_int32(value, start_index)` |
| long | System.Int64 | int | `BitConverter.ToInt64(ReadOnlySpan<Byte>)` | `struct.unpack('<q', value)` | `to_int64(value, start_index)` |
| float | System.Single | float (64ビットなので等価ではない) | `BitConverter.ToSingle(ReadOnlySpan<Byte>)` | `struct.unpack('<f', value)` | `to_single(value, start_index)` |
| ushort | System.UInt16 | int (64ビットなので等価ではない) | `BitConverter.ToUInt16(ReadOnlySpan<Byte>)` | `struct.unpack('<H', value)` | `to_uint16(value, start_index)` |
| uint | System.UInt32 | int (64ビットなので等価ではない) | `BitConverter.ToUInt32(ReadOnlySpan<Byte>)` | `struct.unpack('<I', value)` | `to_uint32(value, start_index)` |
| ulong | System.UInt64 | int (符号付き) | `BitConverter.ToUInt64(ReadOnlySpan<Byte>)` | `struct.unpack('<Q', value)` | `to_uint64(value, start_index)` |

本パッケージの関数の `start_index` はデフォルトで0です。
そのため、例えば `BitConverter.ToBoolean(ReadOnlySpan<Byte>)` と `to_bool(value)` は同等です。
開始インデックスを指定する場合、 `BitConverter.ToBoolean(Byte[], Int32)` と同等となります。

# References
- [C# BitConverter Class](https://learn.microsoft.com/en-us/dotnet/api/system.bitconverter?view=net-8.0)
- [Python struct](https://docs.python.org/3/library/struct.html)

# Troubleshooting


# Versions
- 1.0: 2024/1/25

# Author
- Takayoshi Hagiwara
    - Graduate School of Media Design, Keio University
    - Toyohashi University of Technology


# License
- MIT License