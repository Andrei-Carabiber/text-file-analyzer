# Text File Analyzer

A simple and efficient command-line Python tool for analyzing and manipulating text files. It offers various operations to process text, such as word counting, punctuation removal, case conversion, and identifying the most common words, among others.

## Features:
- **Count Words**: Count the total number of words in the text file.
- **Remove Punctuation**: Automatically remove common punctuation marks from the text to clean it up.
- **Convert Text Case**: Change the text to lowercase or uppercase to normalize it for further analysis.
- **Most Common Words**: Identify and display the most common words in the text file, sorted by frequency.
- **File Reset and Modification**: Apply multiple operations at once or reset the file to its original state.

## Installation:

Make sure you have python installed. To check run:
```
python --version
```
You need at least python 3.x in order for this to run.
If you don't have it installed follow the next instructions.
If you have it already just skip to **Running the code**

## Downloading:
You have to clone this in order to have it on your pc. To do this go to where you want to download this and open a terminal.
### Normal Clone with Username-Password
In the terminal run the following command
```
git clone https://github.com/your-username/word-counter.git
```
Where __your-username__ is your GitHub username.(You will be asked for your username and password)
### Clone with SSH Key
In the terminal run the following command
```
git@github.com:your-username/word-counter.git
```
Make sure you replace __your-username__ with your GitHub username.
In order to have this work you must set up the SSH key on your PC and on GitHub. With this method you will not be asked
for credentials.
## Python on Windows

### **Step 1: Install Python via the Microsoft Store (Recommended)**

1. Open the Microsoft Store on your PC.
2. In the search bar, type "Python".
3. Select Python 3.x (latest version available) and click Get.
4. Once the installation is complete, Python will be installed, and the python command will be available in the terminal.

### **Step 2: Install Python via the Official Installer (Alternative)**
1. Visit the official Python [website](https://www.python.org/downloads/).
2. Download the latest Python installer for Windows.
3. Run the installer and make sure to check the box "Add Python to PATH" during the installation.
4. After installation, open Command Prompt or PowerShell and verify Python installation:
```
python --version
```
You should see the Python version printed, indicating it's installed correctly.

## Python on MacOS

### **Step 1: Install Python via Homebrew (Recommended)**
1. **Install Homebrew** ( If not already installed). Open terminal and paste
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
2. Install Python via Homebrew:
```
brew install python
```
3. After installation, verify Python:
```
python3 --version
```
### **Step 2: Install Python via the Official Installer (Alternative)**
1. Visit the official Python [website](https://www.python.org/downloads/).
2. Download the latest Python installer for macOS.
3. Open the .pkg file and follow the installation instruction
4. After installation, open the terminal and verify Python installation:
```
python3 --version
```

## Running the code
1. Put you .txt file in the put-file-here folder
2. Open a terminal in the main folder that contains main.py
3. **WINDOWS** Run the following command:
```
py main.py
```
3. **macOS** Run the following command:
```
python3 main.py
```
4. Follow the instructions in the terminal
