import json
import grp
import spwd
from .helpers import user_names

def load(inventory_filename):
    with open(inventory_filename) as f:
        return json.load(f)
def dump(dest_filename, users_to_export_list=user_names()):
    users = []
    for user_name in users_to_export_list:
        password = spwd.getspnam(user_name).sp_pwd
        groups = _groups_for_user(user_name)
        users.append({
            'name': user_name,
            'groups': groups,
            'password': password
        })
    with open(dest_filename, 'w') as f:
        json.dump(users, f)
def _groups_for_user(user_name):
    return [g.gr_name for g in grp.getgrall() if user_name in g.gr_mem]
