import sys

from setuptools import setup

NAME = 'pyls'
SCRIPT = 'pyls.bat'


def main():
    if 'py2exe' in sys.argv:
        import py2exe
    version = __import__(NAME).__version__
    setup(
        name=NAME,
        version=version,
        entry_points={
            'console_scripts': [
                'pyls=pyls.main.main',
            ],
        },
        author='Jonathan Hartley',
        author_email='tartley@tartley.com',
        url='https://github.com/tartley/pyls',
        license='New BSD License',
    )


if __name__ == '__main__':
    main()

