pyTable
=======

A python symbols table made for a syntactic analyzer.

USE:

- Download both .py files (Table.py and SymTable.py).
- Import class SymTable defined inside SymTable.py
- you only need to create one instance of SymTable. It provides the following methods to create, manage, print to a file and destroy symbols tables:
  - newTable(): creates a new symbol table and returns its id.
  - destroyTable(id): deletes id table.
  - existTable(id): returns wether id table exist or not.
  - add(id, lex): Adds the lexem lex to id table. Returns the id of the lexem if everything is OK or false if lex already exist on that table
  - addType(id, lex, type): Adds the "type" to the lexem whose id is "lex" in the table whose id is "id"

Software distributed under a Creative Commons Attribution-ShareAlike 3.0 Unported license. This allows you to adapt, copy, distribute and transmit the work while crediting the author of the original work and sharing under the same or similar license.
Full legal text of this license can be found on http://creativecommons.org/licenses/by-sa/3.0/legalcode
