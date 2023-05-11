# Barcode Scanning Attendance System in Python
* As part of my second-semester mini project in Python, I developed a program that functions as an attendance system. It operates by scanning the barcode found on an individual's identity card.
* As part of the development process, I created a Python file that serves as a module for the main project file. This module contains several important code snippets that are essential for the proper functioning of the project. By creating a separate module file, it becomes easier to manage and organize the code, making it more modular and maintainable. 
* The project is a Graphical User Interface (GUI) created using tkinter, which enables the students and faculty members of the Cyber Security Batch at my University to perform various functions such as adding, viewing, and modifying attendance, and accessing important databases.
* To decode the barcode, the project utilizes the pyzbar library and employs an SVM Classifier for accurate and efficient recognition. Furthermore, OpenCV is utilized to capture the barcode and process the images. These tools and techniques enable the system to quickly and accurately extract information from the barcodes and match it with the relevant student or faculty member.
* For the databases, the project uses Excel files, which are commonly used and easily accessible by the majority of users. The Excel files store important data such as student and faculty information, and attendance records. By utilizing Excel files, the project provides a simple yet effective solution for managing the databases, making it easy for users to modify and access the data as required.

## Structure of the Repository
1. [`AttendanceSystem.py`](https://github.com/fromjyce/BarCodeAttendanceSystem/blob/main/AttendanceSystem.py) - This file is the primary Python script that contains all the necessary functionalities and modules for the project. It serves as the entry point for the Graphical User Interface (GUI) and allows users to perform various functions such as adding, viewing, and modifying attendance, accessing important databases, and decoding barcodes. The "attendance_system.py" file is the backbone of the project and is essential for the proper functioning of the system.
2. [`Module.py`](https://github.com/fromjyce/BarCodeAttendanceSystem/blob/main/Module.py) - This file was created to contain various helper functions and utilities used by the main file. This module file is imported and used by the main file to perform image processing, barcode decoding, and database management.
3. [`BarCodeDecoder.py`](https://github.com/fromjyce/BarCodeAttendanceSystem/blob/main/BarCodeDecoder.py) - The code snippet is part of `Module.py` file that captures barcodes and decodes them using the Pyzbar library.This function uses the OpenCV library to capture frames from the camera, and then it decodes any barcodes present in those frames using Pyzbar. The decoded barcodes are stored in a list and returned by the function for use in the program. 
4. [`BCAS - One Page Summary.docx`](https://github.com/fromjyce/BarCodeAttendanceSystem/blob/main/BCAS%20-%20One%20Page%20Summary.docx) - This document provides a comprehensive overview of the project's methodology, datasets, classifiers, output images, flowchart, and image processing techniques. The document outlines the entire development process, including the different stages of design, implementation, and testing. It also includes detailed descriptions of the different functionalities and tools used in the project, providing readers with a clear understanding of how the system works.
5. [`LoadingScreen.py`](https://github.com/fromjyce/BarCodeAttendanceSystem/blob/main/LoadingScreen.py) - This code snippet is located in the `"Module.py"` file and is responsible for creating a loading screen that displays a progress bar while the application is loading. This loading screen helps to improve the user experience by providing users with a clear indication that the application is loading, and reduces the perception of waiting time.
6. [`ExcelProtectedView.py`](https://github.com/fromjyce/BarCodeAttendanceSystem/blob/main/ExcelProtectedView.py) - This code snippet is located in the `"Module.py"` file and is responsible for viewing specific Excel sheets of a workbook in a protected view.he purpose of this code snippet is to allow users to view specific Excel sheets of a workbook without giving them the ability to modify or make any changes to the content. This is achieved by hiding all other sheets in the workbook and enabling a protected view that restricts the user's ability to edit or interact with the content.
7. `CyberSecurity.xlsx` - To ensure the privacy and security of the students and faculty members, the Excel files containing sensitive data were not included in the repository. The Excel files contain important information such as student and faculty details, class schedules, and attendance records. As such, it is essential to protect this information from unauthorized access or manipulation.

## Modules used in the Program
* OpenCV
* tkinter
* datetime
* openpyxl
* pyzbar
* time
* datetime
* pywin32
* pythoncom

## Running of the Programs
To run the Python programs, you need to have a Python Interpreter installed on your system. The programs have been tested on the Microsoft Visual Studio Code in Windows 11. ***You are free to choose any IDE that suits your needs.***

## Contact
If you come across any mistakes in the programs or have any suggestions for improvement, please feel free to contact me <jaya2004kra@gmail.com>. I appreciate any feedback that can help me improve my coding skills

## License
All the programs in this repository are licensed under the MIT License. You can use them for educational purposes and modify them as per your requirements. ***However, I do not take any responsibility for the accuracy or reliability of the programs.***

## MY SOCIAL PROFILES:
### [LINKEDIN](https://www.linkedin.com/in/jayashre-%E2%80%8E-932002251/)

