class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}
        
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        props_string = ""
        if self.props == None:
            props_string = "None"
        else:
            for key, value in self.props.items():
                props_string = props_string + f" {key}=\"{value}\""
        return props_string

    def __repr__(self):
        return f"HTMLNode( tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value):
        super().__init__(tag, value)

    def to_html(self):
        if self.value == "":
            raise ValueError("Leaf node must have a non-empty value.")
        if self.tag == "":
            return str(self.value)
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children):
        super().__init__(tag, None, children)

    def to_html(self):
        if self.tag == "":
            raise ValueError("Parent node must have a non-empty tag.")
        if self.children is None or len(self.children) == 0:
            raise ValueError("Parent node must have non-empty children.")
        
        output = ""
        output += f"<{self.tag}>"
        for child in self.children:
            output += child.to_html()
        output += f"</{self.tag}{self.props_to_html()}>"
        return output

