#Testing The Map
from dash import Dash,html

app = Dash()

app.layout = html.Div([

    html.h1(children="Kepler Map"),
    html.Iframe(src="https://kepler.gl/demo/map?mapUrl=https://dl.dropboxusercontent.com/scl/fi/0dx02q252o6e0f98nwz50/keplergl_v9p55wm.json?rlkey=3e324l3b0v0f2ao7pwok4pp76&dl=0")

])