from argparse import ArgumentParser, Action

class ExportAction(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        export = values
        namespace.export = export.lower()

def create_parser():
    '''
    The alternative usage of th CLI will be to pass a --export flag:
        $ hr --export path/to/inventory.json

    This --export flag won't take any arguments. Instead, you'll want to default
    the value of this field to False and set the value to True if the flag is present. Look at the action documentation to determine how you should go about doing this.

    Important: The export value is set to True if the --export flag is given.
    '''
    
    parser = ArgumentParser()
    parser.add_argument(
        'path',
        help='the path to the inventory JSON file'
    )
    parser.add_argument(
        '--export', '-e',
        action='store_true'
    )
    return parser
def main():
    from hr import inventory, user

    args = create_parser().parse_args()
    if args.export:
        inventory.dump(args.path)
    else:
        users_info = inventory.load(args.path)
        user.sync(users_info)
        