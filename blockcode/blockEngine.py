class Block:
    def __init__(self):
        self.inner_blocks = []
        self.heap = {}

    def name(self):
        print self.name

    def add_block(self, block):
        self.inner_blocks.append(block)

    def add_variable_expression(self, variable):
        variable.add_to_heap(self)

    def execute(self):
        for inner_block in self.inner_blocks:
            inner_block.execute()


class IfBlock(Block):
    def __init__(self, comparison_character, compared_value1, compared_value2, else_block):
        Block.__init__(self)
        self.comparison_character = comparison_character
        self.compared_value1 = compared_value1
        self.compared_value2 = compared_value2
        self.else_block = else_block

    def execute(self):
        if self.comparison_character is '>':
            if self.compared_value1 > self.compared_value2:
                Block.execute(self)
            else:
                if self.else_block:
                    self.else_block.execute()


class PrintBlock(Block):
    def __init__(self, print_value):
        self.print_value = print_value

    def execute(self):
        print self.print_value


class ElseBlock(Block):
    pass


class VariableExpression:
    def __init__(self, variable_name, variable_value):
        self.variable_name = variable_name
        self.variable_value = variable_value

    def add_to_heap(self, block):
        block.heap[self.variable_name] = self.variable_value


elseBlock = ElseBlock()
elseBlock.add_block(PrintBlock("else value"))

ifBlock2 = IfBlock('>', 12, 12, elseBlock)
ifBlock2.add_block(PrintBlock('print value 2'))
ifBlock2.add_variable_expression(VariableExpression('me', 2))

ifBlock = IfBlock('>', 12, 10, None)
ifBlock.add_block(PrintBlock('print value'))
ifBlock.add_block(ifBlock2)
ifBlock.execute()
