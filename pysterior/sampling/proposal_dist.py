import abc
from math import log

import numpy as np


class AbstractProposalDistribution(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def transition_log_probability(self, current_state, new_state):
        """Return the log likelihood of a transition under this proposal distribution."""

    @abc.abstractmethod
    def propose(self, current_state):
        """Propose a new state given the current state."""

class MetropolisProposal(AbstractProposalDistribution):
    def transition_log_probability(self, current_state, new_state):
        return log(1.0)

class GaussianMetropolisProposal(MetropolisProposal):
    def __init__(self, sigma):
        self.sigma = sigma

    def propose(self, current_state):
        return np.random.normal(current_state, self.sigma)

class SphereGaussianMetropolisProposal(AbstractProposalDistribution):
    def __init__(self, sigma, number_of_parameters):
        self.sigma = sigma
        self.number_of_parameters = number_of_parameters

    def propose(self, current_state):
        return np.array([np.random.normal(x, self.sigma) for x in current_state])

    def transition_log_probability(self, current_state, new_state):
        return 0.0