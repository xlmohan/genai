# -01 create virtual environment
## you are creating the environment inside the path rather than giving it a name. conda only lists named environments
conda create -p env python=3.8 -y

# -02 Activate the env 

source activate ./env

# -03 folders required

- src (source code)
    - __init__.py ()
    - mcqgenerator (consider this folder as a local package)
        __init__.py (what ever source code which i am writing inside the project, we will write here itself)
    
## Note: What will package: it is a folder which contain multiple file, inside the file you will, example: numpy, pandas there are all packages, inside that you will be having multiple python files, we are going to use particular file

## Here mcqgenerator - the convenstion to treat it as a package is by using __init__.py it represents the folder is a package

    - experiment
        - mcq.ipynb (ipynb is i python notebook )

## what ever experiment you want to do in your applications you can do it in here and later you can push it to end to end pipeline

# -04 open the mcq.ipyd file and you will find Select kernel on the right side click on it and you will find one popunder select env (Python 3.8 blablabla.....)

# -05 you need to use this repository
https://github.com/sunnysavita10/Automated-MCQ-Generator-Using-Langchain-OpenAI-API

## we are going to use openai api using langchain

# -06 Many ways to install the packages

1- pip install openai 
2- if you have multiple packages, you have two ways
python -> setup.py
1) save all the package name inside the requirements.txt (it should be in that formate only)
pip install -r requirements.txt (-e .) - automatically it will search packages in you current virtual environment and install it
2) Lets open setup.py file and copy the code, code is having statement find_packages, setup, and using setup method you need to mention the following setup
packages=find_package() - it will consider only the file which is having __init__.py inside the folder then it will recognize that as a package (it will download all the packages from you local)

Note: you will find all the meta information inside the mcqgenerator.egg-info with respect to your local packages as well

---- check the packages if there are installed or not ----
import sys
print(sys.executable)

!{sys.executable} -m pip install langchain-openai

from langchain_openai import ChatOpenAI
---- if package is installed but seems not working try this ----

---- To create end to end project, follow the steps -----

# inside src folder create another folder called mcqgenerator, inside mcqgenerator folder create logger.py

why we need to use utils.py file, it is a helper file, what every helping code, function and all you are going write inside that utility file

# total three files we have created
src >> mcqgenerator >> MCQGenerator.py, logger.py and utils.py

# another file we will create inside root directory Response.json file

# one more file we will create inside root directory StreamlitAPP.py

In any project these file and file structure will remain same.

---- commit the changes inside github -----

---- Lets start with the coding ----
 # 1. we have various classes and functions and all, the functions which you going to create for particular purpose, when every you execute that function it will save inside.
 logger.py >> create logger file using dymanic date-time stamp when ever function or class or any action is triggered

 check python logger documentation there you can find how to use the labels example: till info and above the info 
 https://docs.python.org/3/library/logging.html#:~:text=pickled%20and%20unpickled.-,Logging%20Levels,-%C2%B6



 -- to activate the envirounment ----
 source activate ./env
 pip list ( it will list all the libraries and packages )
 Note : you will also find your local package as well mcqgenerator






