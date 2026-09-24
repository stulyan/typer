# typer
A python script that types text character by character into software monitoring manual typing, with unicode, formatting, and randomized delays. Useful if you need to hide that you pasted something into a document lol
A simple python script that types text from `Text.txt` character by character into the active window.
As mentioned above, the script can help bypass protection based on version history. To start typing, place the cursor where you want the text to appear and run the script.

## Requirements

* Windows 10 / 11
* Python 3.10+

You can download Python 3.12 from the Microsoft Store.

After installation, check that Python is available:

```bash
python --version
```

**If the command displays the Python version, the installation was successful.**

**Next, install the required library. Open `cmd` using `Win + R` and run:**

```bash
pip install pydirectinput-rgx
```

## Preparation

Put the text you want to type into:

```text
Text.txt
```

**The `Text.txt` file must be saved using `UTF-8` encoding.**

## Running

1. Open a text editor or another application where you want to enter the text.
2. Place the cursor where you want the text to appear.
3. Run the script:

```bash
python main.py
```

**You can also right-click `main.py` and open it with python.**

4. During the `START_DELAY` period, switch to the target window and **do not close it until the typing is finished.**
5. The script will start typing the contents of `Text.txt`.

## Configuration

The main parameters are located at the beginning of `main.py`.

| **Variable**      | **Description**                          |
| ----------------- | ---------------------------------------- |
| `TEXT_FILE`       | Name of the text file                    |
| `START_DELAY`     | Delay before typing starts               |
| `CHAR_DELAY_MIN`  | Minimum delay between regular characters |
| `CHAR_DELAY_MAX`  | Maximum delay between regular characters |
| `PUNCT_DELAY_MIN` | Minimum delay after punctuation          |
| `PUNCT_DELAY_MAX` | Maximum delay after punctuation          |
| `ENTER_DELAY_MIN` | Minimum delay after line breaks          |
| `ENTER_DELAY_MAX` | Maximum delay after line breaks          |

## Warning

* Windows only!!
* The target window must remain active while typing.
* The target application must accept keyboard input.
* The script simply simulates manual keyboard input.

**Bugs may occur!**

## License

MIT
