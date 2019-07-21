User Management Python Package
==============================
github_token: b36844d6e2031f40149514efdfdd716c066f16fc

Python package to manage users on a server
based on an "inventory" JSON file.

Set up the project's directory structure and metadata
-----------------------------------------------------

1. Create a project folder called ``hr`` (short for human resources)
2. Set up the directories to put the project's source code and tests
3. Create the ``setup.py`` with metadata and package discovery
4. Utilize ``pipenv`` to create a virtualenv and Pipfile
5. Add ``pytest`` and ``pytest-mock`` as development dependencies
6. Set the project up in source control and make your initial commit

Ideal usage of the ``hr`` commands is this:
::
    $ hr path/to/inventory.json
    Adding user 'kevin'
    Added user 'kevin'
    Updating user 'lisa'
    Updated user 'lisa'
    Removing user 'alex'
    Removed user 'alex'

The alternative usage of th CLI will be to pass a ``--export`` flag:
::
    $ hr --export path/to/inventory.json
This ``--export`` flag won't take any arguments. Instead, you'll want to default
the value of this field to ``False`` and set the value to ``True`` if the flag is present. Look at the action documentation to determine how you should go about doing this.

For this exercise, Write a few tests before implementing the CLI parser. Ensure the following:

1. An error is raised if no arguments are passed to the parser.
2. No error is raise if a path is given an argument.
3. The ``export`` value is set to ``True`` if the ``--export`` flag is given.