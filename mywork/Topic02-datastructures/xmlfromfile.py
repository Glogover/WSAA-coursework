from xml.dom.minidom import parse

filename = "employees.xml"

# read file in two ways
doc = parse(filename)
# or 
# with open(filename) as fp:
#     doc = parse(fp)

employeeNodeList = doc.getElementsByTagName("Employee")
print(len(employeeNodeList))
for employeeNode in employeeNodeList:
    # print("->")
    firstNameNode = employeeNode.getElementsByTagName("FirstName").item(0)
    firstName = firstNameNode.firstChild.nodeValue.strip()
    print(firstName)
    