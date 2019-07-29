List the content and structure of a Python project

Only tested on Microsoft Windows and Python 2.7

Docs and download: http://pypi.python.org/pypi/pyls
Source code: https://github.com/tartley/pyls


# Usage

    pyls [<dir1> [, <dir2>...] ]


Produces a listing of the python project in directly <dir>, or else in the
current directory if none given, in the following format::

    package
        subpackage
            module1.py
                ClassA
                ClassB
            module2.py
                ClassC
        module3.py
            ClassD

# Known Issues

Pyls works by importing every module it finds in the given directories, and
enumerating the classes defined by importing that module. If you are doing
anything cleverer than defining static classes in regular modules, then pyls
will probably barf on it.


# Thanks

To Susan for putting up with my googly-eyed coding frenzies.

