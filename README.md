# QHack2022_LudoTeleport
This directory is created for uploading QHack solutions for IBM challenge

## Steps to open & play the Game
1. Install Django and Qiskit
 - To install Django type in: _pip install Django==3.1.5_
 - To install Qiskit type in: _pip install qiskit_
2. Dowload & extract the zip file 'qsite'
3. Open the /qsite/qrng/views.py file
 - In the code you will see a line called IBMQ.enable_account('ENTER API KEY HERE'). This is where you need to put in an API token. In order to get an API key you will have to register to the IBM quantum experience: https://quantum-computing.ibm.com
4. Using terminal, navigate to the directory where qsite folder has been extracted.
5. Make sure you have the files up to date by entering: _python manage.py migrate_ in to your terminal.
6. Make sure you have the django webservice running by entering: _python manage.py runserver_ in to your terminal.
7. Now you are all set. Just open any web browser, and type http://localhost:8000/ to enjoy and play LudoTeleport!

## Members
 - Vardaan Sahgal @Varary73
 - Deeksha Singh @deeksha-singh030 
 - Dinesh Vishnu Kumar @dineshvishnugithub
