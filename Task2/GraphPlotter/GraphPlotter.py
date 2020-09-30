import matplotlib.pyplot as plt
import numpy as np


def plot(x_list: list, y_list: list):
    """
    :param x_list:
    :param y_list:
    """
    plt.plot(x_list, y_list)
    plt.title('CrossNova Task 2 Graph')
    plt.ylim(-1, 4.5)
    plt.xlim(0, 15)
    plt.show()


def set_graph_x(start, iterations, move_size) -> list:
    """
    sets the x indexes for a graph
    :param start: x[0] in the set
    :param iterations: how many indexes are in the set
    :param move_size: distance between each x in the set
    :return: a list with all the x indexes for the graph
    """
    x_indexes = []
    to_add = start
    for _ in np.arange(start, start + iterations, 1):
        x_indexes.append(to_add)
        to_add += move_size
    return x_indexes


def set_graph_y(start, length, multiplier) -> list:
    """
    sets y indexes for a graph
    :param start: y[0] of the new set of indexes
    :param length: how many points in the sets
    :param multiplier: the multiplier which sets the final height of each index
    :return: a list containing all the new indexes
    """
    y_indexes = []
    half_range = int(length / 2)
    to_add = start + half_range / length ** 2
    for index in range(half_range):
        if index % 2 == 0:
            y_indexes.append(to_add)
        else:
            y_indexes.append(to_add * -1)
        to_add = to_add + (half_range - index) / length ** 2 * multiplier
    for index in range(half_range, 0, -1):
        if index % 2 == 0:
            y_indexes.append(to_add)
        else:
            y_indexes.append(to_add * -1)
        to_add = to_add - (half_range - index) / length ** 2 * multiplier
    return y_indexes


if __name__ == '__main__':
    xs = []
    ys = []
    set_size = 20
    last = 0
    for i in range(10):
        new_x_loop_indexes = set_graph_x(last, set_size, 0.07)
        new_y_loop_indexes = set_graph_y(0, set_size, 7)
        for i in range(len(new_y_loop_indexes)):
            new_y_loop_indexes[i] = new_y_loop_indexes[i] + (new_x_loop_indexes[i] * 0.2)
        last = new_x_loop_indexes[len(new_x_loop_indexes) - 1]
        xs.extend(new_x_loop_indexes)
        ys.extend(new_y_loop_indexes)
    plot(xs, ys)
