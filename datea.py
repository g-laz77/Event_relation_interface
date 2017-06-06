monthDict = ['जनवरी', 'फरवरी', 'मार्च', 'अप्रैल', 'मई', 'जून', 'जुलाई', 'अगस्त', 'सितम्बर', 'अक्टूबर', 'नवंबर', 'दिसंबर']
monthDictAlt = ['दिसम्बर', 'नवम्बर']
numbers = ['एक', 'दो', 'तीन', 'चार', 'पांच', 'छह', 'सात', 'आठ', 'नौ', 'दस']
wrtGivenDate = ['अगले', 'पिछले', 'बाद', 'पहले']
dateAnnotators = ['आज', 'कल', 'परसों', 'दिन', 'हफ्ते', 'सप्ताह', 'महीने', 'साल', 'वर्ष', 'शताब्दी']
timeOfday = ['रात', 'सुबह', 'दोपहर', 'शाम', 'दिन', 'रात']
relationalMarkers = ['वे', 'पहले', 'दुसरे',  'तीसरे', 'चौथे', 'पांचवे', 'छत्ते', 'सातवे', 'आठवे', 'नौंवे ', 'दसवे']
baje = ['बजे']
def dateRegex(date):
    #date2 = "12 मार्च"
    dateList = date.split(',')[0].split(' ')
    if (dateList[0]+" "+dateList[1] != date):
        dateList.append(date.split(',')[1].strip())

    month = dateList[1]
    epochDate = str(dateList[0]) + "/"
    i = 0
    #print (dateList)
    while i < 12:
        if (monthDict[i] == month):
            epochDate = epochDate + str(i+1) + "/"
            break
        else:
            i+=1
    if len(dateList) == 3:
        epochDate = epochDate + str(dateList[2])
    #print (dateList[2])
    print (epochDate)

dateRegex("1 जून, 2017")
