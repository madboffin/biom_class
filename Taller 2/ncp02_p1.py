
import numpy as np

rnd_seq = np.random.choice([True, False], 100000)

# code here
list_f2t = []
cnt = 0

# from second item to end
for k in range(0, len(rnd_seq)-1):
    # adds to counter if false is followed by true
    if (not rnd_seq[k] and rnd_seq[k+1]):
        cnt += 1
        list_f2t.append(k)

print(rnd_seq)
print(cnt)
print(list_f2t)