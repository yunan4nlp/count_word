import sys


def read_corpus(path):
    inFile = open(path, mode="r", encoding="utf8")
    sent_num = 0
    word_num = 0

    min_len = 100000
    max_len = -1
    for line in inFile.readlines():
        sent_num += 1
        line = line.strip()
        words = line.split(" ")
        tmp_num = len(words)
        word_num += tmp_num
        if min_len > tmp_num:
            min_len = tmp_num
        if max_len < tmp_num:
            max_len = tmp_num
    inFile.close()
    print("word num: " + str(word_num))
    print("sent num: " + str(sent_num))

    print("max num: " + str(max_len))
    print("min num: " + str(min_len))
    print("avg: " + str(word_num / sent_num))

read_corpus(sys.argv[1])
