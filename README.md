# groundStation

A repository for AIAA-UH Ground station code.

<br><br>

## Installation

### Install source code

`git clone https://github.com/nathansamuell/groundStation/`

_If installing on Development Machine_

Setup and Start Python Virtual Environment:
For my virtual environments, I use miniconda. More information on this system can be found [here.](https://docs.anaconda.com/free/miniconda/index.html) The stock python module instructions are listed below, which works fine!

`python3 -m venv venv`  
`cd groundStation`  
`source bin/venv/activate`  

Install Project + Dependencies

`pip3 install -e .`  
`pip3 install PyQt5`

_If installing on Running Machine_

Install source code

`git clone https://github.com/nathansamuell/groundStation/`

Install Project Dependencies -- _you will also need a DE/WM!!_

`sudo apt-get update && sudo apt-get upgrade -y`  
`sudo apt-get install python3-pyqt5 -y`  
`cd groundStation`  
`pip3 install . --break-system-packages`  
