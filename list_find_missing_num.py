# How do you find the missing number in a given integer array of 1 to 100?
# Note: The 99 numbers were readomly added into the list, so there is no order.
import random as random
import numpy as np

# Preparation: generate a list of ramdomly placed numbers within [1, 100], with one missing
m = int(input('specify a missing number within [1,100], I\'ll find it. : '))
s = [x for x in range(1,101) if x != m]
random.shuffle(s)
print('the input list: \n', s)

# find the missing one. This algorithm actually has only one line code here.
missing = int((1+100)*100/2) - sum(s)

print('\n the missing number =', missing)