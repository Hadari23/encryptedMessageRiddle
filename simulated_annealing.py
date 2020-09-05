import math
import random

class SimulatedAnnealing:

    def __init__(self, temp = 100, threshold = 1/1000, alpha = 0.995):
        self.temp = temp
        self.threshold = threshold
        self.alpha = alpha

    def run(self, hyp, msg, lngModel):
        # hyp is a permutation
        # msg is a string
        # lngModel is a language model
        T = self.temp
        while T > self.threshold:
            h = hyp.get_neighbor()
            delta = h.get_energy(msg,lngModel) - hyp.get_energy(msg,lngModel)
            if delta < 0:
                p = 1
            else:
                p = math.exp((-delta)/T)
            r = random.random()
            if r < p:
                hyp = h
            T = self.alpha * T

        return hyp
