import xml.etree.ElementTree as ET
import simplejson


def extractor(filename):
    tree = ET.parse(filename)
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
            child.text = child.text + '_' + child.attrib['tid']
            final_dict[child.text] = child.attrib
            # print(final_dict)
            # print(child.attrib)
            tree.write('output2.xml', encoding="UTF-8", xml_declaration=True)
        elif child.tag == 'EVENT':
            child.attrib.pop('tense')
            child.attrib.pop('aspect')
            child.text = child.text + '_' + child.attrib['eid']
            final_dict[child.text] = child.attrib
            # print(final_dict)
            # print(child.attrib)
            tree.write('output2.xml', encoding="UTF-8", xml_declaration=True)

    json = simplejson.dumps(final_dict, ensure_ascii=False)

    # f = open('output.txt','w+')
    # f.write(json)
    return json


extractor('data.xml')
