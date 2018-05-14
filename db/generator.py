from random import randint as ri

def gen_acc():
    acc = '40708810'
    for i in range(12):
        acc += str(ri(0,9))
    return acc

def gen_card():
    card = '4373'
    for i in range(12):
        card += str(ri(0,9))
    return card

def gen_num():
    num = '7'
    for i in range(10):
        num += str(ri(0,9))
    return num

with open('table.csv', 'a') as file:
    for i in range(20):
        file.write('"' + gen_num() + '";"";"'+ str(i+1) \
                   + '";"' + gen_acc() + '";"' + gen_card() + '"\n')

