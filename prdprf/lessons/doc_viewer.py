import reflex as rx
from typing import List

class DocViewer(rx.Component):
    library = "react-doc-viewer"
    tag = "DocViewer"

    documents: rx.Var[List[str]]

