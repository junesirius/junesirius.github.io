#!/bin/sh
#!/usr/bin/env bash

INSTALL_PYTHON="G:\Anaconda3\envs\py38\python.exe"
PYTHON_SCRIPT=".pre-commit.py"

if [ -x "$INSTALL_PYTHON" ]; then
    if [ -f "$PYTHON_SCRIPT" ]; then
        python $PYTHON_SCRIPT
    else
        echo "$PYTHON_SCRIPT not found. Skipping pre-commit checking."
    fi
else
    echo "'pre-commit' not found. Skipping pre-commit checking."
fi

if [ $? != 0 ]; then
    echo "git status:"
    git status --untracked-files=no
    exit 1
fi
