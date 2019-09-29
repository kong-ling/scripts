#coding=utf-8
import  xml.dom.minidom

#¿?¿?xml¿?¿?
dom = xml.dom.minidom.parse('sample.xml')

#¿?¿?¿?¿?¿?¿?¿?¿?
root = dom.documentElement
print(root.nodeName)
print(root.nodeValue)
print(root.nodeType)
print(root.ELEMENT_NODE)
