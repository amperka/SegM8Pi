"""This example demonstrates the outline of the available symbols on a
SegM8 module. Unavailable characters are displayed as underscore."""

import time
from string import ascii_letters, digits, punctuation
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
            # Display lowercase and uppercase letters.
            for letter in ascii_letters:
                print(letter)
                segm8_module.display_string(letter, 0, 1)
                time.sleep(1)
            # Display numbers.
            for number in digits:
                print(number)
                segm8_module.display_string(number, 0, 1)
                time.sleep(1)
            # Display punctuation characters.
            for symbol in punctuation:
                print(symbol)
                segm8_module.display_string(symbol, 0, 1)
                time.sleep(1)
    except KeyboardInterrupt:
        print("Exit")


if __name__ == "__main__":
    main()
