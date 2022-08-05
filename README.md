# Covid Questionnaire
The COVID-19 Questionnaire deploys when a person is detected by a camera. Its purpose is to serve as an automated reminder about the current COVID-19 quarantine and isolation guidelines.

![Program being run](https://i.imgur.com/sWf93rR.png?1)

## The Algorithm
This code uses the Jetson Detectnet SSD-Mobilenet-v2 detection model in order to identify objects (in this case a person) in the camera frame. It then assigns the identified object to a class in a specified set (in the case of Mobilenet-v2 one of the 91 COCO classes).

## Running this project
Requirements:
1. Jetson nano
2. USB webcam
3. USB to MicroUSB Data Cable
4. USBC Power Supply
5. Ethernet Cable 

Directions:
1. SSH into your jetson nano via terminal using "ssh @<username> 192.168.55.1" then entering your password and pressing enter when prompted
2. Install git and cmake ("sudo apt-get update" then "sudp apt-get install git cmake")
3. Clone the jetson-inference project ("git clone https://github.com/dusty-nv/jetson-inference" then "cd jetson-inference" then "git submodule update --init")
4. Install python packages ("sudo apt-get install libpython3-dev python3.numpy")
6. Install Mobilenet-v2 using "$ cd jetson-inference/tools" then "$ ./download-models.sh" and using the downloader tool
7. Create a directory in your home folder using "mkdir <directory name>"
8. Either use the nano command to create a file and copy and paste the code in or download questionnaire.py on your computer and upload it to the jetson directory using "scp <from> <to>"
9. Run the program in the directory you created using "python3 questionnaire.py"

[View a video explanation here](https://youtu.be/wZePneHsl8M)
