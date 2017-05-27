import xml.etree.ElementTree as ET
import simplejson


def extractor(filename):
    tree = ET.parse(filename)
    root = tree.getroot()

    print(root.tag)

    final_dict = {}
    for child in root:
        #print(child)
        # print(child.tag, child.attrib, child.text)
        if child.tag == 'TIMEX3':
            child.attrib.pop('valueFromFunction')
            child.attrib.pop('mod')
            child.attrib.pop('anchorTimeID')
            child.attrib.pop('functionInDocument')
            final_dict[child.text] = child.attrib
            # print(final_dict)
            # print(child.attrib)
<<<<<<< HEAD
            tree.write('output.xml')
=======
            tree.write('output2.xml', encoding="UTF-8", xml_declaration=True)
>>>>>>> f5296e8d24f8f782696d88eb05ee665a82a853f6
        elif child.tag == 'EVENT':
            child.attrib.pop('tense')
            child.attrib.pop('aspect')
            final_dict[child.text] = child.attrib
            # print(final_dict)
            # print(child.attrib)
<<<<<<< HEAD
            tree.write('output.xml')
=======
            tree.write('output2.xml', encoding="UTF-8", xml_declaration=True)
>>>>>>> f5296e8d24f8f782696d88eb05ee665a82a853f6

    json = simplejson.dumps(final_dict, ensure_ascii=False)

    # f = open('output.txt','w+')
    # f.write(json)
    return json
<<<<<<< HEAD
    l = open(filename, "w")

extractor("data.xml")
=======


extractor('data.xml')
>>>>>>> f5296e8d24f8f782696d88eb05ee665a82a853f6
