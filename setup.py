# we have imported find_packages and setup classes
from setuptools import find_packages,setup

# now we are using setup method
setup(
    name='mcqgenrator', #what ever the init file is there inside the folder it will treat it as a package
    version='0.0.1',
    author='sunny savita',
    author_email='sunny.savita.tests@ineuron.ai',
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)