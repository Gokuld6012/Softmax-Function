import numpy as np

def softmax(sc):
    y_x = np.exp(sc - np.max(sc))
    return y_x / y_x.sum()

#scores = [3.0,1.0,0.2]
#scores = [3.0,1.0,0.2]
#print(softmax(scores))

print "Enter the values for softmax in spaces"

scores = raw_input()
input_list = scores.split() #splits the input string on spaces
# process string elements in the list and make them integers
input_list = [float(a) for a in input_list] 


print(softmax(input_list))