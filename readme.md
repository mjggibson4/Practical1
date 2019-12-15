# Population Model

## Description

This python based project a simple agents based model of predator prey dynamics. In this scenario these two competing agents have been defined as that of sheep and wolves. These agents move randomly around a defined domain and are allowed to interact with one another. In particular, these sheep agents "graze" their spatial eniviroment while the wolves consume these sheep if close enough. Both of these agents reproduce dependent on the resources on which they have consumed. This model provides a visual representation of these spatial dynamics and behaviours.

The exact logic and "rules" of this population model can be found in more detail here: [here](https://github.com/mjggibson4/Practical1/blob/master/Scope.md "")

## Table of Contents

1. Prerequisites
2. Installation
3. Initialising Program
4. Running Program
4. Standards
4. Known Issues
5. Acknowledgements

## Prerequesits

Before this project can be executed, a suitable python enivironment must first be in place. This project was used using the data science platform Anaconda. This package is free and includes the integrated development environment Spyder 3.3.6 on which this project was developed. A installation guide to Anaconda alongside installation instructions can be found here: 
[install guide](https://docs.anaconda.com/anaconda/install/windows/ "").

This model scrapes the initial locations for the sheep agents from the web. Due to this a suitable web connection is advised although in it absense these starting locations will be randomly generated.


## 1 Installation

This project consists of 3 python scripts and one text file which should be downloaded from the github repository found here: [Practical 1 Repo](https://github.com/mjggibson4/Practical1 ""). These files should be saved to the users desktop

## 2 Project Structure

The three script files contained within this project have their own unique function.

GUI:  Sets up the graphical user interfaces from which the program is run. This interface allows for the initial parameters of the model to be edited as neccesary. 

Maincode: Defines the logic behind the model itself.

Framework: Contains the classes from which the agents are defined. This framework dictates the behaviours of the agents such as how they move, eat and reproduce. 

In.txt: Defines the environment in which the agents interact with

## 3 Initialising the Program

This model can be initilised in one of two manners:

#### Option A: From command line
1. Right click on the Desktop.
2. Select Open New Command Window Here
3. Type python GUI.py
4. Press enter

#### Option B: From IDE
1. Open the file GUI in Spyder
2. Press Run

Either of these methods should result in the GUI for the population model being presented as displayed below


## 4 Running Program

### Open Parameters Menu

Click menu and then "Set Parameters". This produces a window in which the user is asked to input 6 parameters which will influence the behaviour of the model. These parameters are listed below alongside a brief explaination of what they represent in regards to the model.

* Number of Sheep - The initial number of sheep agents to be placed in the model
* Number of Wolves - The initial number of wolf agents to be placed in the model
* Neighbourhood - The distance at which sheep are allowed to share resources
* Number of Iterations - The number of iterations for which the model will run
* Wolf Threshold - The number of sheep needed to be eaten by a wolf in order for it to reproduce
* Sheep Threshold - The amount of units of environment needed to be consumed by a sheep in order for it to reproduce


![alt text](https://github.com/mjggibson4/mjggibson4.github.io/blob/master/ParameterMenu.png "Logo Title Text 1")
 
Once these parameters have been defined, click apply. These parameters must be postive integers and an internal check occurs to verify this is the case. If this is not the case, a warning is displayed on the screen.

###  Run the Model

Select the "Model" menu and "Click" Run. A within the canvas of the GUI window, the agents will be observed moving around the domain.

## 5 Standards

This model has been produced in Python 3.7. The code has been produced to adhere to Google Python standards. The full details of this style can be found [here](http://google.github.io/styleguide/pyguide.html "")

## 6 Troubleshooting

In the case of errors within this program please check the troubleshooting file which can be located [here](https://github.com/mjggibson4/Practical1/blob/master/InternalChecks.md "")

## 7 Licensing

This program is open source and licensed via an MIT license. The full details of this license are available [here](https://github.com/mjggibson4/Practical1/blob/master/License.md "")

## 8 Acknowledgements

This project has been produced as part of coursework for the module: Programming for Geographical Information Analysts: Core Skills (WUN).  Exercises and tutorials given within this course have been modified as appropriate and used within the python code for this project. In addition, I'd like to give thanks to my course tutor Andy Turner who helped with issues encountered during development.
