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

def test_user_remove():
    pass
def test_user_update():
    pass
def test_user_sync():
    pass