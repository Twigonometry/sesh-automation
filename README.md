# sesh-automation

Demo code for Sheffield Ethical Student Hackers' Automation in Python session.

## blindcommit.sh

Demonstrates the 'gitgone' code shown in session. Echoes some text to commit-this.txt so there's something to send off. If run, WILL commit + push all changes to master - so be careful!

## params-and-flags

Bash script to demo parameters and flags in bash. Pass optional `-s` and `-i` flags as well as an arbitrary number of positional parameters - they will all be printed to the screen.

## basic-files.py

Reads all files in the basic-files directory - used as a precursor to showing make-and-move.py. Really nothing interesting to see here - there's not even any validation.

## make-and-move.py

Demos the use of `os` and `subprocess` libraries to create several .txt files and move them to a new directory.

## basic-http.py

Makes a GET request, and a POST request. Exciting.

## basic-api.py

Tells you the weather in Sheffield. Make sure you sign up for an account at https://openweathermap.org first and add your API key to a file called conf_secret.py - we don't include that for you, unfortunately!