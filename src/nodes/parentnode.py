from nodes.htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(
            self,
            tag: str,
            children: list[HTMLNode],
            props: dict[str, str] | None = None
    ):
        super().__init__(tag, None, children, props)

    def to_html(self) -> str:
        if self.tag is None:
            raise ValueError("invalid HTML: no tag")
        
        if len(self.children) == 0:
            raise ValueError("invalid HTML: no children")

        if self.props:
            result = f"<{self.tag} {self.props_to_html()}>"
        else:
            result = f"<{self.tag}>"

        for child in self.children:
            result += child.to_html()
        result += f"</{self.tag}>"
        return result
    
    def __repr__(self):
        return f"ParentNode({self.tag!r}, {self.children!r}, {self.props!r})"