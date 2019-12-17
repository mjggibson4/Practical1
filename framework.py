#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Script which defines the properties and behaviours of the wolves and sheep 
agents within the population model.

This script sets up a generic agent class. This defines how the agents move
within the model. Leave one blank line.  The rest of this docstring should contain an
overall description of the module or program.  Optionally, it may also
contain a brief description of exported classes and functions and/or usage
examples.
"""

# Import required modules
import random


class Agent:
    """Agent class, used to define a generic agent within the model

    Agent class, used to define the methods which are common to both the wolves
    and sheep agents. This class is used to initialise these classes and acts
    as a parent class from which methods are inherited. If x and y coordinates 
    of these agents are null, then these are randomly assigned

    Attributes:
        agents: list of agents
        enviroment: This list models the enviroment in which agents 
        will be moving and interacting with.
        _y: y coordinate of agent
        _x: x coordinate of agent
        store: represents the amount of "assets" or "food" stored by agent
    """

    def __init__(self, agents, environment, _y, _x):
        """Inits Agent with environment, agents, _y and _x."""
    
        import random
        # If x null assign random value
        if (_x == None):
            self.x = random.randint(0,100)
        else:
            self.x = _x
        # If y null assign random value    
        if (_y == None):
            self.y = random.randint(0,100)
        else:
            self.y = _y
        self.environment = environment
        self.agents = agents
        self.store = 0




    def move(self):
        """Randomly moves agents around environment. This process defines a 
          randomand based on this moves the agent vertically. Similarly this is 
          repeated for horizontal movement as well. Code is defined in a manner 
          such that the domain of the enviroment is respected meaning that agents 
          can not escape this domain"""
#    if self.y == 100:
#             self.y = (self.y - 1) % 100
#    elif self.y == 0:
#             self.y = (self.y + 1) % 100
#    elif random.random() < 0.5:
#             self.y = (self.y + 1) % 100
#    else:
#             self.y = (self.y - 1) % 100
##set these to be temporary variables
#    if self.x == 100:
#             self.x = (self.x - 1) % 100
#    elif self.x == 0:
#             self.x = (self.x + 1) % 100
#    elif random.random() < 0.5:
#             self.x = (self.x + 1) % 100
#    else:
#             self.x = (self.x - 1) % 100
    # If object is at boundary conditions, move it away from edge             
        if self.y == 100 or self.y == 0:
            if self.y == 100:
                 self.y = (self.y - 1) % 100
            else:
                 self.y = (self.y + 1) % 100
        # Else move object in a random manner
        else:
            if random.random() < 0.5:
                 self.y = (self.y + 1) % 100
            else:
                 self.y = (self.y - 1) % 100
                 
                 
        # If object is at boundary conditions, move it away from edge          
        if self.x == 100 or self.x == 0:
            if self.y == 100:
                 self.x = (self.x - 1) % 100
            else:
                 self.x = (self.x + 1) % 100
        # Else move object in a random manner         
        else:
            if random.random() < 0.5:
                 self.x = (self.x + 1) % 100
            else:
                 self.x = (self.x - 1) % 100
                 
             
        
            
    

class Sheep(Agent):
    """Sheep agent class, used to define a sheep object. Child class of agent. 

    Sheep agent class, used to define the methods which are unique to sheep
    agents such as eating and reproduction. All attributes defined within 
    agents are inherited within this class.

    Attributes (Inherited from Class Agent)
        agents: list of agents
        enviroment: This list models the enviroment in which agents 
        will be moving and interacting with.
        _y: y coordinate of agent
        _x: x coordinate of agent
        store: represents the amount of "assets" or "food" stored by agent
    """
    def __init__(self, agents, environment, _y, _x):
        # Inherit all attributes defined within class Agent  
        Agent.__init__(self, agents, environment, _y, _x) 

 

    def eat(self):
      """Allows sheep to consume environemt and store these units within the
      agents personal store 10 units at the time. If the enviroment contains
      less that ten unit, sheep consumes all that is available"""
      if self.environment[self.y][self.x] >= 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
      else:
            self.store = self.environment[self.y][self.x]
            self.environment[self.y][self.x]=0
    

    
    def share_with_neighbours(self, neighbourhood):
         """Allows sheep lying within a defined distance to one another to equally
         share their stores.
          
         Args:
             Neighbourhood: Constant defining the distance at which sheep agents can
                            share resources
         """  
         for agent in self.agents:  
             # Calculate the distance between sheep and all other sheep in 
             # flock
             dist = self.distance_between(agent)
             #If this distance is less than user defined distance, share stores
             if dist <= neighbourhood:
                 sum = self.store + agent.store
                 ave = sum /2
                 self.store = ave
                 agent.store = ave
                 #print("sharing " + str(dist) + " " + str(ave))
             

 

    def distance_between(self, agent):
         """Calculates euclidean distance between two agents and returns this
         distance""" 
         return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5

    def reproduce(self, sheep_threshold):
          """If sheep store is greater or equal to the reproduction threshold
          append a copy of the agent to the flock and reset stores to 0
          
          Args:
              sheep_threshold: Store size needed for sheep to reproduce""" 
          if self.store >= sheep_threshold:
             self.store = 0
             self.agents.append(Sheep(self.agents,self.environment, self.y, self.x))
     

class Wolf(Agent):
    """Wolf agent class, used to define a wolf object. Child class of agent. 

    Wolf agent class, used to define the methods which are unique to wolf
    agents such as eating and reproduction. All attributes defined within 
    agents are inherited within this class.

    Attributes (Inherited from Class Agent)
        agents: list of agents
        enviroment: This list models the enviroment in which agents 
        will be moving and interacting with.
        _y: y coordinate of agent
        _x: x coordinate of agent
        store: represents the amount of "assets" or "food" stored by agent
    """
    def __init__(self, agents, environment, _y, _x):
    # Inherit all attributes defined within class Agent:
        Agent.__init__(self, agents, environment, _y, _x)
    
        
    def distance_between(self, agent, x, y):
        """Calculates euclidean distance between two agents and returns this
        distance""" 
        return (((self.x - x)**2) + ((self.y - y)**2))**0.5
     
    
    def eat(self, Sheep):
        """Allows wolfs to consume sheep agents that are adjacent to themselves.
         
        Args: 
             Sheep: List of sheep agents
             
        Returns:
             i = index of sheep which have been consumed
          
        """
        # Extract x,y coords from sheep list
        for i in range(len(Sheep)):
            x = Sheep[i].x
            y = Sheep[i].y
            # Calculate distance of wolf to every sheep within flock
            for agent in self.agents:
             dist = self.distance_between(agent, x, y)    
             # If sheep is adjacent to wolf, return it index and increase wolf
             # store by 1
             if dist <= (2)**0.5:
                 self.store += 1
                 return i
                 break
             
    def reproduce(self, wolf_threshold):
          """If wolf store is greater or equal to the reproduction threshold
          append a copy of the agent to the wolf pack and reset stores to 0
          
          Args:
             wolf_threshold: Store size needed for sheep to reproduce"""    
          if self.store >= wolf_threshold:
              self.store = 0
              self.agents.append(Wolf(self.agents,self.environment, 
                                      self.y, self.x))

__author__ = "Michael Gibson"
__copyright__ = "Copyright 201i, Michael Gibson"
__license__ = "MIT"
__version__ = "1"
__maintainer__ = "Michael Gibsosn"
__email__ = "mjggibson4@gmail.com"
__status__ = "Production"  
             

        
        

    
        
