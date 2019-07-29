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
        python_requires="<3.0.0",
        packages=['pyls'],
        entry_points={
            'console_scripts': [
                'pyls=pyls.main:main',
            ],
        },
        author='Jonathan Hartley',
        author_email='tartley@tartley.com',
        url='https://github.com/tartley/pyls',
        license='New BSD License',
        classifiers=[
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.7',
        ],
    )


if __name__ == '__main__':
    main()

