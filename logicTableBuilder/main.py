class LogicTable:
    # the base logic table object of the logic table builder
    # this object will hold the fundamental data regarding the table
    # you'd like to generate.
    # overall goal is to build a nice library to build
    # logic tables and output everything to a spreadsheet or pdf
    # formatted with latex.
    def __init__(self, value):
        # defines rows on instantiation
        self.row_total = 2**value

    def get_row_total(self):
        return self.row_total

    def test_rows(self):
        for x in range(self.row_total):
            format(x, 'b')








