import gdb
import codecs
from datetime import datetime
import os

PRINT_LOG = True
REMOVE_LOGFILE = False
WRITE_LOGFILE = True
NOW = datetime.now().strftime("%Y%m%d%H%M%S")
LOGNAME = f"print_debug_breakpoint-{NOW}.log"

def delete_PDB_handler(event):
    if isinstance(event, PrintDebugBreakpoint):
        print(f"PrintDebugBreakpoint({event.expression}) deleted.")
        if REMOVE_LOGFILE and WRITE_LOGFILE and os.path.isfile(LOGNAME):
            print("Removing file...")
            os.remove(LOGNAME)
            print("Done.")

def exit_handler(event):
    if REMOVE_LOGFILE and WRITE_LOGFILE and os.path.isfile(LOGNAME):
        print("Removing file...")
        os.remove(LOGNAME)
        print("Done.")

class PrintDebugBreakpoint(gdb.Breakpoint):
    # r0 = gdb.selected_inferior().architecture().registers().find("r0")

    def stop(self):
        # IMPORTANT NOTE: If you ever want to use pwndbg.regs.<stuff> and other pwndbg.<stuff> here
        # and you "return False" here then you need to do
        # `pwndbg.events.after_reload(start=False)` first to reload the state!

        # maybe events.inferior_call could be used instead (would not block anything)
        log_string = gdb.execute("x/s $r0", to_string=True)
        processed_string = codecs.decode(log_string, "unicode-escape").lstrip('\t 0123456789xabcdef:').rstrip('" \n').lstrip('"')
        if WRITE_LOGFILE:
            with open(LOGNAME, "a") as file:
                file.write(processed_string + "\n")
        if PRINT_LOG:
            # print(log_string)
            print(processed_string)
        try:
            pwndbg.events.after_reload(start=False)
        except Exception:
            pass
        return False


PrintDebugBreakpoint("svcOutputDebugString")
gdb.events.breakpoint_deleted.connect(delete_PDB_handler)
gdb.events.exited.connect(exit_handler)
if WRITE_LOGFILE:
    print(f"Writing log to file: {LOGNAME}")
