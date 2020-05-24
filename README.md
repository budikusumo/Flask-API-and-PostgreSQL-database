# Flask-API-and-PostgreSQL-database
Simple Flask API using single method request ( [POST] only ) to communicate with PostgreSQL

## Project Description

This API project is to simplify the API request using single method only (POST method). This project develop on windows 10, using Visual Studio Code as code editor, and postman. In this project also included:

1. before_first_request module, this module will check anything before the first API request.
     
     a. Identify the database existance (database_exists function) and create a database inside postgreSQL database server (setup_module function on db.py file).

     b. Identify the tabel existance inside the database and create tabels (create_all function), include constraints (primary key, foreign key, check constraints, and tabel relationship), see the models file (agama.py and user.py) inside models folder. 
                   
2. JWT that will authenticate the API request, include generating an access token.

3. This project using Python library Flask, Flask-RESTful, Flask-JWT, Flask-SQLAlchemy, SQLAlchemy_utils, psycopg2, and werkzeug.security. 


## Python Installation

1. Download python installation file from python official website 
```
http://www.python.org
```
2. then, install it. Note: don't forget to check 'Add python 3.x to PATH' usually at the bottom of installation windows.


## Visual Studio Code (VSCode) Installation

1. Download Visual Studio Code installation file from microsoft Visual Studio Code official website 
```
https://code.visualstudio.com/
```
2. then, install it.

3. Run the Visual Studio Code and create a virtual environtment (venv)


## Project Folder Setting

1. create the project folder (in this project, the project folder was API folder, see the folder structure below)
```
API
|-- modules
|   |-- controllers
|   |   |-- __init__.py  
|   |   |-- agama.py
|   |   |-- user.py
|   |
|   |-- models
|       |-- __init__.py  
|       |-- agama.py
|       |-- user.py	 
|-- venv (this folder will appear after the virtual environtment installed. About the installation see below)
|-- app.py
|-- db.py
|-- security.py
```
2. Download all file project inside this git and put it on the project folder (API folder)

3. open this project folder on VSCode.

    a. choose file >> Open Folder... or press Ctrl+K Ctrl+O
    
    b. choose the project folder on windows explorer, then press Select Folder


## Virtual Environtment (venv) Installation

1. open the VSCode terminal press Ctrl+Shift+P, then type Python: Create Terminal, press enter (the VSCode terminal usually at the bottom of VSCode windows and the command prompt usually like this below)
```
'PS D:\API>'
```
note: this project folder (API folder) was placed on D directory.

2. type the command below on the VSCode Terminal
```
python -m venv venv
```
3. if pop up this information 'Do you want to select it for the workspace folder?', choose Yes. This will make the API folder as the workspace folder


## Virtual Environtment (venv) Activation

1. Open Python Terminal (via Ctrl+Shift+P) type "Python: Select Interpreter", then press enter

2. Choose the python interpreter that has extension usually like below
```
./venv/Scripts/python.exe
````
3. type the command below on the VSCode Terminal (in this case, the project folder (API folder) was on D directory) 
```
d:/API/venv/Scripts/Activate.ps1
```
4. when the virtual environtment was activated the command prompt on the terminal will show (venv) infront of the command prompt, see below
```
(venv) PS D:\API>
```
5. check the installed default library on virtual environtment (make sure that the (venv) appear in front of the command prompt like above) then type "pip freeze".
```
(venv) PS D:\API> pip freeze

astroid==2.4.1
colorama==0.4.3
isort==4.3.21
lazy-object-proxy==1.4.3
mccabe==0.6.1
pylint==2.5.2
six==1.15.0
toml==0.10.1
wrapt==1.12.1  
```
6. Install the library as needed (type the command below one by one)
```
pip install Flask
pip install Flask-RESTful
pip install Flask-JWT
pip install Flask-SQLAlchemy
pip install psycopg2
pip install SQLAlchemy_utils
```
7. go to the modules folder by typing the command below on the VSCode terminal, then press enter
```
cd modules
```
8. Run the API application by typing the command below on the VSCode terminal, then press enter
```
python app.py
```
9. and will show this information below on the VSCode terminal (it means that API server activated)
```
(venv) PS D:\API\modules> python app.py

 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 285-235-934
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
10. check the API through postman


