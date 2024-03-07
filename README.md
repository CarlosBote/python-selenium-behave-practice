# Step-by-step guide

This guide explain step by step what you need
to design a automation test with behave in python language


## Environment configuration
### 1. Create and activate venv
Normally, you can set up the virtual environment (venv) when creating the project
in PyCharm. However, if you encounter issues with that or if you are using a different IDE,
you may need to set up the venv using terminal commands.
If this is the case, follow the instructions below.

create the venv with the following command:

`python3 -m venv <venv_name>`

Then activate the venv:

MacOS and Linux:
`source <venv_name>/bin/activate`

Windows:
`<venv_name>\Scripts\activate`

### 2. Install all dependencies
Use the python package manager (PIP) to install Selenium and Behave:

`pip3 install selenium behave`

It's good practice to create a requirements.txt file containing all dependencies in plain text.
You can generate this file easily by executing the following command:

`pip3 freeze > requirements.txt`

If you already have a requirements.txt file, you can install the
dependencies listed in it by executing the following command:

`pip3 intall -r requirements.txt`

## Directory Architecture
The directory architecture must have the following structure 

    project/ 
        ├──features/  
        │    ├──feature_name_1.feature
        │    ├──feature_name_2.feature
        │    ├──feature_name_3.feature
        │    └──steps/ 
        │        ├──step_definiton_1.py
        │        ├──step_definiton_2.py
        │        └──step_definiton_3.py
        │
        ├──pages/ 
        │    └──page.py
        │
        ├── utilities/ 
        │    ├── __init__.py
        │    ├── config.py
        │    └── logger.py
        │
        ├──venv/
        │
        ├── .gitignore
        ├── behave.ini
        ├── requirements.txt
        └── README.md

## version the project iun a remote repository
### 1. version locally with git
execute the below commands:

initiate local git repository: `git init`

add the files to the staging area: `git add .`

Do the first commit: `git commit -m "first commit"`

Create a branch: `git branch -M main`

### 2. Version remotely 

Create a remote repository in GitLab or GitHub

add the remote repository`git remote add origin «URL_of_your_remote_repository»`

push the changes of your local repository to the remote `git push -u origin main`




        


