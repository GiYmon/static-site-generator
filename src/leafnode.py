from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(
            self, 
            tag: str | None, 
            value: str, 
            props: dict[str, str] = None
    ):
        super().__init__(tag, value, None, props)

    def to_html(self) -> str:
        if self.value is None:
            raise ValueError("LeafNode must have a value")
        
        if self.tag is None:
            return self.value
        
        props_html = self.props_to_html()
        if props_html:
            return f"<{self.tag} {props_html}>{self.value}</{self.tag}>"
        return f"<{self.tag}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag!r}, {self.value!r}, {self.props!r})"