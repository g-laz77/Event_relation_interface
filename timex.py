import io
import time, os

monthDict = ['जनवरी', 'फरवरी', 'मार्च', 'अप्रैल', 'मई', 'जून', 'जुलाई', 'अगस्त', 'सितम्बर', 'अक्टूबर', 'नवंबर',
             'दिसंबर']
numbers = ['एक', 'दो', 'तीन', 'चार', 'पांच', 'छह', 'सात', 'आठ', 'नौ', 'दस']
wrtGivenDate = ['अगले', 'पिछले', 'बाद', 'पहले']
dateAnnotators = ['आज', 'कल', 'परसों', 'दिन', 'हफ्ते', 'महीने', 'साल']
timeOfDay = ['रात', 'सुबह', 'दोपहर', 'शाम', 'दिन', 'रात']


def Timex(file):
    count = 0
    with io.open('timextag.txt', 'w', encoding='utf-8') as g:
        with open(file, 'r') as f:
            for line in f:
                count += 1
                if count > 1:
                    if count is 2:
                        ab = ''.join(line)
                        ab = ab.split('|')
                        ab = ab[0].split(',')
                        ab = ab[1].split('(')
                        ab = ab[0].split(' ')
                        ab.pop(0)
                        ab.pop(len(ab) - 1)
                        print(ab)
                        fin = ' '.join(ab)

                        g.write(fin)
                    else:
                        line = '\n' + line
                        g.write(line)

        f.close()
    g.close()


def publishTag(file):
    p = '%d %b %Y %I:%M %p'

    with open(file, 'r') as f:
        for line in f:
            dt = line
            break
    # print(dt,type(dt),dt.split())
    dt = dt[:-1]
    a = time.strptime(dt, p)
    # print(a)
    epoch = int(time.mktime(a))
    # print(epoch)


def annotate(file):
    with open(file, 'r') as f:
        for line in f:
            print(line)
            pass


Timex('file_27')
annotate('timextag.txt')
publishTag('timextag.txt')
