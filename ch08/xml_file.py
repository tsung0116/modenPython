import xml.etree.ElementTree as et

tree = et.ElementTree(file='menu.xml')
root = tree.getroot()
print(root.tag)

for child in root:
    print('tag:', child.tag, 'attributes:', child.attrib)
    for grandchild in child:
        print('\ttag:', grandchild.tag, 'attributes:', grandchild.attrib, 'text:', grandchild.text)

print(root[0].attrib)
print(root[1][0].text)

print(len(root))
print(len(root[1]))