## Postman Installation

1. Download Postman installation file from postman official website 
```
https://www.postman.com/downloads/
```
2. then, install it.


## User registration using API request

1. Run the installed postman then type the URL below on request URL box, and choose POST as the API method on the dropdown menu (usually on the left of request URL box)
```
http://127.0.0.1:5000/register
```
2. choose "Headers" tab (below the request URL box), and on "Key box" (left side box) type "Content-Type", on "Value box" (middle side box, just right to key box) type "application/json"

3. then choose "Body" tab (just next/right to "Headers" Tab), choose the "raw" radio button (just below the "Body" tab)

4. type the JSON below on the code box (just below the "raw" radio button)
```
{
    "username": "admin",
    "password": "admin"
}
```
5. then press Send button (right to the request URL box)

6. if Succeed will appear this JSON message 
```
{
    "message": "User created successfully."
}
```


## Authentication using API request


1. Run the installed postman then type the URL below on request URL box, and choose POST as the API method on the dropdown menu (usually on the left of request URL box)
```
http://127.0.0.1:5000/auth
```
2. and do the next step as mentioned above as on 'User registration using API request' (from step 2 to 5)

3. if Succeed will generate the access token
```
{
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1OTAyOTYwODgsImlhdCI6MTU5MDI5NTc4OCwibmJmIjoxNTkwMjk1Nzg4LCJpZGVudGl0eSI6M30.ISZkOR0RgIgffe60qH0hq45TeO1BeaougES2Hbup-t4"
}
```

## API request md_agama tabel (this request need access token for authorization)

1. Run the installed postman then type the URL below on request URL box, and choose POST as the API method on the dropdown menu (usually on the left of request URL box)
```
http://127.0.0.1:5000/agama
```
2. choose "Headers" tab (below the request URL box), and on "Key box" (left side box) type "Content-Type", on "Value box" (middle side box, just right to key box) type "application/json"

3. on Key box (left side box, just below the first "Key box") type "JWT", on Value box (middle side box, just right to key box) type "JWT --the access token as generated on auth--" (explanation JWT[space][the access token value]), see the sample below
```
JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1OTAyOTYwODgsImlhdCI6MTU5MDI5NTc4OCwibmJmIjoxNTkwMjk1Nzg4LCJpZGVudGl0eSI6M30.ISZkOR0RgIgffe60qH0hq45TeO1BeaougES2Hbup-t4
```
4. then choose "Body" tab (just next/right to "Headers" Tab), choose the "raw" radio button (just below the "Body" tab)

5. type the JSON below on the value box (just below the "raw" radio button)

a. Add/Update data
```
{
    "kd_agama": "AAA",
    "nm_agama": "BBB",
    "keterangan": "CCC",
    "catatan": "DDD",
    "is_aktif": "1",
    "user_id": "admin",
    "order": "add",
}
```

b. Delete data
```
{
    "kd_agama": "AAA",
    "nm_agama": "",
    "keterangan": "",
    "catatan": "",
    "is_aktif": "",
    "user_id": "",
    "order": "del",
}
```
note : this API request (delete) only need "kd_agama" and "order" values, so other value can left blank  

c. view all data
```
{
    "kd_agama": "",
    "nm_agama": "",
    "keterangan": "",
    "catatan": "",
    "is_aktif": "",
    "user_id": "",
    "order": "",
}
```
note : this API request (view all) doesn't need any data to be POSTed, so all value can left blank  

d. view secific data
```
{
    "kd_agama": "AAA",
    "nm_agama": "",
    "keterangan": "",
    "catatan": "",
    "is_aktif": "",
    "user_id": "",
    "order": "",
}
```
note : this API request (view specific) only need "kd_agama" values, so other value can left blank  

6. then press Send button (right to the request URL box)

7. if Succeed will appear this message for adding data
```
{
    "message": "Data added successfully."
}
```
