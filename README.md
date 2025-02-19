# Perforce-Automation-Tool
Scripts for a custom tool that automates common version control tasks in P4V and Helix Core by Perforce. 
Ideal for teams with no prior experience using Perforce as part of their pipeline, since the tool greatly simplifies the workflow of creating new changelists, checking out and submitting files, etc.

<img width="1050" alt="P4V-tool" src="https://github.com/user-attachments/assets/7ac4f951-2b69-4623-bbb7-a2d6e03c237e" />

<ins>*Features supported by the tool includes:*</ins>
- Connecting and disconnecting from the Perforce server
- Monitoring of important file activity in the Perforce directory
- Automated process of reverting files from a changelist
- Automated submission of changelists
- Automated deletion of empty changelists
- Automated shelving and un-shelving of files
- Conflict resolution through either local or depot accept

Documentation on how to use the tool can be read in the attached PDF.
An .exe-file is also included for running the tool outside of an IDE environment.

This project was made possible because of Viacheslav Makhynko and the knowledge-sharing from his Udemy course about Python automation in Perforce. I built the tool by following his course and, as of the date of writing this .README file, updated it to work with PySide6, the latest stable version of Python (3.13.1). 
Furtheremore, I've also enabled the Perforce tool to work with the latest version of Substance Painter (10.1.2), so that it can be used in tandem with the Substance Painter Custom Exporter Tool in my other repository.

https://github.com/user-attachments/assets/3ad0f9ad-acf1-45ff-abe0-50bffc687677

## How to install and use:

1. Download this GitHub repository as a ZIP-file under the Code tab and unzip it into a folder.
2. Navigate to the Python folder of your Substance Painter installation. By default it is: *C:\Users\YOUR_USER_NAME\Documents\Adobe\Adobe Substance 3D Painter\python*
3. Copy and paste the *.vscode, modules, plugins* and *startup* folders here, from your unzipped folder.
4. Open Substance Painter.
5. You should now be able to access the Custom Exporter tool. Make sure that *Python -> custom_exporter* and *Window -> Views -> Custom Exporter* are ENABLED from the top left menu options.
6. The Custom Exporter tool should now appear as a widget window in the middle of your screen, that you can dock anywhere you want inside the Substance Painter editor. It behaves like any other widget windows.
7. You can now open any Substance Painter project and utilize the Custom Exporter for streamlining texture exports. Click on the tool's blue help icon to get started, all information on how to use it is written there.
8. OPTIONAL: For dev work on the tool, you need to open the Python modules in Visual Studio Code (or another IDE of choice with Python support, but VS Code is what I used).
9. OPTIONAL: Then add  *"python.analysis.extraPaths": ["C:/Program Files/Adobe/Adobe Substance 3D Painter/resources/python/modules"]* under the default interpreter path in the *settings.json* file.




