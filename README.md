# Perforce-Automation-Tool

<img width="1050" alt="P4V-tool" src="https://github.com/user-attachments/assets/7ac4f951-2b69-4623-bbb7-a2d6e03c237e" />

Scripts for a custom tool that automates common version control tasks in P4V and Helix Core by Perforce. 
Ideal for teams with no prior experience using Perforce as part of their pipeline, since the tool greatly simplifies the workflow of creating new changelists, checking out and submitting files etc.

<ins>*Features supported by the tool includes:*</ins>
- Connecting and disconnecting from the Perforce server
- Monitoring of important file activity in the Perforce directory
- Automated process of reverting files from a changelist
- Automated submission of changelists
- Automated deletion of empty changelists
- Automated shelving and un-shelving of files
- Conflict resolution through either local or depot accept

Documentation on how to use the tool is included in the attached PDF.

This project was made possible because of Viacheslav Makhynko and the knowledge-sharing from his Udemy course about Python automation in Pertforce. I built the tool by following his course and, as of the date of writing this .README file, updated it to work with PySide6 and the latest stable version of Python (3.13.1).



