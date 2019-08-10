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
def test_user_sync():
    pass