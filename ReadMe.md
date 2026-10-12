To run the script

create a virtual environment with python 3.12

py -3.12 -m venv .venv

If the venv environment doesn't open just running
.\.venv\Scripts\Activate.ps1

Then run this command
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1

Then run
pip install PyRth

Debugging
If you get a NaN issue, make sure the data doesn't have 0 seconds as an input
