# AirBnB_clone
Python Airbnb clone: console app with Fabric deployment on Nginx. REST API with Flask, data stored in local files &amp; MySQL. HTML/CSS for dynamic web interface.

![image](https://github.com/vick-ram/AirBnB_clone/assets/89000333/4bec4911-6a93-489c-8a55-5c12ee251d8f)
# Background Context
## Welcome to the AirBnB clone project!
Before starting, please read the **AirBnB** concept page.
### First step: Write a command interpreter to manage your AirBnB objects.
This is the first step towards building your first full web application: the **AirBnB clone**. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…
Each task is linked and will help you to:
* put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
* create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
* create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
* create the first abstracted storage engine of the project: File storage.
* create all unittests to validate all our classes and storage engine
## What’s a command interpreter?
Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:
* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object
# Learning Objectives
## General
* How to create a Python package
* How to create a command interpreter in Python using the **cmd** module
* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* How to manage **datetime**
* What is an **UUID**
* What is **\*args** and how to use it
* What is **\*\*kwargs** and how to use it
* How to handle named arguments in a function
# More Info
## Execution
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
But also in non-interactive mode: (like the Shell project in C)
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
All tests should also pass in non-interactive mode: $ echo "python3 -m unittest discover tests" | bash
![image](https://github.com/vick-ram/AirBnB_clone/assets/89000333/1ae0e327-6a58-4b7c-989e-358c9cd4db9d)