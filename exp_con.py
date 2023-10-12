import random
import argparse

def exp_con(first, second, ll):
    printout = []
    
    char_list = list(first + second)
    for char in range(len(char_list)):
        char_list.append(' ')

    for i in range(len(first), 0, -1):

        my_list = list(first)
        while len(my_list) > i:
            my_list.pop(random.randint(0,len(my_list)-1))
            if len(my_list) > 2:
                index2 = random.randint(0,len(my_list) - 1)
                index3 = random.randint(0,len(my_list) - 1)
                while index2 == index3:
                    index3 = random.randint(0,len(my_list) - 1)
                temp = my_list[index2]
                my_list[index2] = my_list[index3]
                my_list[index3] = temp

        if len(my_list) < len(first):
            printout.append("".join(my_list))

    printout.reverse()

    #for item in printout:
    #    print(item)

    #print(first)
    printout.append(first)
    for i in range(1,ll - len(first)):
        my_list = list(first)
        limit = len(my_list) + i

        while len(my_list) < limit:
            index = random.randint(0,len(my_list))
            if index < len(my_list):
                my_list.insert(index, random.choice(char_list))
            else:
                my_list.append(random.choice(char_list))

            index2 = random.randint(0,len(my_list) - 1)
            index3 = random.randint(0,len(my_list) - 1)
            while index2 == index3:
                index3 = random.randint(0,len(my_list) - 1)
            temp = my_list[index2]
            my_list[index2] = my_list[index3]
            my_list[index3] = temp

        #random.shuffle(my_list)

        my_final_string = ''.join(my_list)
        #print(my_final_string)
        printout.append(my_final_string)

    for item in printout:
        print(item)

    printout = []
    printout.append(second)

    for i in range(1,ll - len(second)):
        my_list = list(second)
        limit = len(my_list) + i

        while len(my_list) < limit:
            index = random.randint(0,len(my_list))
            if index < len(my_list):
                my_list.insert(index, random.choice(char_list))
            else:
                my_list.append(random.choice(char_list))

            index2 = random.randint(0,len(my_list) - 1)
            index3 = random.randint(0,len(my_list) - 1)
            while index2 == index3:
                index3 = random.randint(0,len(my_list) - 1)
            temp = my_list[index2]
            my_list[index2] = my_list[index3]
            my_list[index3] = temp

        #random.shuffle(my_list)

        my_final_string = ''.join(my_list)
        #print(my_final_string)
        printout.append(my_final_string)

    printout.reverse()

    for i in range(len(second), 0, -1):

        my_list = list(second)
        while len(my_list) > i:
            my_list.pop(random.randint(0,len(my_list)-1))
            if len(my_list) > 2:
                index2 = random.randint(0,len(my_list) - 1)
                index3 = random.randint(0,len(my_list) - 1)
                while index2 == index3:
                    index3 = random.randint(0,len(my_list) - 1)
                temp = my_list[index2]
                my_list[index2] = my_list[index3]
                my_list[index3] = temp

        if len(my_list) < len(second):
            printout.append("".join(my_list))
            
    for item in printout:
        print(item)

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('x', type=str, nargs='?', default="OF SHADOW")
    parser.add_argument('y', type=str, nargs='?',default="AND SUBSTANCE")
    parser.add_argument('lim', type=int, nargs='?', default=27)
    args = parser.parse_args()

    #LINE_LIMIT = 27
    #my_string = "OF SUBSTANCE"
    #my_string2 = "AND SHADOW"

    #exp_con(my_string, my_string2, LINE_LIMIT)
    exp_con(args.x, args.y, args.lim)

if __name__ == '__main__':
    main()


