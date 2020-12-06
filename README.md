# Group 3

Thursday Tutorial

Adam Baker  
Sam Guttormson  
Jeff Folster  
Johann Doell  
Oluwaseun Fashoranti  

To run test_proof_of_concept.py:

Ensure Pytest is installed.

In Pycharm:
   1. Go to Settings/Preferences,
      under Tools|Python Inegrated Tools|Testing
      choose "Default test runner" to be pytest.
   2. If run configuration not set
      for test_proof_of_concept.py,
      right-click the file and click
      "create 'pytest in test_proof_of_concept.py'"
   3. Right-click the directory "src", then
      "Mark Directory As|Sources Root" to ensure that the
      test file imports the module Names.py.
   3. Run the file. If the file produces no output, check
      that the configuration is running pytest.
   
------------

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
flask run
```
this will start up the back end server
next, in the second tab/window run:
```
cd group3/src/react-components
npm start
```
this will launch the front end React app. After a few seconds the app will
launch your browser and open up our website automatically.

You are now free to interact with the forum!
