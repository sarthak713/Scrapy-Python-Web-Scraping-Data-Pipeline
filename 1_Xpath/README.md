### What is XPath ?

- XML Path Language
- Used for extracting values from XML documents
- Can be applied to HTML documents also, since HTML uses similar syntax to XML
- It returns html nodes
- Practice XPath queries with HTML/XML documents: http://xpather.com/ 

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

### Axes

- Used to define relations between nodes in a document to make more powerful queries

1. //span[@class='author']/ancestor::ul
    - Select ul ancestor of span with class author
    - Selects all ul ancestors
2. //span[@class='author']/ancestor::ul[1]
    - Select the first ul ancestor of span with class author 
3. //span/parent::li
    - Select parent of span which is li
4. //li[@class='book']/child::span[@class='price']
    - Select span with class price which is child of li with class book
5. //ul/descendant::span[@class='price']
    - Select all descendant of ul which are span with price class
    - Similar to //ul//::span[@class='price']
6. //li[@class='book']/following::span
    - Select all spans inside li leaving the first li node, and other spans also
7. //div[@class='header']/following-sibling::span
    - Select span siblings of div with class header
8. //span[@class='price']/preceding::span
    - Selects all spans before span with price class, not necessarily having the same parent
9. //span[@class='price']/preceding-sibling::span
    - Selects spans before price span but limit to same parent

---