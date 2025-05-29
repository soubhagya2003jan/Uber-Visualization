from dash import Dash, html,dcc,callback,Input,Output
import pandas as pd 
import plotly.express as px

#Reading The Data
df = pd.read_csv('Nyc_Taxi_Trip//train.csv')

#Reading Total Rides
Total_Rides = len(df)
Unique_Rides = df['id'].nunique()

#Creating Daily Ride Count
#Transforming The DateTime Into Pandas Datetime for convenience
df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'])
df['dropoff_datetime'] = pd.to_datetime(df['dropoff_datetime'])

Daily_Rides = df.groupby(df['pickup_datetime'].dt.date).size().reset_index(name='ride_count')

#Trip Duration In Minutes
df['trip_duration_mins'] = (df['dropoff_datetime'] - df['pickup_datetime']).dt.total_seconds() / 60

#Average Trip Duration
Average_Duration = round(df['trip_duration_mins'].mean(),2)


#Creating a Line Chart Using Plotly
Line_Fig = px.line(Daily_Rides, x='pickup_datetime', y='ride_count',
                   labels={'pickup_datetime':'Date', 'ride_count': 'Number of Rides'},
                   template="simple_white")
Line_Fig.update_traces(line=dict(color='black'))
Line_Fig.update_layout(
    yaxis=dict(showgrid=True)
)

#Initializing The Dash Constructor
app = Dash(__name__)

app.layout = html.Div([
    # 🟦 Top Hero Bar
    # The Tittle Of The Hero Bar + Total Rides & Unique Rides
    html.Div([
    # Group Uber title + Metrics
        html.Div([
            html.Div("Uber", className="hero-title"),
            html.Div([
                html.Div([
                    html.Small("Total Rides", className="metric-label"),
                    html.Div(f"{Total_Rides:,}", className="metric-value")
                ]),
                html.Div([
                    html.Small("Unique Riders", className="metric-label"),
                    html.Div(f"{Unique_Rides:,}", className="metric-value")
                ])
            ], className="hero-metrics")
        ], className="hero-left"),

        html.Div([
            html.A("Home", href="#"),
            html.A("Github", href="https://github.com/soubhagya2003jan", target="_blank"),
            html.A("LinkedIn", href="https://www.linkedin.com/in/soubhagyaswain/", target="_blank")
        ], className="hero-right")
    ], className="hero-bar"),

    # 🟥 Main content with left + right
    html.Div([
        #Left Panel
        html.Div([
    html.Iframe(
        src="https://kepler.gl/demo/map?mapUrl=https://dl.dropboxusercontent.com/scl/fi/0dx02q252o6e0f98nwz50/keplergl_v9p55wm.json?rlkey=3e324l3b0v0f2ao7pwok4pp76&dl=0",
        className="kepler-map"
    )
], className="left-panel"),

    html.Div([
        html.Div("Uber Ride Trends", className="right-title"),
        dcc.Graph(figure=Line_Fig, className="ride-graph"),

        html.Div("Average Trip Prediction", className="right-section-title"),

        html.Div([
            html.Small("Trip Time", className="trip-metric"),
            html.Div(f"{Average_Duration} Mins", className="trip-value")
        ], className="prediction-box")

    ], className="right-panel")
        ], className="main-content")
])

if __name__ == "__main__":
    app.run(debug=False)
