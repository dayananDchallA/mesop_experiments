import mesop as me

_STYLE_CONTAINER = me.Style(
    display="grid",
    grid_template_columns="1fr 1fr 1fr",
    grid_column="2/3",
    #margin=me.Margin(top=20,left=20,right=20),
    padding=me.Padding(top=20, right=20, bottom=20, left=20),
    background="content-box radial-gradient(crimson, skyblue);",
    height=100,
    #width=30,
)

#_COLOR_BACKGROUND = "#f1f4f8"
_COLOR_BACKGROUND = "GREEN"

_STYLE_APP_CONTAINER = me.Style(
  background=_COLOR_BACKGROUND,
  #padding=me.Padding(left=10, right=10),
  display="grid",
  height="100vh",
  grid_template_columns="repeat(1, 1fr)",
)

_ICON_STYLE = me.Style(
    color="white",
    font_size=20,
    padding=me.Padding(left=10, right=10),
    margin=me.Margin(top=10, bottom=10, left=10),
    background="no-repeat url('./dummy_logo.jpeg');",
    border_radius=10,
    cursor="pointer",
    width=100,
)

def _make_style_chat_ui_container(has_title: bool) -> me.Style:
  """Generates styles for chat UI container depending on if there is a title or not.

  Args:
    has_title: Whether the Chat UI is display a title or not.
  """
  return me.Style(
    display="grid",
    grid_template_columns="repeat(1, 1fr)",
    grid_template_rows="1fr 14fr 1fr" if has_title else "5fr 1fr",
    margin=me.Margin.symmetric(vertical=0, horizontal="auto"),
    width="min(1024px, 100%)",
    height="100vh",
    background="#fff",
    box_shadow=(
      "0 3px 1px -2px #0003, 0 2px 2px #00000024, 0 1px 5px #0000001f"
    ),
    padding=me.Padding(top=20, left=20, right=20),
  )

title = "UI Chat"

_STYLE_TITLE = me.Style(align_self='center')

_STYLE_CHAT_INPUT_BOX = me.Style(
  padding=me.Padding(top=30), display="flex", flex_direction="row"
)
_LABEL_INPUT = "Enter your prompt"
_STYLE_CHAT_INPUT = me.Style(width="100%")
_STYLE_CHAT_BUTTON = me.Style(margin=me.Margin(top=8, left=8))

@me.page()
def app():
    with me.box(style=_STYLE_APP_CONTAINER):
        me.text(title, type="headline-2", style=_STYLE_TITLE)
        with me.box(style=_make_style_chat_ui_container(bool(title))):
            me.text("Hello", type="headline-6", style=me.Style(padding=me.Padding(left=10)))
            with me.box(style=_STYLE_CHAT_INPUT_BOX):
                with me.box(style=me.Style(flex_grow=1)):
                    me.input(
                        label=_LABEL_INPUT,
                        style=_STYLE_CHAT_INPUT,
                    )
                    #me.textarea(label="Basic input")
                    me.box(key="scroll-to", style=me.Style(height=300))
                    me.button(
                        "Send",
                        color="primary",
                        type="flat",
                        disabled=False,
                        style=_STYLE_CHAT_BUTTON,
                        key="send-button",
                        )