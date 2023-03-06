import laspy
import argparse

#zainicjowanie parsera
parser = argparse.ArgumentParser()

parser.add_argument("--path1")
parser.add_argument("--path2")
parser.add_argument("--index")
parser.add_argument("--output")

#polecenie ktore parsuje argumenty
args = parser.parse_args()

cloud1 = laspy.read(args.path1)
cloud2 = laspy.read(args.path2)

old_class = int(args.index)
classification = cloud1.classification

for i, point in enumerate(classification):
    if point == old_class:
        cloud2.classification[i] = old_class


cloud2.write(args.output)

#cokolwiek