import sys
import os

def main():
    import pdb
    pdb.set_trace()

    script_path = os.path.dirname(os.path.realpath(__file__))
    root_path = os.path.abspath(os.path.join(script_path, os.pardir))

    #### Edit as necessary
    ALLOWABLE_FILES = (
    '.py', '.txt', '.html', '.css'
    )
    DEFAULT_FILE_TYPE = '.txt'
    DEFAULT_NOTE_DIR_NAME = 'Notes'
    ####
    default_note_path = "{}/{}".format(root_path, DEFAULT_NOTE_DIR_NAME)

    qn_args = sys.argv[1:]
    note_args = qn_args[0].split(' ')

    def process_note_info(note_args):
        note_name = note_args.pop(0)
        file_type = DEFAULT_FILE_TYPE
        dir_name = DEFAULT_NOTE_DIR_NAME

        # If args still exists they are either file
        # extension, directory name, or both
        # otherwise use the defaults
        if note_args:
            if len(note_args) == 1:
                if note_args[0] in ALLOWABLE_FILES:
                    file_type = note_args[0]
                else:
                    dir_name = dir_name = note_args[0]
            else:
                file_type, dir_name = note_args[0], note_args[1]

        return (
            note_name, file_type, dir_name
            )

    note_name, file_type, dir_name = process_note_info(note_args)

    # Create dir and/or update target path
    target_path = default_note_path
    if dir_name != DEFAULT_NOTE_DIR_NAME:
        target_path = "{}/{}".format(default_note_path, dir_name)
        if not os.path.isdir(target_path):
            print('Creating dir named: {}'.format(dir_name))
            os.mkdir(target_path)
        else:
            print('Directory {} exists'. format(dir_name))
    elif os.path.isdir(target_path):
        os.mkdir(default_note_path)

    # Create the file in the directory
    pdb.set_trace()
    note_name_w_ext = "{}{}".format(note_name, file_type)
    full_note_path = "{}/{}".format(target_path, note_name_w_ext)
    f = open(full_note_path, 'a+')
    f.close()

    # Open the file
    osCommandString = "atom {}".format(full_note_path)
    os.system(osCommandString)

if __name__ == '__main__':
    main()
