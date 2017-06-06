import io
import time

monthDict = ['जनवरी', 'फरवरी', 'मार्च', 'अप्रैल', 'मई', 'जून', 'जुलाई', 'अगस्त', 'सितम्बर', 'अक्टूबर', 'नवंबर',
             'दिसंबर']
numbers = ['एक', 'दो', 'तीन', 'चार', 'पांच', 'छह', 'सात', 'आठ', 'नौ', 'दस']
wrtGivenDate = ['अगले', 'पिछले', 'बाद', 'पहले']
dateAnnotators = ['आज', 'कल', 'परसों', 'दिन', 'हफ्ते', 'महीने', 'साल']
timeOfDay = ['रात', 'सुबह', 'दोपहर', 'शाम', 'दिन', 'रात']
baje = ['बजे']
relationalMarkersAlt = ['ली', 'पहली', 'दूसरी', 'तीसरी', 'चौथी', 'पांचवी', 'छटी', 'सातवीं', 'आठवीं', 'नवी', 'दसवीं']
relationalMarkers = ['वे', 'पहले', 'दुसरे', 'तीसरे', 'चौथे', 'पांचवे', 'छत्ते', 'सातवे', 'आठवे', 'नौंवे ', 'दसवे']


def Timex(file):
    count = 0
    flag = 0
    with io.open('timextag.txt', 'w', encoding='utf-8') as g:
        with open(file, 'r') as f:
            for line in f:
                count += 1
                if count > 1:
                    if count is 2:
                        ab = ''.join(line)
                        ab = ab.split('|')
                        ab = ab[0].split(',')
                        if 'Publish' in ab[0]:
                            flag = 1
                            ab = ab[1].split('(')
                            ab = ab[0].split(' ')
                            ab.pop(0)
                            ab.pop(len(ab) - 1)
                            # print(ab)
                            fin = ' '.join(ab)

                            g.write(fin)
                    else:
                        line = '\n' + line
                        g.write(line)

        f.close()
    g.close()
    return flag


def publishTag(file):
    p = '%d %b %Y %I:%M %p'
    dt = ''
    with open(file, 'r') as f:
        for line in f:
            dt = line
            break
    print(dt)
    dt = dt[:-1]
    a = time.strptime(dt, p)
    # print(a)
    epoch = int(time.mktime(a))
    print(epoch)


def annotate(file):
    with open(file, 'r') as f:
        count = 0
        for line in f:
            print('line: ',line)
            # print(count)
            if count is 0:
                # print(line, type(line))
                pass
                count = 1
            else:
                arr = line.split(' ')
                temp = arr[len(arr) - 1]
                temp = temp[:-1]
                # print(temp)
                arr[len(arr) - 1] = temp
                print(arr)
                for i in range(len(arr)):
                    print(arr[i])
                    if arr[i].isdigit():
                        # print('here')
                        if int(arr[i]) < 13 and arr[i + 1] in baje:
                            print('3', arr[i], arr[i + 1])  # 12 baje
                        # print('here3')
                        if arr[i + 1] in monthDict:
                            # print('here2')
                            if i + 2 < len(arr):
                                if int(arr[i + 2]) < 2017:  # 25 January 2017
                                    print('1', arr[i], arr[i + 1], arr[i + 2])
                            else:  # 25 January
                                print('2', arr[i], arr[i + 1])

                    elif arr[i].split('-')[0].isdigit() and arr[i].split('-')[1].isdigit():
                        print('i hai', i)
                        print(arr[1])
                        if arr[i + 1] in monthDict:  # 25-26 January
                            print('4', arr[i], arr[i + 1])
                        elif arr[i + 2] in timeOfDay:  # 25-26 ki raat
                            print('5', arr[i], arr[i + 1], arr[i + 2])

                    elif arr[i] in monthDict:
                        # print('mila hai: ', arr[i], arr[i + 1])
                        if i+1<len(arr):
                            if int(arr[i + 1]) < 2025:  # January 2017
                                print('6', arr[i], arr[i + 1])
                        else:  # January
                            print('7', arr[i])

                    elif arr[i] in wrtGivenDate:
                        if arr[i + 1] in dateAnnotators:  # Agle mahine
                            print('8', arr[i], arr[i + 1])
                count += 1


# flag = Timex('file_263')
annotate('sample')
# if flag is 1:
#     publishTag('timextag.txt')
