import subprocess
import pwd

def add(user_dict):
    print(f"adding user '{user_dict['name']}'")
    subprocess.call([
        'useradd',
        '-p',
        user_dict['password'],
        '-G',
        _groups_str(user_dict),
        user_dict['name']
    ])
def remove(user_dict):
    print(f"Removing user '{user_dict['name']}'")
    subprocess.call([
        'userdel',
        '-r',
        user_dict['name']
    ])
def update(user_dict):
    print(f"updating user '{user_dict['name']}")
    subprocess.call([
        'usermod',
        '-p',
        user_dict['password'],
        '-G',
        _groups_str(user_dict),
        user_dict['name']
    ])
def sync(user_list, existing_usernames=None):
    username_list = [user['name'] for user in user_list]
    existing_usernames = (existing_usernames or _usernames())
    for user in user_list:
        if user['name'] not in existing_usernames:
            add(user)
        elif user['name'] in existing_usernames:
            update(user)
    for username in existing_usernames:
        if not username in username_list:
            remove({'name': username})
def _groups_str(user_dict):
    return ','.join(user_dict['groups'] or [])
def _usernames():
    return [user.pw_name for user in pwd.getpwall()
            if user.pw_uid >= 1000 and 'home' in user.pw_dir]
