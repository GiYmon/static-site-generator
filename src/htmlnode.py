


class HTMLNode:
    def __init__(
            self, 
            tag: str = None, 
            value: str = None, 
            children: list["HTMLNode"] = None, 
            props: dict[str, str] = None
        ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self) -> str:
        raise NotImplementedError("Subclasses must implement this method")
    
    def props_to_html(self) -> str:
        if not self.props:
            return ""
        return " ".join(f'{key}="{value}"' for key, value in self.props.items())
    
    def __repr__(self) -> str:
        return f"HTMLNode({self.tag!r}, {self.value!r}, {self.children!r}, {self.props!r})"