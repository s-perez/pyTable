"""
Software distributed under a Creative Commons Attribution-ShareAlike 3.0 Unported license. This allows you to adapt, copy, distribute and transmit the work while crediting the author of the original work and sharing under the same or similar license.
Full legal text of this license can be found on http://creativecommons.org/licenses/by-sa/3.0/legalcode
"""

class Table():

    def __init__(self, id):
        self.lexems = {}
        self.exists = True
        self.id = id

    def delete(self):
        """This function marks this table as deleted"""

        self.exists = False
        return True

    def exist(self):
        """Checks if this table is deleted or not"""

        return self.exists

    def add(self, lex):
        """Adds lex to this table.
        Returns the position of the lex if everything went OK. Otherwise, it returns False"""

        if not lex in self.lexems:
            self.lexems[lex] = ''
            return self.getPos(lex)
        else:
            return self.getPos(lex)

    def setType(self, lex, type):
        """Sets the type of lex.
        Returns True if everything went OK. Otherwise, returns False"""

        if lex in self.lexems:
            self.lexems[lex] = type
            return True
        else:
            return False

    def getType(self, lex):
        "Returns the type of lex"

        return self.lexems[lex]

    def contains(self, lex):
        "Checks if lex is in the table or not"

        return self.lexems.has_key[lex]

    def write(self, path):
        "Writes the contents of this table to the file pointed to by path"

        if self.exist():
            f = open(path, 'a')
            f.write('--------------------| Tabla' + str(self.id) + ' |--------------------\n')
            f.write('----------------------------------------------------\n')
            for e in self.lexems.keys():
                f.write('\t' + str(e))
                if self.lexems[e] != '':
                    f.write(' (' + self.lexems[e] + ')')
                f.write('\n')
            f.write('\n\n\n')
            f.close()
            return True
        else:
            return False

    def getPos(self, lex):
        "returns the ID of lex or False if lex is not in this table"

        i = 0
        for e in self.lexems.keys():
            if e == lex:
                break
            else:
                i = i + 1
        return False if i == len(self.lexems) else i
