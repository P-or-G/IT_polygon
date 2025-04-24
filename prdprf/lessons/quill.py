import reflex as rx
from typing import List, Dict


class ReactQuillLib(rx.components.component.NoSSRComponent):
    library = "react-quill-new"
    lib_dependencies: List[str] = [ "lodash", "quill" ]


class ReactQuill(ReactQuillLib):
    tag = "ReactQuill"

    theme: rx.Var[str] = "snow"
    default_value: rx.Var[str]
    value: rx.Var[str]
    placeholder: rx.Var[str]
    modules: rx.Var[Dict
        [str,

         Dict[str, int | bool | str]
         | List[List[str | Dict[str, List[int | bool | str]]]]
         | bool
        ]
    ] # оно работает.
    on_change: rx.EventHandler[lambda val: [val]]

    is_default = True # я не знаю что оно делать но это НЕ УБИРАТЬ И НЕ МЕНЯТЬ

    def add_imports(self):
        return {
            "": ["react-quill-new/dist/quill.snow.css"],
        }

    def add_custom_code(self) -> str:
        return """
        """


Quill = ReactQuill.create

QuillDeps = [
        # KaTeX
        rx.script(
            src="https://cdn.jsdelivr.net/npm/katex@0.16.21/dist/katex.js"
        ),
        rx.el.Link(
            href="https://cdn.jsdelivr.net/npm/katex@0.16.21/dist/katex.css",
            rel="stylesheet",
            crossorigin="anonymous",
        ),
        rx.script(
            src="https://cdn.jsdelivr.net/npm/katex@0.16.21/dist/contrib/auto-render.js"
        ),

        rx.el.Link(
            href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/atom-one-dark.min.css",
            rel="stylesheet",
        ),
        rx.script(
            src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"
        ),
]