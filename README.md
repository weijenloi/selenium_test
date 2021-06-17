# selenium_test

## Setup environment
Setup environment before running test

    python -m venv .env


## Activate environment & Install Packages
Packages requirements for running test

    .\.env\Scripts\activate
    pip install -r requirements.txt

## If SSL Error

    pip install -r requirements.txt --trusted-host pypi.org --trusted-host files.pythonhosted.org


## To run Test

    python maintest.py

### First draft implementation

Unit test written for Chrome Browser and Windows Platform
Test1 - Move small circle to big circle and assert text
Test2 - Upload file and assert upload status
#### To do

C# version of Unit Test
Firefox
Other OS

#### Identified challenges:

1. Limitation on Python selenium capabilities to interact with open file dialog box. There is a need for pygetwindow in order to interact with Win32 windows. Although we might be able to direct send file path to input element of the page for file upload.

1. Initial approach is to use jQuery, due to script needed to be imported and jQuery requires a CSS_Selector to find elements. jQuery approach should be used together with jQuery or Javascript actions

1. Still on research on how to write back test result to a file


### Linux Ubuntu
1. NotImplementedError: PyGetWindow currently does not support Linux.
sudo apt-get install -y libwnck-3-0 
pip3 install vext
pip3 install vext.gi
