import numpy as np
import copy


class MarkovDecisionProblem:
    def __init__(self, World):
        self.world = World

    def calculate_transition_probability(self, action, state):
        nstates = self.world.nStates
        nrows = self.world.nRows
        forb_indexes = self.world.stateForbiddenIndexes
        term_indexes = self.world.stateTerminalsIndexes
        prob_U = self.world.prob[0]
        prob_L = self.world.prob[1]
        prob_R = self.world.prob[2]

        probability = np.zeros((1, nstates))

        if state not in (forb_indexes + term_indexes):
            if action == "U":  # UP
                if state + nrows <= nstates and (state + nrows) not in forb_indexes:  # look right
                    probability[0][state + nrows - 1] += prob_R
                else:
                    probability[0][state - 1] += prob_R
                if 0 < state - nrows <= nstates and (state - nrows) not in forb_indexes:  # look left
                    probability[0][state - nrows - 1] += prob_L
                else:
                    probability[0][state - 1] += prob_L
                if (state - 1) % nrows > 0 and (state - 1) not in forb_indexes:  # look up
                    probability[0][state - 1 - 1] += prob_U
                else:
                    probability[0][state - 1] += prob_U
            if action == "D":  # DOWN
                if state + nrows <= nstates and (state + nrows) not in forb_indexes:  # look left
                    probability[0][state + nrows - 1] += prob_L
                else:
                    probability[0][state - 1] += prob_L
                if 0 < state - nrows <= nstates and (state - nrows) not in forb_indexes:  # look right
                    probability[0][state - nrows - 1] += prob_R
                else:
                    probability[0][state - 1] += prob_R
                if 0 < state % nrows and (state + 1) not in forb_indexes and (state + 1) <= nstates:  # look up
                    probability[0][state + 1 - 1] += prob_U
                else:
                    probability[0][state - 1] += prob_U
            if action == "R":  # RIGHT
                if state + nrows <= nstates and (state + nrows) not in forb_indexes:  # look up
                    probability[0][state + nrows - 1] += prob_U
                else:
                    probability[0][state - 1] += prob_U
                if 0 < state % nrows and (state + 1) not in forb_indexes and (state + 1) <= nstates:  # look right
                    probability[0][state + 1 - 1] += prob_R
                else:
                    probability[0][state - 1] += prob_R
                if (state - 1) % nrows > 0 and (state - 1) not in forb_indexes:  # look left
                    probability[0][state - 1 - 1] += prob_L
                else:
                    probability[0][state - 1] += prob_L
            if action == "L":  # LEFT
                if 0 < state - nrows <= nstates and (state - nrows) not in forb_indexes:  # look up
                    probability[0][state - nrows - 1] += prob_U
                else:
                    probability[0][state - 1] += prob_U
                if 0 < state % nrows and (state + 1) not in forb_indexes and (state + 1) <= nstates:  # look left
                    probability[0][state + 1 - 1] += prob_L
                else:
                    probability[0][state - 1] += prob_L
                if (state - 1) % nrows > 0 and (state - 1) not in forb_indexes:  # look right
                    probability[0][state - 1 - 1] += prob_R
                else:
                    probability[0][state - 1] += prob_R
        elif state in term_indexes:
            probability[0][state - 1] = 1
        return probability[0]

    def state_action_value_function(self, state, V):
        actions = self.world.actions
        maxs = {key: 0 for key in actions}
        max_a = ""
        action_map = {k: v for k, v in zip(actions, [1, 3, 2, 4])}
        for action in actions:
            if state not in self.world.stateTerminalsIndexes:
                maxs[action] += self.world.rewards[state - 1] + self.world.gamma * np.dot(
                    self.calculate_transition_probability(action, state), V)
            else:
                maxs[action] = self.world.rewards[state - 1]
        maxi = -10 ** 10
        for key in maxs:
            if maxs[key] > maxi:
                max_a = key
                maxi = maxs[key]
        return maxi, action_map[max_a]

    def value_iteration(self, gnuplot):
        theta = 0.0001
        delta = theta + 1
        iter = 0

        V_new = np.zeros((self.world.nStates,))  # values
        P = np.zeros((self.world.nStates, 1))  # policy

        while delta > theta:
            iter = iter + 1
            delta = 0
            V_old = copy.deepcopy(V_new)
            for state in range(1, self.world.nStates + 1):
                V_new[state - 1], P[state - 1] = self.state_action_value_function(state, V_old)
                delta = max(delta, np.abs(V_old[state - 1] - V_new[state - 1]))
                gnuplot.addValue(state - 1, round(V_new[state - 1], 4))
        return V_new, P, iter
