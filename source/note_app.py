import sys
import os

####
# Modify as you'd like
DEFAULT_DIR_NAME = 'notes'
DEFAULT_EDITOR = 'atom'
####

def get_args(argv):
    from argparse import ArgumentParser

    parser = ArgumentParser()
    add = parser.add_argument
    add('note_name', help='Name of note')
    add('-e', '--extension', help='Note extension', type=lambda x: x.lower(), default='txt')
    add('-d', '--directory', help='Directory Name', default=DEFAULT_DIR_NAME)
    add('-t', '--template', help='Use template', action='store_true')
    return parser.parse_args(argv[0].split(' '))

def join_str(names, char_str='/', char_at_end=False):
    joined_str = char_str.join(names)
    if char_at_end:
        joined_str += char_str
    return joined_str

def make_dir_if_not_exists(path):
    if not os.path.isdir(path):
        os.mkdir(path)

def main():
    args = get_args(sys.argv[1:])
    note_name = args.note_name
    note_ext = args.extension
    note_dir = args.directory
    use_template = args.template

    script_path = os.path.dirname(os.path.realpath(__file__))
    root_path = os.path.abspath(os.path.join(script_path, os.pardir))
    default_note_path = join_str([root_path, DEFAULT_DIR_NAME])
    template_path = join_str([root_path, 'templates'])

    make_dir_if_not_exists(default_note_path)

    sub_dir_path = None
    if note_dir != DEFAULT_DIR_NAME:
        sub_dir_path = join_str([default_note_path, note_dir])
        make_dir_if_not_exists(sub_dir_path)

    full_note_name = note_name + '.' + note_ext
    target_dir = sub_dir_path or default_note_path
    note_path = join_str([target_dir, full_note_name])

    with open(note_path, 'a+') as note:
        print('Creating note: {}'.format(note_name))
        if use_template:
            template = join_str([template_path, note_ext])
            if os.path.isfile(template):
                with open(template, 'r') as t:
                    note.writelines(t.readlines())

    osCommandString = join_str([DEFAULT_EDITOR, note_path], char_str=' ')
    os.system(osCommandString)

if __name__ == '__main__':
    main()
