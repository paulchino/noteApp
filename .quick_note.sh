#!/bin/bash
# Include in bash profile

function qn() {
  if [ -z "$1" ]
    then
        echo "ERROR: No arguments supplied"
        return 1
  fi
  # map to location of the project directory
  python_dir="${HOME}/Desktop/projects/noteApp/source/"
  script_name="note_app.py"
  note_args="$@"
  python "${python_dir}${script_name}" "${note_args}"
}
