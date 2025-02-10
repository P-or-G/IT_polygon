import reflex as rx

class QuillLib(rx.Component):
    library = "react-quilljs"

    def _get_custom_code(self) -> str:
        return """import 'quill/dist/quill.snow.css';
               """

class UseQuill(QuillLib):
    tag = "useQuill"


uq = UseQuill.create # create should accept args

quillRef = uq()
rx.link("kaslkda", quillRef)

def index():
    return rx.vstack(
        rx.heading("Google OAuth"),
        rx.link("Protected Page", href="/protected"),
    )


app = rx.App()
app.add_page(index)
