# Stackoverflow-lite

[![Build Status](https://travis-ci.org/lennykamande/stackoverflow.svg?branch=master)](https://travis-ci.org/lennykamande/stackoverflow)

[![Coverage Status](https://coveralls.io/repos/github/lennykamande/stackoverflow/badge.svg?branch=master)](https://coveralls.io/github/lennykamande/stackoverflow?branch=master)

# stackoverflow Lite
This is the Userinterface to our Stackoverflow Lite Project.

## Getting Started
Clone or download the project from git either via terminal using the commands 
* git clone : https://github.com/lennykamande/stackoverflow.github.io
* Download zip file from the right hand coner


## Use the following endpoints to perform the specified tasks
		 
| 	Endpoint                               | Functionality                                                  
| ---------------------------------------------| -----------------------------------------------|
| POST api/v1/auth/registration                | Create a user account                          |          
| POST /api/v1/auth/login                      | Login a user                                   |
| GET api/v1/auth/users                        | Retrieve the registered users                  |
| GET /api/v1/auth/users/<int:id>              | Retrieve a specific registered user            |
| POST /api/v1/questions                       | Create a question                              |
| GET /api/v1/questions                        | Retrieve posted questions                      |
| POST /api/v1/questions/<int:id>/answer       | Create an answer to a specific question        |
| GET /api/v1/questions/<int:id>               | Retrieve a specific posted question and answer |
		 

## Application Features

1. Create and Read questions
2. Create and Read answers

<br>

**Users can do the following**

* Users can create an account and log in.
* Users can post questions.
* Users can delete the questions they post.
* Users can post answers.
* Users can view the answers to questions. 


### Prerequisites

Please make sure you have a browser installed on your computer if you want to be able to check all files and see how the user interface looks like.

### Installing

Make sure you download postman to be able to test the specific endpoints on this project.

## Running 

git clone https://github.com/lennykamande/Stackoverflow-lite
cd into folder
create a virtual enviroment using virtualenv nenv
activate nenv
run command "python run.py"

### Happy Coding/Debugging
