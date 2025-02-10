import reflex as rx

from typing import List, Dict, TypeAlias, Union, Any

JSON: TypeAlias = Dict[str, Any]


class Nothing(rx.components.component.NoSSRComponent):
    library = "react-quill-new"
    lib_dependencies: List[str] = [ "lodash", "quill" ]
    tag = "Quill"
    is_default = False

    def add_imports(self):
        return {"react-quill-new": [rx.ImportVar(tag="Quill")]}


class ReactQuillLib(rx.components.component.NoSSRComponent):
    library = "react-quill-new"
    lib_dependencies: List[str] = [ "lodash", "quill" ]

class ReactQuill(ReactQuillLib):
    tag = "ReactQuill"

    theme: rx.Var[str] = "snow"
    default_value: rx.Var[str]
    value: rx.Var[str]
    placeholder: rx.Var[str]
    modules: rx.Var[JSON]
    on_change: rx.EventHandler[lambda val: [val]]

    is_default = True

    def _get_imports(self):
        d = super().add_imports()
        # d["react-quill-new"] = [rx.ImportVar(tag="Quill", is_default=False)]

        d[""] = [
            'react-quill-new/dist/quill.snow.css'
        ]

        d["@botom/quill-resize-module"] = [rx.ImportVar(tag="ResizeModule", is_default=True)]
        # d["quill-resize-module"] = [rx.ImportVar(tag="QuillResize", is_default=True)]
        # d["quill-html-edit-button"] = rx.ImportVar(tag="htmlEditButton", is_default=True)
        d["next/dynamic"] = [rx.ImportVar(tag="dynamic", is_default=True)]

        # print(d)

        return d

    def _get_custom_code(self):
        return """
// const reflex_init = async () => {
//     if (typeof window !== 'undefined') {
//         const { Quill } = await import('react-quill-new');
//         const htmlEditButton = await import('quill-html-edit-button');
// 
//         Quill.register({ 'modules/htmlEditButton': htmlEditButton });
//     };
// };
// 
// reflex_init();

// ReactQuill.register({ 'modules/htmlEditButton': htmlEditButton });
// ReactQuill.register('modules/resize', QuillResize);
"""

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

