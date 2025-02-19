# Perforce-Automation-Tool

<img width="1050" alt="P4V-tool" src="https://github.com/user-attachments/assets/7ac4f951-2b69-4623-bbb7-a2d6e03c237e" />

Scripts for a custom tool that automates common version control tasks in Perforce P4V. 

If naming conventions or texture resolutions do not pass the validation checks for a given texture set, exporting will be disabled for that texture set, until it meets the validation requirements.

The tool can automatically change the texture resolution to meet the texture budget, and allows lower resolution as long as the texture doesn't exceed the maximum allowed budget per asset type texture.

It will only export to a specified folder, based on the selected asset name, and a dropdown-selectable shader type controls the export presets.

Hot-keys and documentation are included.

This project was made possible because of Viacheslav Makhynko and the knowledge-sharing from his Udemy course about Python automation in Substance Painter. I built the tool by following his course and updated it to work with the PySide6 module and, as of the date of writing this .README file, the latest stable version of Python (3.13.1) and Substance Painter (10.1.2).

For future work, I plan to extend upon the project and add at least some of the following features:

Adding support for exporting textures that are using UV Tile workflow (UDIms)
Automation of texture renaming to be within naming conventions
Extending resolution validation for non-square sizes (width != height)
Adding support for textures that use material layering
