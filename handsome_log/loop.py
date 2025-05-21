import itertools
import threading
import time
import sys
from datetime import timedelta

def loop_status(
    self,
    iterable,
    message="Processing",
    delay=0.1,
    show_spinner=True,
    show_percent=False,
    end_message="done ✓"
):
    """
    Displays a live terminal spinner while looping through an iterable.

    Args:
        iterable: The iterable to loop through.
        message: Text to show alongside the spinner.
        delay: Delay between frames (in seconds).
        show_spinner: Toggle spinner display.
        show_percent: Display progress as a percentage.
        end_message: Message displayed after loop completion.
    """
    spinner = itertools.cycle(["|", "/", "-", "\\"])
    stop = False
    total = len(iterable) if hasattr(iterable, '__len__') else None
    start_time = time.time()

    def spin():
        index = 0
        while not stop:
            spin_char = next(spinner) if show_spinner else ""
            percent_text = ""
            if show_percent and total:
                percent = int((index / total) * 100)
                percent_text = f" {percent:3d}%"
            sys.stdout.write(f"\r[{self.name}] {message}{percent_text} {spin_char}")
            sys.stdout.flush()
            time.sleep(delay)
            index += 1

        elapsed = timedelta(seconds=time.time() - start_time)
        elapsed_str = (
            str(elapsed).split(".")[0]
            if elapsed.total_seconds() > 60
            else f"{elapsed.total_seconds():.2f}s"
        )
        sys.stdout.write(
            f"\r[{self.name}] {message} {end_message} (Elapsed time: {elapsed_str})\n"
        )

    def wrapped():
        nonlocal stop
        t = threading.Thread(target=spin)
        t.daemon = True
        t.start()
        try:
            for i, item in enumerate(iterable):
                yield item
        finally:
            stop = True
            t.join()

    return wrapped()
