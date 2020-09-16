import plotly.graph_objects as go


def correlo(df, to_drop, point_size, palette, title, height, width, fontsize):
    dh = df.drop(columns=to_drop)
    corr = dh.corr()
    x = [[i for _ in range(corr.shape[0])] for i in corr.index]
    x = [j for sub in (x) for j in sub]
    y = [i for i in corr.index] * corr.shape[1]

    size = [point_size * j for sub in (corr.values.tolist()) for j in sub]
    size = [j if j >= 0 else -j for j in size]
    color = [j for sub in (corr.values.tolist()) for j in sub]

    fig = go.Figure(data=go.Scatter(
        y=y,
        x=x,
        mode='markers',
        hovertext=color,
        hoverinfo="text",
        marker=dict(size=size,
                    color=color,
                    colorbar=dict(title="Correlation"),
                    colorscale=palette, cmid=0)))
    fig.update_layout(height=height, width=width, font=dict(size=fontsize), title=title)
    fig.update_xaxes(
        showgrid=True,
        ticks="outside",
        tickson="boundaries",
        ticklen=0)
    fig.update_yaxes(
        showgrid=True,
        ticks="outside",
        tickson="boundaries",
        ticklen=0)
    return fig
