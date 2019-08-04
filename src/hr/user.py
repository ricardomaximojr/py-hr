import subprocess

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
def _groups_str(user_dict):
    return ','.join(user_dict['groups'] or [])