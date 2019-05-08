#!/bin/python3
import argparse
from Graph import Graph, Two_opt
from Node import Node
from csv import reader


def get_data(file_name, class_name):
    if class_name == '2opt':
        knn = Two_opt()
    else:
        knn = Graph()
    with open(file_name) as csv_file:
        readerable = reader(csv_file)
        for row in readerable:
            knn.add_node(Node(row[0], float(row[1]), float(row[2])))

    return knn


def handle_parser():
    parser = argparse.ArgumentParser(usage='./tsp.py <country> [<algorithm>]')
    parser.add_argument('country', help='the start country')
    parser.add_argument('-t', '--type', help='select the algorithm',
                        choices=['K-NN', '2opt'])
    args = parser.parse_args()
    return args


def main():
    args = handle_parser()
    if args.country in ['china_cities.csv', 'vietnam_cities.csv',
                        'usa_cities.csv']:
        content = get_data(args.country, args.type)
        if args.type == '2opt':
            solution, len = Two_opt.two_opt(content)
            print(solution)
            print(len)
        else:
            solution, total_len = content.k_nearest_neighbor()
            print(solution)
            print(total_len)
    else:
        print("Invalid file")
        return


if __name__ == '__main__':
    main()