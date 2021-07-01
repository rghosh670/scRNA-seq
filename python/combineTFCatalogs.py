f = open('data/tf2.txt', 'r')
tf = f.read().split()
f.close()

f = open('data/transcriptionFactors.txt', 'r')
tf2 = f.read().split()
f.close()

final = tf + list(set(tf2) - set(tf))
print(len(final))


with open('data/transcriptionFactors2.txt', 'w') as f: # write out results to text file
    for item in final:
        f.write("%s\n" % item)

f.close()