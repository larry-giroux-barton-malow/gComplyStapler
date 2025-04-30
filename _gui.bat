@REM Run gui.py with python interpreter
python gui.py
@REM Check if the script was run with the correct interpreter
IF ERRORLEVEL 1 (
    @ECHO.
    @ECHO This script must be run with the Python interpreter.
    @ECHO Please ensure that Python is installed and added to your PATH.
    @ECHO.
    EXIT /B 1
)
@REM Check if the script was run with the correct interpreter
