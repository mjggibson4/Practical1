#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Main code of the population model. Creates the agents and defines how these
act.

This script creates the agents and environment in which they act. This script 
calls the class methods from the script framework to define these agents
behaviour. This simulation happens over a defined set of iterations and is 
animated within a graph which is passed back to and observed within the model
GUI 

  Typical usage example:

  Typically this module will only ever be called from the script GUI.py. 
  However for development purposes, this script can be ran independently using 
  the code defined within the fuction if __name__ == "__main__":
"""

# Import required modules
import matplotlib
matplotlib.use('TkAgg')
import random
import matplotlib.pyplot
import matplotlib.animation 
import framework
import requests
import bs4
from tkinter import messagebox
import sys


#Set intial values for the model


def create_environment():
    """Creates an environment for agents to inhabit and interact with.

    Retrieves csv data from a defined .txt file from the document repository. 
    This data is constructed into a list of lists which matches the dimensions
    defined by the csv file. If this file is not found in the correct directory
    the user is informed and the program terminated

    Args:
        in.txt - .txt file defining the enviroment and its values

    Returns:
        Enivironment - A list of lists that represents the enivironment in 
        which agents are to move around.

    Raises:
        Prints an error in the console asking the user to place in.txt file in 
        the correct directory and terminates program
    """
    try:
        # Define initial list
        environment = []
        # Attempt to open .csv file
        f = open("in.txt")
        #Create enivronment
        for line in f:
            parsed_line = str.split(line,",")
            rowlist = []
            for word in parsed_line:
                rowlist.append(float(word))
            environment.append(rowlist)
        f.close()
        return environment
    except:
        # If error returned, inform user and state that the file is not in the 
        # specified location
        messagebox.showerror("Error", "File 'in.txt' not found in specified directory. Please ensure this file is in the correct location and rerun this scenario")
        # End program
        sys.exit()    


def set_sheep(environment, num_of_sheep):
    """Creates a list of sheep agents.

    Webscrapes preset online data in order to define the starting location of
    the sheep agents. If a web connection is not present, these starting 
    locations are randomly placed using the class method of the sheep class object

    Args:
        enviroment: This list models the enviroment in which sheep agents 
        will be moving and interacting with.
        num_of_sheep: This variable outlines how many sheep agents are to be 
        created within this function.
        

    Returns:
        flock: A list containing a defined amount of sheep
    
     Raises:
        Prints message box if program is unable to access the URL which defines
        the initial starting coordinates of the sheep
    """           
    #Initialise flock list
    flock = []    
    try: 
        # Access HTML of website
        r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
        content = r.text
        soup = bs4.BeautifulSoup(content, 'html.parser')
        # Search HTML for y and x tags and pass these values into a list
        td_ys = soup.find_all(attrs={"class" : "y"})
        td_xs = soup.find_all(attrs={"class" : "x"})
    
        # Create and return a list of sheep agents: flock
        for i in range(num_of_sheep):
            _y = int(td_ys[i].text)
            _x = int(td_xs[i].text)
            flock.append(framework.Sheep(flock,environment, _y, _x))
        return flock
    
    except:
        # If defined URL is not available, warn user
        messagebox.showerror("Information", "Unable to retrieve initial sheep starting locations. Scenario will be initialised with random data")
        # Create and return a list of sheep agents: flock
        for i in range(num_of_sheep):
            _y = None
            _x = None
            flock.append(framework.Sheep(flock,environment, _y, _x))
        return flock


def set_wolves(environment, num_of_wolves):
    """Generate a list of wolf agents.

    Generates a list of wolf agents. These agents are to be randomly placed
    around the domain of the environment using the class methods defined within
    the wolf object class. 
    
    Args:
        enviroment: This list models the enviroment in which wolf agents 
        will be moving and interacting with.
        
        num_of_sheep: This variable outlines how many wolf agents are to be 
        created within this function.

    Returns:
        wolves: A list of wolf agents

    Raises:
        Null
    """
    # Initialise wolfpack list  
    wolves = []
    # Loop around the number of wolves to be defined and append this to list
    for i in range(num_of_wolves):
        #  Wolves are to be placed randomly. Set x,y values to null in order to let
        #  these values be randomly defined within the Agent class.   
        _y = None
        _x = None
        # Append wolves to list
        wolves.append(framework.Wolf(wolves,environment, _y, _x))
    return wolves

	
def update(frame_number, wolves, flock, neighbourhood, fig, wolf_threshold, sheep_threshold):
    #print(frame_number) Internal checks
    """Moves agents around the environment domain and allows agents to interact
    .

    This function allows the agents to move randomly across the enivironment 
    domain. As these agents move they reproduce and share resources. 
    In addition, the wolf agents predate on sheep that lie one square over. 
    This behaviour is defined from class methods imported from the framework 
    script

    Args:
        Frame_Number: The iteration of the animation
        Wolves: List containing wolf agents
        Flock: List containing sheep agents
        Neighbourhood: Constant defining the distance at which sheep agents can
        share resources
        wolf_threshold: Number of sheep needed to be consumed for 
                        wolves to reproduce
        sheep_threshold: Store size needed for sheep to reproduce
        

    Returns:
        Fig: A scatter plot of the agents location overlayed onto a heatmap
        of the enviroment at a defined frame number

    Raises:
        Null
    """

    # print(frame_number) internal check to view if framenumber is as expected
    # Randomly shuffle agents
    random.shuffle(flock)
    random.shuffle(wolves)
    fig.clear()
    matplotlib.pyplot.xlim(0, 100)
    matplotlib.pyplot.ylim(0, 100)

    # print(len(flock)) Internal check - to see if flock is size expected
    
    # Loop through all sheep in the flock
    for i in range(len(flock)): 
       flock[i].move()
       flock[i].eat()
       flock[i].share_with_neighbours(neighbourhood)
       flock[i].reproduce(sheep_threshold)
       num_of_sheep = len(flock)
       sheep_plot = matplotlib.pyplot.scatter(flock[i].x, flock[i].y, c = 'white') 
    
    #Return the updated environment which has been nibbled by the sheep
    environment = flock[0].environment           
    
    # Define a blank list, this list will be appended with indices of the sheep 
    # that have been consumed by wolves and hence must be removed from the flock list
    sheep_to_remove = []
    
    # Loop through all the wolves in the pack
    for j in range(len(wolves)):       
       wolves[j].move() 
       # Find index of sheep adjacent to wolves, append this to list
       x = wolves[j].eat(flock)
       if x is not None:   
           sheep_to_remove.append(x)
       wolf_plot = matplotlib.pyplot.scatter(wolves[j].x, wolves[j].y, c = 'black')
       num_of_wolves = len(wolves)
       wolves[j].reproduce(wolf_threshold) 
       
    # Remove sheep that have fallen foul to wolves from flock list   
    if len(sheep_to_remove) >= 1:
        #For loop works in reverse order to avoid index ambuiguity.
        for k in sorted(sheep_to_remove, reverse= True):
            del flock[k]
    matplotlib.pyplot.imshow(environment, cmap = 'RdYlGn')
    scale_bar = matplotlib.pyplot.colorbar()
    scale_bar.set_label('Resources Available',fontsize= 12,rotation =90)
    #Set up chart title and legends
    matplotlib.pyplot.title('Wolves/Sheep Population Model: Iteration {}'.format(frame_number+1),fontsize= 20)
    matplotlib.pyplot.legend((sheep_plot, wolf_plot),
           ('Sheep: {}'.format(num_of_sheep), 'Wolves: {}'.format(num_of_wolves)),
           scatterpoints=1,
           bbox_to_anchor=(1,0), loc="lower right",
           ncol=3,
           fontsize=12)
    #fig.legend()
#    ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.00), shadow=True, ncol=2)


def run(num_of_sheep, num_of_wolves, num_of_iterations, neighbourhood, fig, wolf_threshold, sheep_threshold):
    """Function which runs the actual population model.

    Calling this function runs the population model. This function sets up the 
    required environment and ages. It then calls the relevant behaviours from
    the Framework module and applies these to the defined agents. This is
    simulated within an animation which appears within the model GUI

    Args:
       num_of_sheep: Number of sheep in initial iteration
       num_of_wolves: Number of wolves in initial iteration
       neighbourhood: range at which sheep can share resources
       num_of_iterations: number of moves allowed from each agent
       wolf_threshold: Number of sheep needed to be consumed for 
                        wolves to reproduce
       sheep_threshold: Store size needed for sheep to reproduce

    Returns:
        Animation of the resulting matplotpy graphs in the GUI of the population
        model
    Raises:
        N/A.
    """   
    
    global animation
    environment = create_environment()
    # Create sheep agents
    flock = set_sheep(environment, num_of_sheep)
    # Create wolf agents
    wolves = set_wolves(environment,num_of_wolves)      
    fig = matplotlib.pyplot.figure(figsize=(10, 10))
    # Set animation going
    animation = matplotlib.animation.FuncAnimation(fig, update, interval=500, repeat=False, frames=num_of_iterations, fargs = (wolves, flock, neighbourhood, fig, wolf_threshold, sheep_threshold))
    return fig


if __name__ == "__main__":
    #If main program launch iterations using default values
    #Set default values
    num_of_sheep = 20
    num_of_iterations = 20
    neighbourhood = 20
    num_of_wolves = 20
    fig = matplotlib.pyplot.figure(figsize=(10, 10))
    environment = create_environment()
    #Create sheep agents
    flock = set_sheep(environment, num_of_sheep)
    #Create wolf agents
    wolves = set_wolves(environment,num_of_wolves)      
    fig = matplotlib.pyplot.figure(figsize=(10, 10))
    animation = matplotlib.animation.FuncAnimation(fig, update, interval=500, repeat=False, frames=num_of_iterations, fargs = (wolves, flock, neighbourhood, fig))

    
__author__ = "Michael Gibson"
__copyright__ = "Copyright 201i, Michael Gibson"
__license__ = "MIT"
__version__ = "1"
__maintainer__ = "Michael Gibsosn"
__email__ = "mjggibson4@gmail.com"
__status__ = "Production"    
