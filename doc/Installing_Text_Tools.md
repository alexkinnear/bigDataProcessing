# Using the Text Tools with Assignment #2

You have created your own text processing tools, which increases your power as
a programmer in two ways:

1.  You have a suite of useful commands that let you process large amounts of
    text more easily than with an editor
2.  You have gained much knowledge about processing textual data.

You can use your own text tools to get a handle on your next assignment.  Or,
you can use the text tools that come with the Bash shell.  Each of the commands
that `tt.py` takes corresponds to a classic Unix text-processing program.
These programs have more options than yours, and are likely faster.

On the other hand, your Text Tools have the advantage of being flexible: you
can add to or change them as the need arises.  For this reason you should make
them available for use anywhere on your system.


## How to install your Text Tools

While you were working on Assignment 1 your shell had to be in the project
directory to run `tt.py`.  Further, when you ran the program you had to type
`python tt.py` to launch it.

This document explains how to "install" your Text Tools so that you can run
`tt.py` from *anywhere* on your system without needing to also type `python` in
the command line.


### Update $PATH in ~/.bash_profile

In order for `bash` to find `tt.py` on your system, you need to add its
location to the shell's search path.

1. Open a bash shell
2. Change into the `src/` directory containing `tt.py`
3. Run `pwd` to print the absolute path of this directory
4. Open the file `~/.bash_profile` in a proper text editor (i.e. PyCharm, *not*
   notepad or wordpad)
5. Add this line to the bottom of `~/.bash_profile`, replacing `<TEXTTOOLS_DIR>`
   with the path from step 3

```
PATH=<TEXTTOOLS_DIR>:$PATH
```

If the path to `tt.py` reported by `pwd` contains spaces (e.g. because your
Windows username contains spaces), you'll need to "escape" them by adding a
single backslash `\` in front of each one.



### Test it out

1.  Open a new bash window
2.  Run `tt.py`.  You should see its usage message and not a "command not
    found" error.




## Troubleshooting

### bash: tt.py: command not found

This error indicates that the directory containing `tt.py` is not correctly
specified in your `PATH`.

*   Launch a new bash window and try again.  The bash shell reads this file
    once upon startup; changes made to it don't automatically affect instances
    of bash that are already running.
*   Double-check the spelling of the directory containing `tt.py` within `~/.bash_profile`.
*   The path to `tt.py` should end in `src`.
*   If the path to `tt.py` on your system contains spaces, make sure they are
    properly escaped with backslashes `\`.


### No such file or directory

Errors messages containing these words look like the following:

```
/usr/bin/env: 'python': No such file or directory
```

```
bash: /c/Users/user/Desktop/cs1440-falor-erik-assn1/src/caesar.py: /usr/bin/env: bad interpreter: No such file or directory
```

The remedy is to update the shebang line in `tt.py`.  The first line of `tt.py`
looks like this:

```
#!/usr/bin/env python
```

This line tells the bash shell which programming language to run the contents
of that file in.  The name "shebang" is short for "hash-bang" and refers to the
first two characters of the file.

The shebang line I provided *should* work for most systems.  When it doesn't,
you'll get one of the above error messages.  If this happens to you, replace
my shebang line with the location of the Python interpreter on your system.

1.  Find your python interpreter by running `which python`.  If you need to
    specifically run your code with `python3`, use `which python3`.
2.  Replace the entire first line of `tt.py` with a new line that begins with
    `#!` followed by the path returned by `which`.  The result will look
    something like this if you're using Git+Bash on Windows:
    `#!/c/Users/user/AppData/Local/Programs/Python/Python37/python`



### stdout is not a tty

If you're a Windows user you may see this error when you try to redirect the
output of `tt.py` to a file instead of the screen.

Because of the way that Python interacts with the terminal installed by
Git+Bash, I had you create an alias for the `python` program that runs it
through another program called `winpty`.  This enables you to use the Python
REPL from the command line, but breaks the ability to redirect the output of
your text tools to a file.

You can approach this three ways:

1.  Suppress the winpty+python alias on an as-needed basis with a backslash.
    Each time you run Python you have the choice to use `winpty` or not:

    $ \python src/tt.py head -n 10 README.md > testfile


2.  Remove the alias from your terminal for the rest of the session.  You need do this only once each time you open a terminal window:

    $ unalias python
    $ python src/tt.py head -n 10 README.md > testfile


3.  Remove the alias from the `.bash_profile` file in your home directory.
    You'll need to find and open that file in a proper text editor; PyCharm
    will work just fine for this.  Whenever you want to run the Python REPL
    from the bash shell you'll need to remember to first type `winpty` before
    `python` to prevent it from hanging.
