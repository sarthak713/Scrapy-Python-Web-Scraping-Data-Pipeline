### What is XPath ?

- XML Path Language
- Used for extracting values from XML documents
- Can be applied to HTML documents also, since HTML uses similar syntax to XML
- It returns html nodes

### How Xpath works ?

- To reach a specific node, follow path from parent node/nodes to required node
1. /html/body/ul/li/span[@class='title']/text()
    - Extract text from span tags with title class
    - But starting from root element is inefficient, Use // instead
2. //span/text()
    - Jump to span directly
3. //ul//span/text()
    - go to ul, skip children nodes in between & go to span 
4. //@id
    - select all nodes with id attribute regardless of value 
5. //li[2]
    - select 2nd li node
6. //li[last()]
    - select last li node
7. //li[position()<2]
    - get first one
8. //li[position()<3]
    - get first 2
9. //li[last()-1]
    - get second last
10. //*[@class='title']/text()
    - get text of all nodes with class title, regardless of tag type
11. //span[@class='title'] | //div[@class='title']
    - get all span & div with class title using '|'

---