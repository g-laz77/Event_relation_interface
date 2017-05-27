import xml.etree.ElementTree as ET
import simplejson, io, re


def extractor(filename):
    tree = ET.parse(filename)
    root = tree.getroot()

    # print(root.tag)

    final_dict = {}
    for child in root:
        # print(child)
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
            tree.write('output.xml', encoding="UTF-8", xml_declaration=True)
        elif child.tag == 'EVENT':
            child.attrib.pop('tense')
            child.attrib.pop('aspect')
            child.text = child.text + '_' + child.attrib['eid']
            final_dict[child.text] = child.attrib
            # print(final_dict)
            # print(child.attrib)
            tree.write('output.xml', encoding="UTF-8", xml_declaration=True)

    with open('output.xml', 'r') as f:
        con = f.read()

    m = re.findall(r'<[^<>]*>', con)
    for i in range(len(m)):
        con = con.replace(m[i], '')
    print(type(con))
    with io.open('strip.txt', 'w', encoding='utf-8') as f:
        f.write(con)
    f.close()
    count = 0
    with io.open('final.txt', 'w', encoding='utf-8') as g:
        with open('strip.txt', 'r') as f:
            for line in f:
                count += 1
                if count > 3:
                    print(line, count)
                    g.write(line)

        f.close()
    g.close()

    # json = simplejson.dumps(final_dict, ensure_ascii=False)

    # f = open('output.txt','w+')
    # f.write(json)
    # return json


extractor('data.xml')
