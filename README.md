# Group 3

Thursday Tutorial

Adam Baker  
Sam Guttormson  
Jeff Folster  
Johann Doell  
Oluwaseun Fashoranti  

## How to run this project
First you need to create a local version of our repo, on the command line cd
into your favourite directory and run:
```
git clone https://git.cs.usask.ca/CMPT370-01-2020/group3.git
```
After that completes you'll need to install all of the NodeJS modules that the
projects depends on. This can be done by running the following commands
```
cd group3/src/react-components
npm install
```
This will install [create-react-app](https://reactjs.org/docs/create-a-new-react-app.html) which was used to bootstrap the product at v4.0.0.
Then, just to be safe you should run the following command to fix and vulnerabilities
```
npm audit fix
```
Both these will take about 30-45 seconds each
now you're ready to start using the project!

You're going to need two command line tabs/windows in order to run both of our
layers
In the project directory on the first command line, run the following commands:
```
cd group3/server
pip install flask
flask run
```
This will start up the back end server and install [Python Flask](https://flask.palletsprojects.com/en/1.1.x/) at 1.1.2
next, in the second tab/window run:
```
cd group3/src/react-components
npm start
```
This will launch the front end React app. After a few seconds the app will
launch your browser and open up our website automatically.

You are now free to interact with the website!

## How to run Python test files:

For any file in directory "tests":

Ensure Pytest is installed.

In Pycharm:
   1. Go to Settings/Preferences,
      under Tools|Python Inegrated Tools|Testing
      choose "Default test runner" to be pytest.
   2. If run configuration not set
      for file of the form test_filename.py,
      right-click the file and click
      "create 'pytest in test_filename.py'"
   3. Right-click the directory "server", then
      "Mark Directory As|Sources Root" to ensure that the
      test file imports the module Names.py.
   3. Run the file. If the file produces no output, check
      that the configuration is running pytest.
   
------------


The medication API was meant to be a way for drug information to be pulled into the project, however it is not implemented.
The API that was used https://rxnav.nlm.nih.gov/RxNormAPIs.html. The goal for this API was to fetch medication data, which would then be 
put into a list that would attach in the patient profile. The file was supposed to be in an api_handler file in the flask project, 
however it is not implement completely. Though if it is in the correct place pulling data does work, by typing in the drug you want
it should come back with the brand name, the chemical name, the synonym and suppress information. One of which would be added to a list
and would show up in the patient profile. 