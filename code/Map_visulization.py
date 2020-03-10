import plotly.offline as py
import pandas as pd
import plotly.graph_objects as go
import psutil
py.init_notebook_mode(connected=True)
# from plotly.graph_objs import Scatter, Layout,Figure
import matplotlib.pyplot as plt


data_train = pd.read_csv("./data_merged.csv",delimiter=',')

# Latitude and Longitude map
dest_lat = ["42.342907","42.352141","42.350666","42.365008","42.364007", "42.340422","42.355976",
            "42.363428","42.358865","42.351884","42.350282","42.366265"]
dest_lon = ["-71.100292","-71.055135","-71.105410","-71.054222","-71.058433", "-71.089269","-71.0549726",
            "-71.066568","-71.0707475","-71.064262","-71.080968","-71.063098"]

# MapBox Token_access
mapbox_access_token = "pk.eyJ1IjoiamFjaW5kYTk2IiwiYSI6ImNrNnhna" \
                      "HhtaDBpMHIza284cjY2djFtZzIifQ.6JXJfAP7R3Lz7vBZpNhc9w"


#Plot the Boston Map with all the locations
fig = go.Figure(go.Scattermapbox(
        lat=dest_lat,
        lon=dest_lon,
        mode='markers',
        marker=go.scattermapbox.Marker(
            size=9
        ),
        text=["Fenway","South Station","Boston University",
            "North End","Haymarket Square","Northeastern University",
             "Financial District","West End","Beacon Hill",
             "Theatre District","Back Bay","North Station"],
    ))

fig.update_layout(
    autosize=True,
    hovermode='closest',
    mapbox=dict(
        accesstoken=mapbox_access_token,
        bearing=0,
        center=dict(
            lat=42.35,
            lon=-71.07
        ),
        pitch=0,
        zoom=12
    ),
)

fig.show()

#Save the plot
fig.write_image("./chart/boston_map.png")
