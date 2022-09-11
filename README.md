# switch_debug_utils

Small collection of scripts and other utilities I use to debug stuff on the switch

## Contents

- [gdb_scripts](gdb_scripts/)
- [dkp-gdb-py3](dkp-gdb-py3/) contains `PKGBUILD` files for devkitA64-gdb and devkitARM-gdb with python3 support
- [ipc_utils](ipc_utils/) contains convenience scripts to make it easier to deal with IPC buffers

## Resources

Useful resources for debugging switch stuff:

- [switch-gdb-cheatsheet](https://gist.github.com/jam1garner/c9ba6c0cff150f1a2480d0c18ff05e33)
- [pwndbg](https://github.com/pwndbg/pwndbg) - makes gdb debugging a bit nicer

- [switchbrew](https://switchbrew.org/)
  - [Title list](https://switchbrew.org/wiki/Title_list) - especially useful when debugging sysmodules
- [Atmosphère](https://github.com/Atmosphere-NX/Atmosphere) - can often be used as a reference
  - [ams_mitm](https://github.com/Atmosphere-NX/Atmosphere/tree/master/stratosphere/ams_mitm/source) - best reference for mitm sysmodules
- [Switch system update reports](https://yls8.mtheall.com/ninupdates/titlelist.php?sys=hac)
  - I often use the `swipcgen_server_modern.info` files for reversing sysmodules or to create a mitm sysmodule
