import mesop as me
import google.generativeai as genai
import json
import typing_extensions

@me.stateclass
class Article:
    title: str
    outline: str
    response: str

genai.configure(api_key="AIzaSyDdNpdWjzZemXtGPQt3gWTTf5ZHO7U6_0U")
model = genai.GenerativeModel("gemini-1.5-flash-latest")
     
# Response Schema
class Blog(typing_extensions.TypedDict):
    title: str
    content: str

def on_title_input(title: me.InputEvent):
    s = me.state(Article)
    s.title = title.value

def on_outline_input(outline: me.InputEvent):
    s = me.state(Article)
    s.outline = outline.value

def on_click(click: me.ClickEvent):
    s = me.state(Article)
    prompt = f"Write a blog on the following article title and outline: <article_title>{s.title}</article_title><article_outline>{s.outline}</article_outline>. Only return the final blog and title in markdown format."
    # Add environment variable to store the hook URL
    response = model.generate_content(
                prompt,
                generation_config=genai.GenerationConfig(
                    response_mime_type="application/json",
                    response_schema=Blog,
                    temperature=0.8
                ))
    data = json.loads(response.text)['content']
    s.response = data
    print(s.response)

@me.page()
def app():
    with me.box(style=_STYLE_CONTAINER):
        s = me.state(Article)
        with me.box(style=_STYLE_MAIN_COLUMN):
            me.input(label="Title", on_input=on_title_input, type="text", style=_STYLE_INPUT_WIDTH)
            me.input(label="Outline", on_input=on_outline_input, type="text", style=_STYLE_INPUT_WIDTH)
            me.button("Generate Blog", on_click=on_click, style=_STYLE_BUTTON)
    with me.box(style=_STYLE_PREVIEW_CONTAINER):
        if s.response:
            me.markdown(f"{s.response}", style=_STYLE_PREVIEW)
        # me.markdown(blog['content'], style=_STYLE_PREVIEW)

# Styles

_DEFAULT_PADDING = me.Padding.all(15)
_DEFAULT_BORDER = me.Border.all(
    me.BorderSide(color="#e0e0e0", width=1, style="solid")
)

_STYLE_INPUT_WIDTH = me.Style(width="100%")
_STYLE_BUTTON = me.Style(
    background="#1976D2",
    color="#fff",
    padding=me.Padding.symmetric(horizontal=20, vertical=10),
    font_size="16px",
    cursor="pointer",
    margin=me.Margin(bottom=20),
)
_STYLE_PREVIEW_CONTAINER = me.Style(
    margin=me.Margin(top=20),
    height="70vh",
    border=_DEFAULT_BORDER,
    overflow_y="scroll", padding=me.Padding.symmetric(vertical=0, horizontal=20)
)

_STYLE_PREVIEW = me.Style(
    width="100%",
    padding = me.Padding.symmetric(horizontal=40, vertical=10),
)


_STYLE_CONTAINER = me.Style(
    display="grid",
    grid_template_columns="1fr 1fr 1fr",
    grid_column="2/3",
    margin=me.Margin(top=20),
)


_STYLE_MAIN_COLUMN = me.Style(
    grid_column="2/3",
    border=_DEFAULT_BORDER,
    padding=me.Padding.all(15),
    overflow_y="scroll",
)