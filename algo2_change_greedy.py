


def changegreedy(v, a):
    """
    :type v: list - a list where v[i] is the value of the coin of the ith denomination
    :type a: int - the amount of change we are asked to make
    :rtype: list, int
    """

    change_to_make = a
    answer_list = [0] * len(v)

    while change_to_make > 0:
        maxn = max(v)
        position = v.index(maxn)
        if (change_to_make - maxn) >= 0:
            change_to_make -= maxn
            answer_list[position] += 1
        else:
            v.pop()

    min_num_coins = [i for i in answer_list if i != 0]
    min_num_coins = sum(min_num_coins)

    return answer_list, min_num_coins


if __name__ == '__main__':
    # basic tests from assignment pdf
    print(changegreedy([1,2,4,8],15))
    print(changegreedy([1,3,7,12],29))
    print(changegreedy([1,3,7,12],31))
