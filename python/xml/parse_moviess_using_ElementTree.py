import xml.etree.ElementTree as et

tree = et.parse('country_data.xml')
root = tree.getroot()
#root = et.fromstring(
print('root-tag:', root.tag, ',root-attrib:', root.attrib, ',root-text:', root.text)

def print_fields(child):
    print('%s tag:' % child.tag, ',attrib:', child.attrib, ',text:', child.text)


#for child in root:
#    print_fields(child)
#    for sub in child:
#        if sub.find('moive'):
#            print_fields(sub)


ishtarNode = root.find('country')
print(ishtarNode)
if ishtarNode.attrib['name'] == 'Liechtenstein':
    print_fields(ishtarNode)
    root.remove(ishtarNode)

tree.write('country_data_reduced.xml')
