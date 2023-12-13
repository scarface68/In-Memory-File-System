# Inito-Memory-File-System

**Language used** : Python

__Modules used__:
os, shutil, unittest

Run these commands if you dont already have them
```
pip install os
pip install shutil
pip install unittest
```

How to Run and Test
-
To run the project locally

- clone this repo using
```
git clone git@github.com:scarface68/Inito-Memory-File-System.git
```
or
```
git clone https://github.com/scarface68/Inito-Memory-File-System.git
```

- install the modules mentioned earlier (they all come pre-installed with python3)

- Run the main.py file using
```
python3 main.py
```

- To run the pre-designed unit tests
```
python3 Tests.py
```

Operations Implemented
-

- mkdir
- cd
- ls  (**Bonus**: added -a flag to view hidden files)
- touch
- echo (**Bonus**: handles both > and >>. Also handles line break '\n' with -e flag)
- cat
- rm (add -rf flag to remove directories)
- mv
- cp (add -r or -R flag to copy directories)
- grep (**Bonus**: added -i, -w, and -c flag. The flags are used to ignore case, match whole words and print only count of occurrence respectively)
- clear (nobody likes a messy terminal)
- pwd
- exit (exit code to break the infinite loop)

All the flags added serve similar purpose as inside of a terminal. 

**The error messages are also exactly similar to a terminal for all cases.**

__There are 3 files:-__

1. main.py - entry of the program, input is taken here and based on the input different methods of the filesystem class are called.

2. filesystemclass.py - contains the FileSystem class and basically does everything

3. Tests.py - contains 10 tests implemented using unittest module






