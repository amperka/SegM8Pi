# SegM8Pi API

## class SegM8

Create an object of type `SegM8` to communicate with a chain of a particular [SegM8 7-segment
indicator modules](https://my.amperka.com/modules/SegM8).

### `SegM8(pin_CE: int, device_count: int = 1)`

Construct a new SegM8 object that uses the default hardware SPI bus (SPI0).

Parameters:

- `pin_CE`: the chip enable (also known as chip select or slave select) pin used to control the
  shift-register latch. It can take the values **0** or **1**, which corresponds to the **CE0** or
  **CE1** pins on the Raspberry Pi board.
- `device_count`: the number of SegM8 modules connected in a daisy-chain. If omitted, defines
  a single module.

### `clear() -> None`

Sets all module segments to the "dark" state. Clear the internal buffer.

### `display_int(number: int, position: int, width: int, align: int = segm8.Align.RIGHT, pad_zeros: bool = False, radix: int = segm8.NumberSystem.DEC) -> None`

Prints a `number` of type **int** of a fixed `width` starting with the `position` to the output
buffer. Moves the contents of the buffer to the indicator daisy-chain.

Parameters:

- `number`: integer number.
- `position`: starting position of the output of a number in the internal buffer.
- `width`: the number of elements in the internal buffer, and accordingly the number of SegM8
  modules needed to display a number.

Optional parameters:

- `align`: output alignment method: `segm8.Align.RIGHT` – align to the right corner (default state),
  `segm8.Align.LEFT` – align to the left corner.
- `pad_zeros`: add leading zeros before the number. Compatible only with `segm8.Align.RIGHT`.
- `radix`: number system. Determines in which number system the output will be presented:
  `segm8.NumberSystem.DEC` – decimal, `segm8.NumberSystem.HEX` – hexadecimal (compatible only with
  non-negative numbers).

### `display_float(number: float, position: int, width: int, precision: int = 1, align: int = segm8.Align.LEFT, pad_zeros: bool = False) -> None`

Prints a `number` of type **float** of a fixed `width` starting with the `position`to the output
buffer using formatting `flags`. The `precision` determines the number of digits to be printed after
the decimal point. Moves the contents of the buffer to the indicator daisy-chain.
Note: the `.` sign does not occupy a separate module and is displayed with the previous character.

Parameters:

- `number`: floating point number.
- `position`: starting position of the output of a number in the internal buffer.
- `width`: the number of elements in the internal buffer, and accordingly the number of SegM8
  modules needed to display a number.

Optional parameters:

- `precision`: decimal places count of float.
- `align`: output alignment method: `segm8.Align.RIGHT` – align to the right corner,
  `segm8.Align.LEFT` – align to the left corner (default state).
- `pad_zeros`: add leading zeros before the number. Compatible only with `segm8.Align.RIGHT`.

### `display_string(string: str, position: int, width: int, align: int = segm8.Align.LEFT) -> None`

Prints a `string` of a fixed `width` starting with the `position` to the output buffer using
formatting `flags`. Moves the contents of the buffer to the indicator daisy-chain.
Note: the `.` sign does not occupy a separate module and is displayed with the previous character.

When printing text strings, the interpretation of characters in indicator segments is used. Instead
of unsupported characters (e.g. **K, M, V, W, X, Z**) an overline is displayed (segment a).

Parameters:

- `string`: text line.
- `position`: starting position of the output of a string in the internal buffer.
- `width`: the number of elements in the internal buffer, and accordingly the number of SegM8
  modules needed to display a number or a text.

Optional parameter:

- `align`: output alignment method: `segm8.Align.RIGHT` – align to the right corner,
  `segm8.Align.LEFT` – align to the left corner (default state).

### `write_segments(mask: List[bool], device_index: int) -> None`

Displays a custom symbol in the specified position.

- `mask` - list of boolean values for all 8 segments. The ordinal number of the member of this list
  corresponds to the letter index of a indicator segment: 0-a, 1-b, <...>, 7-h(dot).
- `device_index`: A SegM8 device ordinal number in the daisy-chain. Can be in the range
  [0 .. device_count - 1].
