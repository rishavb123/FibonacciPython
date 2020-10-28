@echo off
python compile.py %1%.fpy
python %1%.py
del %1%.py