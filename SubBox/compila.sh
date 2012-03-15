#!/bin/bash

PROJECT_DIR=/Users/paganotti/Documents/Progetti/Python/SubBox

python $PROJECT_DIR/setup.py py2app > log_compila.txt

/Applications/TextEdit.app/Contents/MacOS/TextEdit $PROJECT_DIR/dist/SubBox.app/Contents/Resources/__boot__.py





