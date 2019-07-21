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
-------------------------------------------
::
    $ hr path/to/inventory.JSON
    Adding user 'kevin'
    Added user 'kevin'
    Updating user 'lisa'
    Updated user 'lisa'
    Removing user 'alex'
    Removed user 'alex'
