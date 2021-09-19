# Elycrypt
## _A simple encryptor/decryptor_

Elycrypt is a simple encryptor/decryptor written in Python 3

- Color output
- Linux/MacOs/Windows
- Command line based

## Installation

Elycrypt requires [Python](https://www.python.org/) v3+ to run.

Install the dependencies with pip :

**MacOs/Linux**
```sh
pip install termcolor
```

**Windows**
```sh
py - m pip install termcolor
```

## Run

**With cmd:**

```sh
python elycrypt.py
```

**With args:**

```sh
python elycrypt.py -eF a.txt -o output.txt
```

```sh
python elycrypt.py -dS "^^}U^]^U^^|U-----=====^:::::^}" -k "1.0|3|10|3|$|@@@@@"
```

[-eF] encryptionFilePath
[-dF] decryptionFilePath
[-eS] encryptionFileString
[-dS] decryptionFileString
[-o] outputPath
[-k] key


## License

MIT

**Free to use !**
