import matplotlib.pyplot as plt


def plot(x_list: list, y_list: list):
    """
    :param x_list:
    :param y_list:
    """
    plt.plot(x_list, y_list)
    plt.title('CrossNova Task 2 Graph')
    plt.show()


def calc_graph_indexes(indexes_range: int, split_num: int) -> list:
    """

    :param split_num:
    :type indexes_range: int
    :return:
    """
    each_cycle = int(indexes_range / split_num)
    list_x = []
    list_y = []
    for i in range(split_num):
        # print(len(list_x))
        if len(list_x) == 0:
            start_x_index = 0
        else:
            start_x_index = list_x[len(list_x) - 1]
        list_x.extend([x_index for x_index in range(start_x_index, each_cycle + start_x_index)])
        list_y.extend([y_index if y_index % 2 == 0 else y_index * -1 for y_index in range(int(each_cycle / 2))])
        list_y.extend([y_index if y_index % 2 == 0 else y_index * -1 for y_index in range(int(each_cycle / 2), 0, -1)])
    return list_x, list_y


if __name__ == '__main__':
    xs, ys = calc_graph_indexes(250, 5)
    plot(xs, ys)
