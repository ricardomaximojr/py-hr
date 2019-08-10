import pytest
import subprocess
from hr import user

# encrypted password123
password = '$6FMi11BJFsAc'
user_dict = {
    'name': 'kevin',
    'groups': ['sudo', 'adm'],
    'password': password
}
def test_user_add(mocker):
    '''
    user.add() use useadd command
    to create user with password
    and groups
    '''
    mocker.patch('subprocess.call')
    user.add(user_dict)
    subprocess.call.assert_called_with([
        'useradd',
        '-p',
        password,
        '-G',
        'sudo,adm',
        'kevin',
    ])
def test_user_remove(mocker):
    '''
    user.remove use userdel command
    to delete the user
    '''
    mocker.patch('subprocess.call')
    user.remove(user_dict)
    subprocess.call.assert_called_with([
        'userdel',
        '-r',
        'kevin'
    ])
def test_user_update(mocker):
    '''
    user.update use `usermod` command to 
    set the group and password of the user
    '''
    mocker.patch('subprocess.call')
    user.update(user_dict)
    subprocess.call.assert_called_with([
        'usermod',
        '-p',
        password,
        '-G',
        'sudo,adm',
        'kevin'
    ])
def test_user_sync(mocker):
    '''
    Given a list of user dictionaries, `user.sync(...)`
    should create missing users,
    remove extra non-system users,
    and update existing users.
    A list of existing usernames can be passed in
    or default users will be used.
    '''
    existing_usernames = ['kevin', 'ric']
    users_info = [
        {
            'name': 'krizelle',
            'groups': ['sudo'],
            'password': password
        },
        {
            'name': 'kevin',
            'groups': ['sudo', 'adm'],
            'password': password
        }
    ]
    mocker.patch('subprocess.call')
    user.sync(users_info, existing_usernames)
    subprocess.call.assert_has_calls([
        mocker.call([
            'useradd',
            '-p',
            password,
            '-G',
            'sudo',
            'krizelle'
        ]),
        mocker.call([
            'usermod',
            '-p',
            password,
            '-G',
            'sudo,adm',
            'kevin'
        ]),
        mocker.call([
            'userdel',
            '-r',
            'ric'
        ])
    ])