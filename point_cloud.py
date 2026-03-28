import numpy as np
import plotly.graph_objects as go

class PointCloudBuilder:

    def __init__(self):
        self.points = []

    def add_points(self, pts):

        for p in pts:
            x = p[0]
            y = p[1]
            z = np.random.uniform(1,5)

            self.points.append([x,y,z])

    def show(self):

        if len(self.points) == 0:
            print("No points to display")
            return

        pts = np.array(self.points)

        fig = go.Figure(data=[go.Scatter3d(
            x=pts[:,0],
            y=pts[:,1],
            z=pts[:,2],
            mode='markers',
            marker=dict(
                size=3,
                color=pts[:,2],
                colorscale='Viridis',
                opacity=0.8
            )
        )])

        fig.update_layout(
            title="3D SLAM Point Cloud Map",
            scene=dict(
                xaxis_title='X',
                yaxis_title='Y',
                zaxis_title='Z'
            )
        )

        fig.show()