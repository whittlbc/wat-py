import code
import inspect


def wat():
  # Get our current frame
  curr_frame = inspect.currentframe()

  try:
    # Get previous frame (caller)
    calling_frame = curr_frame.f_back

    # Create merged dict of globals() with locals() from previous frame
    calling_vars = calling_frame.f_globals.copy()
    calling_vars.update(calling_frame.f_locals)

    # Enter interactive console
    code.interact(local=calling_vars,
                  banner='(wat Interactive Console)')
  finally:
    del curr_frame
