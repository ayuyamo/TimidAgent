
from pacman import Directions
from game import Agent, Actions
from pacmanAgents import LeftTurnAgent
from util import manhattanDistance


class TimidAgent(Agent):
    """
    A simple agent for PacMan
    """

    def __init__(self):
        super().__init__()  # Call parent constructor
        # Add anything else you think you need here

    def inDanger(self, pacman, ghost, dist=3):
        """inDanger(pacman, ghost) - Is the pacman in danger
        For better or worse, our definition of danger is when the pacman and
        the specified ghost are:
           in the same row or column,
           the ghost is not scared,
           and the agents are <= dist units away from one another

        If the pacman is not in danger, we return Directions.STOP
        If the pacman is in danger we return the direction to the ghost.
        """
        
        pacman_pos = pacman.getPosition()
        ghost_pos = ghost.getPosition()
        
        if pacman_pos[0] == ghost_pos[0] or pacman_pos[1] == ghost_pos[1]: # Check if the pacman & host or in the same row or column
            if manhattanDistance( ghost_pos, pacman_pos ) <= dist and not ghost.isScared(): # check if their distance <= dist and is the ghost is scared
                pacman_x, pacman_y = pacman_pos # Get x, y positions of pacman
                ghost_x, ghost_y = ghost_pos # Get x, y positions of the ghost
                
                # (dx, dy) is the distance bewteen two agents in vector
                dx = ghost_x - pacman_x
                dy = ghost_y - pacman_y

                direction = Actions.vectorToDirection((dx, dy)) # convert vector to compass direction --> {North, South, East, West, Stop}
                return direction
        
        return Directions.STOP # returned when pacman is not in danger

        raise NotImplemented
    
    def getAction(self, state):
        """
        state - GameState
        
        Fill in appropriate documentation
        """
        
        pacman = state.getPacmanState()
        ghosts = state.getGhostStates()
        
        for ghost in ghosts:
            if self.inDanger(pacman, ghost) != Directions.STOP: # executed if pacman is in danger
                # List of directions the agent can choose from
                legal = state.getLegalPacmanActions()
                heading = pacman.getDirection()
                
                if Directions.REVERSE[heading] in legal:
                    action = Directions.REVERSE[heading]  # Turn around
                elif Directions.LEFT[heading] in legal:
                    action = Directions.LEFT[heading] # Turn left
                elif Directions.RIGHT[heading] in legal:
                    action = Directions.RIGHT[heading] # Turn right 
                elif heading in legal:
                    action = heading
                else:
                    action = Directions.STOP  # Can't move!
            else:  # if pacman is not in danger then it turns left whenever possible
                left_turn_agent = LeftTurnAgent()
                action = left_turn_agent.getAction(state) 
                 
        return action

        raise NotImplemented

