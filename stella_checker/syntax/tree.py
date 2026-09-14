from antlr4.tree.Tree import TerminalNode


def format_tree(root):
    lines = []
    stack = [(root, "", "")]
    while stack:
        node, prefix, branch = stack.pop()
        if isinstance(node, TerminalNode):
            label = repr(node.getText())
        else:
            name = type(node).__name__.removesuffix("Context")
            label = f"{name} [{node.start.line}:{node.start.column + 1}]"
        lines.append(prefix + branch + label)
        children = [] if isinstance(node, TerminalNode) else list(node.getChildren())
        child_prefix = prefix + ("    " if branch == "└── " else "│   " if branch else "")
        for index in range(len(children) - 1, -1, -1):
            child_branch = "└── " if index == len(children) - 1 else "├── "
            stack.append((children[index], child_prefix, child_branch))
    return "\n".join(lines)
