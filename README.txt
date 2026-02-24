How to run the program :

This folder contains two programs. One for planning events with a brute force and dynamic approach with a selected constraint. Another ,which is the extension task, which
plans events with a brute force and dynamic approach with both constraints simultaneously.

To run the one for planning events with a brute force and dynamic approach with a selected constraint:

Run the "event_planner.py" python file found in the main folder. Upon doing this the user will be prompted to enter the file they want to run the programs on, these 
files are read directly from the "inputs" folder located in the repository. To add more input files make sure they are formatted correctly then add them to the "inputs"
folder in the main folder. Select an input folder by typing its name exactly into the input space, then enter the constraint the user wants to put on the schedule. Then enter whether the user would 
like to run the brute force, dynamic or both by typing in either the name of the desired algorithm or "both". After doing this the necessary information will be printed and the 
input loop will restart.

To run the extension task:

Run the "event_planner.py" in the extension folder. Upon doing this the user will be prompted to enter the file they want to run the programs on, these 
files are read directly from the "inputs" folder located in the repository. To add more input files make sure they are formatted correctly then add them to the "inputs"
folder in the extension folder. Select an input folder by typing its name exactly into the input space, then enter the constraint the user wants to put on the schedule or "both" to 
compute both simultaneously. Then enter whether the user would like to run the brute force, dynamic or both by typing in either the name of the desired algorithm or "both". After doing this 
the necessary information will be printed and the input loop will restart.

Dependancies : 

There are no dependencies or libraries required to be installed

File Structure : 

The repository file structure consists of a main folder which contains the program files for the main program code (only taking in one constraint) as well as the "inputs" folder 
which it reads the input files from. Then there is a folder called "extension" in the main folder which contains the program files for the extension code (can do both constraints simultaneously)
as well as the "inputs" folder which it reads the input files from.