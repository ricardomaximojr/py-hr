import tempfile
from hr import inventory
import spwd

def test_inventory_load():
    '''
    `inventory.load` takes file path
    and parses it as json
    '''
    inventory_file = tempfile.NamedTemporaryFile(delete=False)
    inventory_file.write(b'''
    [
        {
            "name": "kevin",
            "groups": ["sudo", "adm"],
            "password": "password_one"
        }
    ]
    ''')
    inventory_file.close()
    users_list = inventory.load(inventory_file.name)
    assert users_list[0] == {
        "name": "kevin",
        "groups": ["sudo", "adm"],
        "password": "password_one"
    }
def test_inventory_dump(mocker):
    '''
    `inventory.dump` take as dest path
    and optional list of users to export
    then exports the existing user info
    '''
    dest_file = tempfile.NamedTemporaryFile(delete=False)
    dest_file.close()

    # spwd.getspnam() cant be used by non-root user normally
    # mock the impl so that we can test
    mocker.patch(
        'spwd.getspnam',
        return_value=mocker.Mock(sp_pwd='password')
    )
    mocker.patch(
        'grp.getgrall',
        return_value=[
            mocker.Mock(gr_name='sudo', gr_member=['kevin', 'bob']),
            mocker.Mock(gr_name='adm', gr_member=['bob'])
        ]
    )

    inventory.dump(dest_file.name, ['kevin', 'bob'])

    with open(dest_file.name) as f:
        assert f.read() == '''[{"name": "kevin", "groups": ["sudo"], "password": "password" }, { "name": "bob", "groups": ["sudo", "adm"], "password": "password"}]'''
