from util import manhattanDistance
from game import Directions, Actions
import random, util

from game import Agent
from pacman import GameState


BIGNUM = 10000
class DumbAgent(Agent):
    def getAction(self, state):
   
        print("Location: ", state.getPacmanPosition())
        print("Actions available: ", state.getLegalPacmanActions())
        if Directions.EAST in state.getLegalPacmanActions():
            print("Going East.") 
            return Directions.EAST
        else:
                print("Stopping.")
                return Directions.STOP 


class RandomAgent(Agent):
    def getAction(self, state):
   
        print("Location: ", state.getPacmanPosition())
        print("Actions available: ", state.getLegalPacmanActions())
        availableActions = state.getLegalPacmanActions()
        action = random.choice(availableActions)
        return action

class BetterRandomAgent(Agent):
    def getAction(self, state):
        print("Location: ", state.getPacmanPosition()) 
        availableActions = state.getLegalPacmanActions()
        availableActions = availableActions[:-1]
        # print("Actions available: ", availableActions) 
        print("Actions available: ", state.getLegalPacmanActions())
        action = random.choice(availableActions)
        return action

class ReflexAgent(Agent):
 
    def getAction(self, gameState):
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalPacmanActions()
        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices)  # Pick randomly among the best
        return legalMoves[chosenIndex]
    def evaluationFunction(self, currentgameState, action):
    # Useful information you can extract from a gameState (pacman.py)
        successorgameState = currentgameState.generatePacmanSuccessor(action)
        newPos = successorgameState.getPacmanPosition()
        newFood = successorgameState.getFood()
        newGhostStates = successorgameState.getGhostStates()
        foodNum = currentgameState.getFood().count()
        if len(newFood.asList()) == foodNum:  # if this action does not eat a food 
            dis = 1000
            for pt in newFood.asList():
                if manhattanDistance(pt , newPos) < dis :
                    dis = manhattanDistance(pt, newPos)
        else:
            dis = 0
        for ghost in newGhostStates:  # the impact of ghost surges as distance get close
            dis += 4 ** (2 - manhattanDistance(ghost.getPosition(), newPos))
        return -dis 
# class ReflexAgent(Agent):
#  def registerInitialState(self, state):
#         return;

#     # GetAction Function: Called with every frame
#  def getAction(self, state):
#         # get all legal actions for pacman
#         legal = state.getLegalPacmanActions()
#         # get all the successor state for these actions
#         successors = [(state.generatePacmanSuccessor(action), action) for action in legal]
#         # evaluate the successor states using scoreEvaluation heuristic
#         scored = [(scoreEvaluation(state), action) for state, action in successors]
#         # get best choice
#         bestScore = max(scored)[0]
#         # get all actions that lead to the highest score
#         bestActions = [pair[1] for pair in scored if pair[0] == bestScore]
#         # return random action from the list of the best actions
#         return random.choice(bestActions)
