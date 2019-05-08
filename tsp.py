#!/usr/bin/env python3
import argparse
from Graph import Graph, Two_opt
from Node import Node
from csv import reader


def get_data(file_name, class_name):
    """
    read data from csv file and consider it as a node.
    Args:
        file_name (str): name of the file
        class_name (str): name of the algorithm
    Returns:
        class: a class contain a bunch of nodes

    Raises:
        Exception: description

    """
    # using the class knn if the algorithm is 2opt
    if class_name == '2opt':
        knn = Two_opt()
    else:
        knn = Graph()
    try:
        # open the csv file and add the information
        with open(file_name) as csv_file:
            readerable = reader(csv_file)
            # add the nodes to the class
            for row in readerable:
                knn.add_node(Node(row[0], float(row[1]), float(row[2])))
    except Exception:
        print('Invalid file')
        return ' '
    return knn


def handle_parser():
    """
    handle the input from user

    Returns:
        str: description
    """

    parser = argparse.ArgumentParser(usage='./tsp.py <country> [<algorithm>]')
    parser.add_argument('country', help='the start country')
    parser.add_argument('-t', '--type', help='select the algorithm',
                        choices=['K-NN', '2opt'])
    args = parser.parse_args()
    return args


def main():
    """
    run the whole program
    Returns:
        class str: a chain of detailed cities and the whole length
    """
    args = handle_parser()
    if args.country in ['china_cities.csv', 'vietnam_cities.csv',
                        'usa_cities.csv']:
        content = get_data(args.country, args.type)
        # choose the suitable algorithm
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
