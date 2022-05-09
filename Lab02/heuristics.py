def scoreEvaluation(state):
    return state.getScore() + [0,-1000.0][state.isLose()] + [0,1000.0][state.isWin()]