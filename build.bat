@echo off
color 2
pyinstaller  --onefile --noconsole --icon=biblelogo.ico --log-level INFO gui.py
RMDIR /S /Q Build
del gui.spec
del dist\Bible.exe
ren dist\gui.exe Bible.exe