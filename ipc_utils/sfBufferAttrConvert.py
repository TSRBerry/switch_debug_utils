#!/usr/bin/env python3
from enum import IntFlag
import argparse

# Source: https://github.com/switchbrew/libnx/blob/62755bebe0ef0e90ae4918a96fe5334da64bec94/nx/include/switch/sf/service.h#L20-L29
class SfBufferAttrs(IntFlag):
    SfBufferAttr_In                             = 0
    SfBufferAttr_Out                            = 1
    SfBufferAttr_HipcMapAlias                   = 2
    SfBufferAttr_HipcPointer                    = 3
    SfBufferAttr_FixedSize                      = 4
    SfBufferAttr_HipcAutoSelect                 = 5
    SfBufferAttr_HipcMapTransferAllowsNonSecure = 6
    SfBufferAttr_HipcMapTransferAllowsNonDevice = 7

    @classmethod
    def find_attrs(self, type_num: int) -> list:
        return [self(flag) for flag, bit in zip(range(8), reversed(f'{type_num:0>8b}')) if bool(int(bit))]


def hextype(string) -> int:
    if string.startswith("0x"):
        return int(string, 16)
    else:
        return int(string)

parser = argparse.ArgumentParser()
parser.add_argument("type_num", type=hextype, nargs="+", help="hex value(s) that should be converted")
args = parser.parse_args()

first_num = True
for type_num in args.type_num:
    if not first_num:
        print()
    else:
        first_num = False
    print(f"{hex(type_num)} -> {f'{type_num:0>8b}'}")
    print(f"{{{' | '.join([x.name for x in SfBufferAttrs.find_attrs(type_num)])}}}")
