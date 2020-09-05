import language_model
import permutation
import simulated_annealing
import time

def main():
    # start_time = time.time()
    print("starting program")
    reader = language_model.corpusReader("http://www.gutenberg.org/files/76/76-0.txt")
    lngmodel = language_model.LanguageModel(reader)
    txt = open("problemset_06_encrypted_input.txt","r")
    msg = str(txt.read())
    txt.close()
    perm= dict()
    T = {",", ".", ":", "\n", "#", "(", ")", "!", "?", "\'", "\"", " "}
    letters = "abcdefghijklmnopqrstuvwxyz"
    for letter in letters:
        perm[letter] = letter
    for t in T:
        perm[t] = t

    p = permutation.permutation(perm)
    print("start simulated_annealing")
    sim = simulated_annealing.SimulatedAnnealing(300, 0.00001, 0.9990)
    h = sim.run(p, msg, lngmodel)
    # start_time = (time.time() - start_time)/60
    # print("exacution took: "+str(start_time))
    print(h.translate(msg))
    print(h.mapChar)


main()
