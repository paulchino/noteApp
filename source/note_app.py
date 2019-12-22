import sys
import os

ALLOWABLE_FILES = (
'.py', '.txt', '.html', '.css', '.sh'
)
DEFAULT_DIR_NAME = 'notes'
DEFAULT_EDITOR = 'atom'

def get_args(argv):
    from argparse import ArgumentParser, ArgumentTypeError

    def allowable_ext_types(v):
        v = v.lower()
        if v not in ALLOWABLE_FILES:
            raise ArgumentTypeError('Not an allowable extension')
        else:
            return v

    parser = ArgumentParser()
    add = parser.add_argument
    add('note_name', help='Name of note')
    add('-e', '--extension', help='Note extension', type=allowable_ext_types, default='.txt')
    add('-d', '--directory', help='Directory Name', default=DEFAULT_DIR_NAME)
    # TODO: Add template option
    return parser.parse_args(argv[0].split(' '))

def main():
    args = get_args(sys.argv[1:])

    script_path = os.path.dirname(os.path.realpath(__file__))
    root_path = os.path.abspath(os.path.join(script_path, os.pardir))
    default_note_path = "{}/{}".format(root_path, DEFAULT_DIR_NAME)

    def _make_dir_if_not_exists(path):
        if not os.path.isdir(path):
            os.mkdir(path)

    _make_dir_if_not_exists(default_note_path)

    sub_dir_path = None
    if args.directory != DEFAULT_DIR_NAME:
        sub_dir_path = "{}/{}".format(default_note_path, args.directory)
        _make_dir_if_not_exists(sub_dir_path)

    full_note_name = args.note_name + args.extension
    target_dir = sub_dir_path or default_note_path
    note_path = '{}/{}'.format(target_dir, full_note_name)

    with open(note_path, 'a+') as f:
        print('Creating note: {}'.format(args.note_name))

    # Open the file
    osCommandString = "{} {}".format(DEFAULT_EDITOR, note_path)
    os.system(osCommandString)

if __name__ == '__main__':
    main()
