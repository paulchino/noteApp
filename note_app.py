import sys
import os

def main():
    import pdb
    #  Add types as necessary
    ALLOWABLE_FILES = (
        '.py', '.txt', '.html', '.css'
    )
    dir_path = os.path.dirname(os.path.realpath(__file__))
    DEFAULT_FILE_TYPE = '.txt'
    DEFAULT_DIR_NAME = "Notes"
    DEFAULT_NOTE_PATH = "{}/{}".format(dir_path, DEFAULT_DIR_NAME)
    qn_args = sys.argv[:]

    python_script = qn_args.pop(0)
    # print(python_script)
    note_args = qn_args[0].split(' ')

    def process_note_info(note_args):
        note_name = note_args.pop(0)

        file_type = DEFAULT_FILE_TYPE
        dir_name = DEFAULT_DIR_NAME
        
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
    print("Note_name: {}".format(note_name))
    print("File_Type: {}".format(file_type))
    print("Dir_name: {}".format(dir_name))

    """
    # want to know what the directory name is
    # if doesn't exist create the default
    if not dir_name:
        print('Creating dir named: {}'.format(dir_name))
        dir_path = "{}/{}".format(dir_path, DEFAULT_DIR_NAME)
        os.mkdir(dir_path)
    else:
        # TODO: Is this needed?
        # if not os.path.isdir(DEFAULT_NOTE_PATH):
        print('Default dir does not exist. Creating...')
        os.mkdir(DEFAULT_NOTE_PATH)
    """


if __name__ == '__main__':
    main()
