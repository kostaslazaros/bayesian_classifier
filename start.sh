#!/bin/sh
python flaskapp.py &
python -m http.server &
