#!/usr/bin/env python3

from ZeroSeg import screen
from ZeroSeg_API import app
from flask import request


def inrange(value: int, down_limit: int, top_limit: int) -> bool:
    if value in range(down_limit, top_limit + 1):
        return True
    else:
        return False


@app.route("/", methods=["POST"])
def root() -> dict:
    args = request.args

    # Verify if `position` is valid.
    if "char" in args or "byte" in args:
        if "position" in args:
            position = args["position"]
        else:
            position = 1

        try:
            if inrange(int(position), 1, 8):
                if "char" in args:
                    send_char(str(args["char"]), position)

                elif "byte" in args:
                    try:
                        byte = int(args["byte"], 0)
                        if inrange(byte, 0, 255):
                            send_byte(byte, position)

                    except ValueError:
                        return {"status": 406}

        except ValueError:
            return {"status": 406}

    if "text" in args:
        send_text(str(args["text"]))

    elif "number" in args:
        send_number(float(args["number"]))

    else:
        return {"status": 403}  # Forbidden


def send_text(text: str) -> dict:
    """
    Display text on screen. If content length is less or equal 8 then in
    use is `write_text` method, else `show_message` and displayed is scrolled
    text from right to left.
    """
    try:
        screen.write_text(text)
    # OverflowError is returned when message content is longer than 8 chars.
    except OverflowError:
        screen.show_message(text)

    return {"status": 200}


def send_number(num: float) -> dict:
    """
    Display any integer (rounded float) starting from right side of screen
    via `write_number` method. Similar as `send_text` function use `show_message`
    method when `OverflowError` is raised. Number is then converted to `str` type.
    """
    try:
        screen.write_number(num)
    except OverflowError:
        screen.show_message(str(num))

    return {"status": 200}


def send_char(char: str, position: int) -> dict:
    """
    Display any `str` type character using `write_char` method on
    any position if specified .
    """
    screen.write_char(char, position)

    return {"status": 200}


def send_byte(byte: int, position: int) -> dict:
    """
    Set any `int` byte value (range {0..255}) on any position if specified
    (default: 1). Function uses `set_byte` method.
    """
    if byte > 255 or byte < 0:
        return {"status": 406}
    else:
        screen.set_byte(byte, position)
        return {"status": 200}
