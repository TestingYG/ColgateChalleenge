import string
import re

def CleanUp(string):
    # string = re.sub("[0-9](?=[^)(]*\))", "", string)

    # v1
    string = re.sub(" ", "", string)
    string = re.sub("\(", ",", string)
    string = re.sub("\)$", "", string)
    string = re.sub("\),", ",", string)
    string = re.sub("\)", ",", string)
    string = re.sub(",,", ",", string)

    string = re.sub("activeingredients:,", "", string)
    string = re.sub("activeingredients,", "", string)
    string = re.sub("activeingredients:", "", string)
    string = re.sub("activeingredients", "", string)

    string = re.sub("inactiveingredients:,", "", string)
    string = re.sub("inactiveingredients,", "", string)
    string = re.sub("inactiveingredients:", "", string)
    string = re.sub("inactiveingredients", "", string)

    string = re.sub("otheringredients:,", "", string)
    string = re.sub("otheringredients,", "", string)
    string = re.sub("otheringredients:", "", string)
    string = re.sub("otheringredients", "", string)

    string = re.sub("medicinalingredients:,","", string)
    string = re.sub("medicinalingredients,","", string)
    string = re.sub("medicinalingredients:","", string)
    string = re.sub("medicinalingredients","", string)

    string = re.sub("others:,","", string)
    string = re.sub("others,","", string)
    string = re.sub("others:","", string)
    string = re.sub("others","", string)

    string = re.sub("/", ",", string)
    string = re.sub("and/or", ",", string)

    string = string.split(",")

    dic = {}
    for x in string:
        if x not in dic:
            dic[x] = 1
        else:
            dic[x] +=1

    return dic

    #v2
    # string0 = re.findall("active ingredients:.*",  string)
    # string1 = re.findall("other ingredients:.*",  string)
    # string2 = re.findall("ingredients:.*",  string)
    # string3 = re.findall("other ingredients:.*", string)
    # string4 = re.findall("medicinal ingredients:.*",string)
    # string5 = re.findall("others.*", string)
    # string6 = re.findall("othes.*", string)
    # string7 = re.findall("other:.*", string)
    # string8 = re.findall("(active)", string)

    #v3
    # string = string.replace(",", " ")
    # string = string.split(" ")
    # dic = {}
    #
    # with open("newwordp2.txt", "r") as f:
    #     crap = f.read()
    #
    # crap = crap.split(" ")
    #
    #
    # for x in string:
    #     if x not in crap:
    #         if x not in dic:
    #             dic[x] = 1
    #         else:
    #             dic[x] +=1
    #
    #
    # return dic

    #v4

    # stringa = stringa.replace(",", " ")
    # dic = {}
    #
    # with open("newwordp2.txt", "r") as f:
    #     crap = f.read()
    #
    # translator = re.compile('[%s]' % re.escape(string.punctuation))
    #
    # stringa = stringa.replace(",", " ")
    # stringa = translator.sub(' ', stringa)
    # stringa = re.sub("[0-9]", " ", stringa)
    # crap = re.sub("[0-9]", " ", crap)
    # crap = translator.sub(' ', crap)
    # stringa = stringa.split(" ")
    #
    # dic = {}
    #
    # for x in stringa:
    #     if x not in crap:
    #         if x not in dic:
    #             dic[x] = 1
    #         else:
    #             dic[x] +=1
    #
    # return dic
