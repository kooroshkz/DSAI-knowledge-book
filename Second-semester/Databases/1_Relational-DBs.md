# Relational model

## Relation (Table):
| ID      | Field 1 | Field 2 | ... |
|---------|---------|---------|-----|
| Record1 | Record1 | ...     | ... |
| Record2 | ...     | ...     | ... |

# Hierarchical models

Type of data model where data is organized in a binary tree structure.
Like XML (eXtensible Markup Language):

```xml
<bookstore> <!--Root element-->
  <book> <!-- Item and Child of Bookstore-->
    <title>Harry Potter and the Sorcerer's Stone</title> <!-- nested elements-->
    <author>J.K. Rowling</author> <!-- nested elements-->
    <year>1997</year> <!-- nested elements-->
    <price>10.99</price> <!-- nested elements-->
  </book>
  <book>
    <title>The Great Gatsby</title>
    <author>F. Scott Fitzgerald</author>
    <year>1925</year>
    <price>12.99</price>
  </book>
</bookstore>

---

# Entity-Relationship (ER) model


- Entities: real-world objects or concepts such as employee
- Attributes: properties or characteristics of entities, such as "Name", "Age", or "Salary"
- Relationships: associations or interactions between entities
<img src="https://www.simplilearn.com/ice9/free_resources_article_thumb/ERDiagramsInDBMS_1.png" width="300">
