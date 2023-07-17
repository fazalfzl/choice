@echo off

REM Clone the repository
git clone https://github.com/fazalfzl/choice.git temp_clone

REM Copy the contents of temp_clone to the current directory
xcopy temp_clone . /E /H /C /I /Y

REM Remove the temp_clone directory
rd /S /Q temp_clone

REM Generate common_support for pyarmor
pyarmor gen common_support application.py

REM Copy the contents of the dist folder to the current directory
xcopy dist . /E /H /C /I /Y

echo All commands executed successfully.
pause
