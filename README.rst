User Management Python Package
==============================

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

Create a module in your package to work
with user information. You'll want to be able
to do the following:

1. Received a list of user dictionaries and
   ensure that the system's user match.
2. Have a function that can create a user
   with given information if no user exists
   by that name 
3. Have a function that can update a user
   based on a user dictionary
4. Have a function that can remove a user
   with a given username
5. The create, update, and remove functions
   should print that they are creating/updating/Removing
   the user before executing the command

User info form:
{
    'name': 'kevin',
    'groups': ['wheel', 'dev']
    'password': '$6$HXdlMJqcV8LZ1DIF$LCXVxmaI/ySqNtLI6b64LszjM0V5AfD.ABaUcf4j9aJWse2t3Jr2AoB1zZxUfCr8SOG0XiMODVj2ajcQbZ4H4/'
} 
The password values will be SHA512 encrypted.
Hint: generate encrypted password in Python that is usable with usermod -p with:
import crypt
crypt.crypt('password', crypt.mksalt(crypt.METHOD_SHA512))

User Inventory Parsing and Exporting
====================================

Package for interacting with the user inventory file.
Inventory file holds user information.

Module needs to implement:
--------------------------
1.  function to read given inventory file,
    parse the JSON, and
    return a list of user dictionaries
2.  function that takes a path, and
    produces inventory file based on the
    current state of the system
    An optional parameter could be
    the specific users to export

Related Python modules
----------------------
`json`  - interact with JSON from Python
`grp`   - Group database
`pwd`   - Password/user database
`spwd`  - Shadow password database.
          (Used to get current encrypted password)

Example inventory JSON file:
::
    [
    {
        "name": "kevin",
        "groups": ["wheel", "dev"],
        "password": "$6$HXdlMJqcV8LZ1DIF$LCXVxmaI/ySqNtLI6b64LszjM0V5AfD.ABaUcf4j9aJWse2t3Jr2AoB1zZxUfCr8SOG0XiMODVj2ajcQbZ4H4/"
    },
    {
        "name": "lisa",
        "groups": ["wheel"],
        "password": "$6$HXdlMJqcV8LZ1DIF$LCXVxmaI/ySqNtLI6b64LszjM0V5AfD.ABaUcf4j9aJWse2t3Jr2AoB1zZxUfCr8SOG0XiMODVj2ajcQbZ4H4/"
    },
    {
        "name": "jim",
        "groups": [],
        "password": "$6$HXdlMJqcV8LZ1DIF$LCXVxmaI/ySqNtLI6b64LszjM0V5AfD.ABaUcf4j9aJWse2t3Jr2AoB1zZxUfCr8SOG0XiMODVj2ajcQbZ4H4/"
    }
    ]

Hint:
-----
Rely on mocking to make interactions with modules like
`grp`, `pwd`, and `spwd` consistent