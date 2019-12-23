# Quick Note

Using terminal, create and open a new note with your favorite terminal.
Paste often used templates into new notes.

Installation:
1. In `.quick_note.sh` modify where you would like your notes saved by changing the `python_dir` variable.
2. Save `.quick_note.sh` in root directory, add reference into your bash profile and run `source ~/.bash_profile`
3. Modify the default values for the directory name and your preferred text editor.

Usage:
`qn note_name [-e extension_name] [-d dir_name] [-t template_flag]`

Examples:
```sh
$ qn note_name -e py
# Creates note named 'note_name.py'. If note_name already exists. Opens the file.
```

```sh
$ qn note_name -e html -d front_end
# Creates a note names 'note_name.html' filed under the directory 'front_end'. Create directory if doesn't exists.
```

```sh
$ qn note_name -e py -t
# Creates a note names 'note_name.py'. If a py file exists under the template directory, the note will copy the template contents.
```
