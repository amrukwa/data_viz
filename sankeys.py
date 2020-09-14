import numpy as np
import colours as c
import plotly.graph_objects as go


def extract_labels_basic(df):
    label = np.array([])
    for col in df.columns.values:
        if col == df.iloc[:, -1].name:
            break
        label = np.append(label, df[col].unique())
    return np.unique(label.tolist())


def extract_sources_basic(df, label):
    l = df.iloc[:, 0].tolist()
    source = [np.where(i == label)[0][0] for i in l]
    return source


def extract_targets_basic(df, label):
    l = df.iloc[:, 1].tolist()
    target = [np.where(i == label)[0][0] for i in l]
    return target


def choose_col(palette, val):
    if val < len(palette):
        color = palette[val]
    else:
        color = palette[len(palette) - val]
    return color


def provide_basic_sankey(df, palette, normalized=False):
    color = c.opacity_conv(palette, 0.2)
    label = extract_labels_basic(df)
    source = extract_sources_basic(df, label)
    target = extract_targets_basic(df, label)
    if normalized:
        fig = go.Figure(data=[go.Sankey(
            valueformat=".2f",
            valuesuffix="%",
            node=dict(
                pad=15,
                thickness=20,
                line=dict(color="black", width=0.5),
                label=label,
                color=palette),
            link=dict(
                source=source,
                target=target,
                value=df.iloc[:, -1].tolist(),
                color=[choose_col(color, i) for i in source]
            ))])
    else:
        fig = go.Figure(data=[go.Sankey(
            node=dict(
                pad=15,
                thickness=20,
                line=dict(color="black", width=0.5),
                label=label,
                color=palette),
            link=dict(
                source=source,
                target=target,
                value=df.iloc[:, -1].tolist(),
                color=[choose_col(color, i) for i in source]
            ))])
    return fig
