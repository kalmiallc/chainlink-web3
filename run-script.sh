#!/bin/bash

if [ "$1" = "test" ]; then
    echo Run tests
    python3 setup.py pytest
fi

if [ "$1" = "build" ]; then
    echo Build library
    python3 setup.py bdist_wheel
fi