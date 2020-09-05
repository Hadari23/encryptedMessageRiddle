import random
import math

class permutation:

    def __init__(self,mapChar):
        self.mapChar = mapChar

    def get_neighbor(self):
        newPerm = self.mapChar.copy()
        keys = newPerm.keys()
        chosen = random.choices(list(keys),k=2)
        chosen = list(chosen)
        temp = newPerm[chosen[0]] #contains the value of chosen[0]
        newPerm[chosen[0]] = newPerm[chosen[1]]
        newPerm[chosen[1]] = temp
        retperm = permutation(newPerm)
        return retperm

    def translate(self, text):
        decrypted = ""
        for c in text:
            decrypted += self.mapChar[c]
        return decrypted

    def get_energy(self, data, model):
        data = self.translate(data)
        energy = 0
        # model.dict is the mapping from a string to probability
        calc = -math.log(model.unigramLaplace[data[0]],2)
        energy += calc
        for i in range(1,len(data)):
            calc = -math.log(model.bigramLaplace[str(data[i-1]) + str(data[i])], 2)

            energy += calc


        return energy
