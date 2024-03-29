import xml.etree.ElementTree as ET

# import flask
import io
import re
import simplejson


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
            child.text = child.attrib['tid'] + '_' + child.text + '_' + child.attrib['tid']

            final_dict[child.text] = child.attrib
            # print(final_dict)
            # print(child.attrib)
            tree.write('output.xml', encoding="UTF-8", xml_declaration=True)
        elif child.tag == 'EVENT':
            child.attrib.pop('tense')
            child.attrib.pop('aspect')
            child.text = child.attrib['eid'] + '_' + child.text + '_' + child.attrib['eid']
            final_dict[child.text] = child.attrib
            # print(final_dict)
            # print(child.attrib)
            tree.write('output.xml', encoding="UTF-8", xml_declaration=True)

    with open('output.xml', 'r') as f:
        con = f.read()

    m = re.findall(r'<[^<>]*>', con)
    for i in range(len(m)):
        con = con.replace(m[i], '')
    # print(type(con))
    with io.open('strip.txt', 'w', encoding='utf-8') as f:
        f.write(con)
    f.close()
    count = 0
    with io.open('final.txt', 'w', encoding='utf-8') as g:
        with open('strip.txt', 'r') as f:
            for line in f:
                count += 1
                if count > 2:
                    if count is 3:
                        ab = ''.join(line)
                        # print(ab,type(ab))

                        ab = ab.split('|')
                        # print(ab[0])
                        ab = ab[0].split(',')
                        print(ab)
                        ab = ab[1].split('(')
                        g.write(ab[0])
                    # print(line, count)
                    else:
                        g.write(line)

        f.close()
    g.close()

    json = simplejson.dumps(final_dict, ensure_ascii=False)

    f = open('output.txt', 'w+')
    f.write(json)
    return json

extractor('data.xml')
