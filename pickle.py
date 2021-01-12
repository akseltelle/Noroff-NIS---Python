# Pickle
import pickle, os

for runs in range(0, 3):
    print("Loop {}".format(runs +1))
    data = [0, 1, 2, 3]

    if os.path.isfile("mypickle.dat"):
        print("Loading pickle")
        the_saved_pickle = open("mypickle.dat", "rb")
        data = pickle.load(the_saved_pickle)
        the_saved_pickle.close()
    else:
        print("No pickle to load")

    print("Data before modification:")
    print(data)

    for i in range(0, 4):
        data[i] = data[i] + 1

    print("Data after modification:")
    print(data)

    print("Pickling the data")
    the_new_pickle = open("mypickle.dat", "wb")
    pickle.dump(data, the_new_pickle)
    the_new_pickle.close()
    print("_" * 30)
