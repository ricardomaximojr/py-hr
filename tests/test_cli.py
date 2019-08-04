import pytest
from hr import cli

@pytest.fixture()
def parser():
    return cli.create_parser()

# def test_parser_fails_without_arguments(parser):
#     '''
#     An error is raised if no arguments are passed to the parser
#     '''
#     with pytest.raises(SystemExit):
#         parser.parse_args([])

# def test_parser_succeeds_with_path(parser):
#     '''
#     No error is raise if a path is given an argument.
#     '''
#     with pytest.raises(SystemExit):
#         args = parser.parse_args(['/path/to/inventory.json'])
#         assert args.path == '/path/to/inventory.json'

def test_parser_export_flag(parser):
        '''
        The alternative usage of th CLI will be to pass a --export flag:
        $ hr --export path/to/inventory.json

        This --export flag won't take any arguments. Instead, you'll want to default
        the value of this field to False and set the value to True if the flag is present. Look at the action documentation to determine how you should go about doing this.

        Important: The export value is set to True if the --export flag is given.
        '''
        args = parser.parse_args(['/path/to/inventory.json'])
        assert args.export == False

        args = parser.parse_args(['--export', '/path/to/inventory.json'])
        assert args.export == True