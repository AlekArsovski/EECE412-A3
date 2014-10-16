IMPORTANT! PLEASE USE THESE INSTRUCTIONS AS THERE ARE SOME ERRORS IN THE PDF INSTRUCTIONS!!!

===EXECUTABLE===
We have decided to include an exe so that the instructors don't have to do the installation as it is quite cumbersome. The executable is named "VPN_Group19.exe"

Please note that all files in the folder are required in order for the executable to run.


===IF YOU WISH TO INSTALL INSTEAD===

Our solution is written in Python. It can be accessed at the following GitHub repository:
https://github.com/AlekArsovski/EECE412-A3.git

The file "test.py" is the one you need to compile.

The user needs to have Python running in Windows (we tested it on Windows 8). As such, if Python is not yet installed, a user will need the following Python installation here: https://www.python.org/download/releases/2.7/.

In addition, PyCrypto 2.6 for Python 2.7 is required which can be found here: http://www.voidspace.org.uk/python/modules.shtml#pycrypto

Lastly, wxPython 3.0 for Python 2.7 is necessary which can be found here:
http://www.wxpython.org/download.php

Once installed, the “python” command should be added to the PATH environment variable, and the user can execute the program by navigating to the folder containing the python program in command line or terminal, and entering “python assignment_3_group_19”.

Once this is done, a graphical interface containing all the functionalities required in the assignment should pop up, and the user will be able to select between client or server mode.


===HOW TO USE===

Please note that the program does not gracefully handle deviations from the following setup process:

If setting up server:
1. Select "Server" radio button
2. Enter your own IP address
3. Enter desired port number
4. Enter shared secret key
5. Click set and wait for client to authenticate
6. Once the client has authenticated then you may enter your message in the "Data to be Sent" textbox and click on the "Send" button to send your message
7. Client messages will be displayed in the "Data Received" textbox

If setting up client:
1. Select "Client" radio button
2. Enter IP address of the server
3. Enter desired port number
4. Enter shared secret key
5. Click set and wait for server to authenticate
6. Once the server has authenticated then you may enter your message in the "Data to be Sent" textbox and click on the "Send" button to send your message
7. Server messages will be displayed in the "Data Received" textbox

For logs:
-If "Enable Continue" is not checked it will display all log messages.
-If "Enable Continue" is checked it will backlog all log messages and pressing "Continue" will show every message line by line.