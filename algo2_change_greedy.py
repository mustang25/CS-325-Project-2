


def changegreedy(v, a):
    """
    :type v: list - a list where v[i] is the value of the coin of the ith denomination
    :type a: int - the amount of change we are asked to make
    :rtype: list, int
    """

    change_to_make = a
    working_list = v[:]
    answer_list = [0] * len(working_list)

    while change_to_make > 0:
        maxn = max(working_list)
        position = working_list.index(maxn)
        if (change_to_make - maxn) >= 0:
            change_to_make -= maxn
            answer_list[position] += 1
        else:
            working_list.pop()

    min_num_coins = [i for i in answer_list if i != 0]
    min_num_coins = sum(min_num_coins)

    return answer_list, min_num_coins


def question_3():


    list_of_a = list(range(2010, 2205, 5))

    for a in list_of_a:
        v = [1, 5, 10, 25, 50]
        answer_list, min_num_coins = changegreedy(v, a)
        print("{}\t{}".format(a, min_num_coins))

def question_4():


    list_of_a = list(range(2000, 2201, 1))
    v1 = [1, 2, 6, 12, 24, 48, 60]
    v2 = [1, 6, 13, 37, 150]

    for a in list_of_a:

        vc1 = list(v1)
        vc2 = list(v2)

        answer_list, min_num_coins1 = changegreedy(vc1, a)
        answer_list, min_num_coins2 = changegreedy(vc2, a)
        print("{}\t{}\t{}".format(a, min_num_coins1, min_num_coins2))

def question_5():


    list_of_a = list(range(2000, 2201, 1))

    for a in list_of_a:
        v = list(range(0, 31, 2))
        v[0] = 1

        answer_list, min_num_coins = changegreedy(v, a)
        print("{}\t{}".format(a, min_num_coins))



if __name__ == '__main__':
    # basic tests from assignment pdf
    print(changegreedy([1,2,4,8],15))
    print(changegreedy([1,3,7,12],29))
    print(changegreedy([1,3,7,12],31))

    #question_3()
    # question_4()
    question_5()



