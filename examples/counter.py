"""This example demonstrates a simple countdown."""

import time
import segm8


def main():
    # Chip Enable pin. Set it to 0 or 1, depending on the connections.
    pin_CE = 0
    # The number of Segm8 modules used.
    device_count = 1
    # Create an object for working with the Segm8 module.
    segm8_module = segm8.SegM8(pin_CE, device_count)
    print("Program started. Press Ctrl-C to exit.")
    try:
        while True:
            # Display numbers from 9 to 0.
            for number in range(9, -1, -1):
                segm8_module.display_int(number, 0, 1)
                time.sleep(1)
    except KeyboardInterrupt:
        print("Exit")


if __name__ == "__main__":
    main()
