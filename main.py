#!/usr/bin/python3
# -*- coding: UTF-8 -*-


import sys

intonations = {
    'a':'aāáǎà',
    'e':'eēéěè',
    'i':'iīíǐì',
    'u':'uūúǔù',
    'o':'oōóǒò',
    'v':'üǖǘǚǜ'
    }

'''
j q x y真淘气，从不和u在一起；
见了小ü更淘气，吹走小ü的圆泡泡。

先标ɑ o e，再标 i u ü。
i、u并列标在后，i上标调把点抹，
轻声不标就空着。
'''

yy = 'aeiouv'
from_file = False
buffer =  None
wf = ''

def topy(s):
    n=int(s[-1])
    s=s[0:-1]
    if 'v' in s:
        toc=False
        for ch in ('j','q','x','y'):
            if ch in s:
                toc=True
        if (toc): s=s.replace('v','u')
    if 'a' in s:
        return s.replace('a',intonations['a'][n])
    elif 'o' in s:
        return s.replace('o',intonations['o'][n])
    elif 'e' in s:
        return s.replace('e',intonations['e'][n])
    elif 'i' in s:
        if 'u' in s:
            i_pos = s.find('i')
            u_pos = s.find('u')
            if u_pos>i_pos: return s.replace('u',intonations['u'][n])
        return s.replace('i',intonations['i'][n])
    elif 'u' in s:
        return s.replace('u',intonations['u'][n])
    else:
        return s.replace('v',intonations['v'][n])

def init(ff,tf):
    global from_file, rf, wf, buffer
    from_file=True
    with open(ff,'r') as rf:
        buffer = iter(rf.readlines())
    wf=open(tf,'w')

def next_s():
    if from_file:
        try:
            return next(buffer)
        except StopIteration:
            return 'quit'
    else:
        return input()

def write_r(result):
    if from_file:
        wf.write(result)
    else:
        print(result)
        
        
def main():
    if len(sys.argv)>=3:
        init(sys.argv[1],sys.argv[2])
    while(True):
        s=next_s()
        result=''
        if s=='quit': break
        p = 0
        last_word = ''
        while p<len(s):
            last_word += s[p]
            if s[p].isdigit():
                result+=topy(last_word)
                last_word=''
            p+=1
        if last_word:
            result+=topy(last_word+'0')
        write_r(result)
    if from_file:wf.close()

if __name__ == '__main__':
    main()
