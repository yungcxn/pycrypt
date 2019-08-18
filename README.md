# pycrypt

A CLI-based tool to en- and decrypt strings.  

Usage:  

```
$ python pycrypt.py [-d/-e] [filepath.txt] [-o] [filepath]
```  



Parameter | What it does
--- | ---
-d | decrypt `filepath`
-e | encrypt `filepath`
filepath | `path/to/file.txt`
-o | optional, output also to file `filepath`  


After that you will be asked which algorithm to choose of.


### Requirements  

These modules need to be installed also via:
`$ pip install des`



These are the already implemented algorithms:  

  1. base64
  2. base32
  3. base16
