import xml.etree.ElementTree as ET
import simplejson

tree = ET.parse('data.xml')
root = tree.getroot()

print(root.tag)

final_dict = {}
for child in root:
    # print(child.tag, child.attrib, child.text)
    if child.tag == 'TIMEX3':
        child.attrib.pop('valueFromFunction')
        child.attrib.pop('mod')
        child.attrib.pop('anchorTimeID')
        child.attrib.pop('functionInDocument')
        final_dict[child.text]=child.attrib
        print(final_dict)
        # print(child.attrib)
        tree.write('output.xml')
    elif child.tag == 'EVENT':
        child.attrib.pop('tense')
        child.attrib.pop('aspect')
        final_dict[child.text] = child.attrib
        print(final_dict)
        # print(child.attrib)
        tree.write('output.xml')

json = simplejson.dumps(final_dict,ensure_ascii=False)
print(json)
f = open('output2.txt','w')
f.write(json)