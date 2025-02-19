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

1. First make sure that Perforce Helix Core and P4V are both installed on your PC, and that you have set up a workspace directory for Perforce.
2. Download this GitHub repository as a ZIP-file under the Code tab and unzip it into a folder.
3. You should now be able to run the tool either with the .exe-file or by going into main.py and running the file from an IDE environment like Visual Studio Code.




