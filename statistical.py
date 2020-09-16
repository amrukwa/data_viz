# import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def basic_violins(df, plot_col, val, title, info, height=500, width=985, to_sort=True,
                  palette=px.colors.qualitative.Plotly):
    regions = df[plot_col].unique()
    j = 0
    for_sort = []
    data = []
    q = []
    fig = go.Figure()
    for region in regions:
        x = df[plot_col][(df[plot_col] == region)]
        y = df[val][(df[plot_col] == region)]
        quantity = x.shape[0]
        if quantity > 2:
            for_sort.append(y.median())
            data.append(go.Violin(x=x,
                                  text=df[info][(df[plot_col] == region)],
                                  y=y,
                                  name=region,
                                  marker=dict(color=palette[j]),
                                  box_visible=True,
                                  meanline_visible=True
                                  ))
        q.append(region + ":<br>" + str(quantity))
        j += 1
    if not to_sort:
        for trace in range(len(data)):
            fig.add_trace(data[trace])
    else:
        for trace in range(len(data)):
            indices = np.argsort(for_sort)
            fig.add_trace(data[indices[trace]])
    fig.update_xaxes(ticktext=q, tickvals=regions, title=plot_col)
    fig.update_yaxes(title=val)
    fig.update_layout(height=height, width=width, title_text=title)
    return fig


def basic_boxes(df, plot_col, val, title, info, height=500, width=985, to_sort=True,
                palette=px.colors.qualitative.Plotly):
    regions = df[plot_col].unique()
    j = 0
    for_sort = []
    data = []
    q = []
    fig = go.Figure()
    for region in regions:
        x = df[plot_col][(df[plot_col] == region)]
        y = df[val][(df[plot_col] == region)]
        quantity = x.shape[0]
        if quantity > 2:
            for_sort.append(y.median())
            data.append(go.Box(x=x,
                               text=df[info][(df[plot_col] == region)],
                               y=y,
                               name=region,
                               marker=dict(color=palette[j])
                               ))
        j += 1
        q.append(region + ":<br>" + str(quantity))
    if not to_sort:
        for trace in range(len(data)):
            fig.add_trace(data[trace])
    else:
        for trace in range(len(data)):
            indices = np.argsort(for_sort)
            fig.add_trace(data[indices[trace]])
    fig.update_xaxes(ticktext=q, tickvals=regions, title=plot_col)
    fig.update_yaxes(title=val)
    fig.update_layout(height=height, width=width, title_text=title)
    return fig


def subboxes(df, plot_cat, plot_col, val, title, height, width, info, to_sort=True, v_spacing=0.1,
             palette=px.colors.qualitative.Plotly, fontsize=11, tickangle=0):
    regions = df[plot_col].unique()
    to_represent = {}
    for region in regions:
        to_represent[region] = True
    fig = make_subplots(rows=len(df[plot_cat].unique()), cols=1, shared_xaxes=False,
                        shared_yaxes=True, vertical_spacing=v_spacing, subplot_titles=(df[plot_cat].unique()))
    j = 0
    for i in df[plot_cat].unique():
        j += 1
        q = []
        k = 0
        for_sort = []
        data = []
        for region in regions:
            x = df[plot_col][(df[plot_col] == region) & (df[plot_cat] == i)]
            quantity = x.shape[0]
            if quantity > 2:
                y = df[val][(df[plot_col] == region) & (df[plot_cat] == i)]
                for_sort.append(y.median())
                data.append(go.Box(x=x,
                                   y=y,
                                   text=df[info][(df[plot_col] == region) & (df[plot_cat] == i)],
                                   name=region,
                                   legendgroup='group' + region,
                                   showlegend=to_represent[region],
                                   marker=dict(color=palette[k])
                                   ))
                to_represent[region] = False
            q.append(region + ":<br>" + str(quantity))
            k += 1
            # sort the data by median
        indices = np.argsort(for_sort)
        if not to_sort:
            for trace in range(len(data)):
                fig.append_trace(data[trace], row=j, col=1)
        else:
            for trace in range(len(data)):
                fig.append_trace(data[indices[trace]], row=j, col=1)
        fig.update_xaxes(
            tickangle=tickangle, tickfont=dict(size=fontsize),
            title=plot_col,
            ticktext=q, tickvals=regions,
            row=j, col=1)
        fig.update_yaxes(title=val, row=j, col=1)
    fig.update_layout(height=height, width=width, title_text=title)
    return fig


def subviolins(df, plot_cat, plot_col, val, title, height, width, info, to_sort=True, v_spacing=0.1,
               palette=px.colors.qualitative.Plotly, fontsize=11, tickangle=0):
    regions = df[plot_col].unique()
    to_represent = {}
    for region in regions:
        to_represent[region] = True
    fig = make_subplots(rows=len(df[plot_cat].unique()), cols=1, shared_xaxes=False,
                        shared_yaxes=True, vertical_spacing=v_spacing, subplot_titles=(df[plot_cat].unique()))
    j = 0
    for i in df[plot_cat].unique():
        j += 1
        q = []
        k = 0
        for_sort = []
        data = []
        for region in regions:
            x = df[plot_col][(df[plot_col] == region) & (df[plot_cat] == i)]
            quantity = x.shape[0]
            if quantity > 2:
                y = df[val][(df[plot_col] == region) & (df[plot_cat] == i)]
                for_sort.append(y.median())
                data.append(go.Violin(x=x,
                                      y=y,
                                      text=df[info][(df[plot_col] == region) & (df[plot_cat] == i)],
                                      name=region,
                                      legendgroup='group' + region,
                                      showlegend=to_represent[region],
                                      marker=dict(color=palette[k]),
                                      box_visible=True,
                                      meanline_visible=True
                                      ))
                to_represent[region] = False
            q.append(region + ":<br>" + str(quantity))
            k += 1
            # sort the data by median
        indices = np.argsort(for_sort)
        if not to_sort:
            for trace in range(len(data)):
                fig.append_trace(data[trace], row=j, col=1)
        else:
            for trace in range(len(data)):
                fig.append_trace(data[indices[trace]], row=j, col=1)
        fig.update_xaxes(
            tickangle=tickangle, tickfont=dict(size=fontsize),
            title=plot_col,
            ticktext=q, tickvals=regions,
            row=j, col=1)
        fig.update_yaxes(title=val, row=j, col=1)
    fig.update_layout(height=height, width=width, title_text=title)
    return fig
