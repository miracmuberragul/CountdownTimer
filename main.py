import time
import sys

def countdown_timer(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = f'{mins:02}:{secs:02}'  # Format the time as MM:SS
        sys.stdout.write(f'\r{timer}')  # Use sys.stdout.write to overwrite the line
        sys.stdout.flush()  # Ensure that the output is immediately updated
        time.sleep(1)  # Wait for 1 second
        seconds -= 1

    print("\nTime's up!")  # Move to the next line after the countdown

# Example: Countdown for 10 seconds
countdown_timer(10)