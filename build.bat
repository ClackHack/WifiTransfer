@echo off
color 2
pyinstaller  --onefile  --log-level INFO main.py
RMDIR /S /Q Build
del main.spec
del dist\wtransfer.exe
ren dist\main.exe wtransfer.exe