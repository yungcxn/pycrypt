# pycrypt

A CLI-based tool to en- and decrypt strings.

Usage:

```
$ python3 pycrypt.py [-d/-e] [filepath.txt] [-o] [filepath]
```



Parameter | What it does
--- | ---
-d | decrypt `filepath`
-e | encrypt `filepath`
filepath | `path/to/file.txt`
-o | optional, output also to file `filepath`

After that you will be asked which algorithm to choose of.

### Requirements

You need to have Python at least at version `3.4`.
The newest Python3 version is highly recommended.

These are the already implemented algorithms:
