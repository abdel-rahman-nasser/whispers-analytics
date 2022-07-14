from turtle import width
import pandas
import plotly.graph_objects as go
from plotly.offline import plot
import country_converter as coco
import plotly.express as px

class Data_Visualize:
#############################################################################
    #Function for Plotting a Bar chart using plotly
    # def plot_bar_chart_go1(self,df1,srch):
    #     graphs = []
    #     colors=["gold","purple","red","green","blue","yellow"]
    #     for i in range(len(df1.columns)):
    #         graphs.append(go.Bar(x=df1[str(srch).split()].index,y=list(df1[str(srch).split()[i]]),
    #         name=str(str(srch).split()[i].upper()),marker=dict(color = colors[i],)))
    #     #Important Note: If there are more than one keyword, 
    #     # the dataframe will return Percentage of searches
    #     # df: represents "comaparison between different trends" 
    #     # "getting most countries that search for the trends 
    #     #  and check which one have more precentage"
    #     y_axis_label='No. of searches'
    #     if len(str(srch).split())>1:
    #         y_axis_label='Percentage'
    #     layout = {
    #     'xaxis_title': 'Countries',
    #     'yaxis_title':y_axis_label ,
    #     'height': 320,
    #     'width': 660,
    #     'plot_bgcolor': 'rgba(14,23,38,255)',
    #     'paper_bgcolor':'rgba(14,23,38,255)',
    #     'font':{'size':14, 'color':'gold','family':'Courier New (monospace)'}
    #     }

    #     bar = plot({'data': graphs, 'layout': layout}, output_type='div')
    #     return bar
###########################################################################
    def plot_time_series_go(self,tm_df,srch):
        graphs = []
        for i in range(len(tm_df.columns)):
            graphs.append(go.Scatter(x=tm_df.index
                                    ,y=tm_df[str(srch).split()[i]], mode='lines'
                                    ,name=str(srch).split()[i].upper()))

            layout = {
            'height': 320,
            'width': 660,
            'plot_bgcolor': 'rgba(14,23,38,255)',
            'paper_bgcolor':'rgba(14,23,38,255)',
            'font':{'size':14, 'color':'gold','family':'Courier New (monospace)'},
            'xaxis':{'showgrid': False},
            'yaxis':{'showgrid': False}
            }

        tm_sr= plot({'data': graphs, 'layout': layout}, output_type='div')
        return tm_sr
########################################################################
    #Plotting a choropleth map for comparing between trends 
    #In addition, its a very helpful to know 
    # the spread of the trends around the world

    def plot_choropleth_go(self,df1,srch):
        if len(df1.columns)>1:
            df = df1.copy()
            #Mapping for getting geocodes of the countries
            df = df.assign(geoCode=lambda x: (coco.convert(x.index)))

            #Getting the Highest Value
            df['HValue'] = df[str(srch).split()].max(axis = 1)

            #Getting the labels of the trends with the highest values in each country
            df['HLabel'] = df[str(srch).split()].idxmax(axis = 1)
            df = df[df.HValue != 0]

            cdm = dict(zip(str(srch).split(),["#5c1ac3", "#e2a03f", "#e7515a", "#1abc9c", "#e0e6ed"]))
            fig = px.choropleth(
                df,
                locations='geoCode',
                color='HLabel',
                hover_name=df.index,
                projection="mercator",range_color=[0, 6500],
                featureidkey="properties.district",
                color_discrete_map=cdm
            )
            fig.update_layout(
                title_text="",
                legend_title_text='',
                paper_bgcolor="#0e1726",
                plot_bgcolor="#0e1726",
                geo=dict(
                    showframe=False,
                    showcoastlines=False,
                    projection_type='orthographic',
                    bgcolor= 'rgba(14,23,38,255)',
                )
            )
            
            choro=fig.to_html(full_html=False)
            return choro

        #If there is one label only
        else:
            df = df1.copy()
            df = df.assign(geoCode=lambda x: (coco.convert(x.index)))

            fig = go.Figure(data=go.Choropleth(
                locations = df['geoCode'],
                z = df[str(srch)],
                text = df.index,
                colorscale = 'Plasma',
                autocolorscale=False,
                reversescale=False,
                marker_line_color='darkgray',
                marker_line_width=0.5,
                colorbar_title = 'Search volume',
            ), layout = go.Layout(geo=dict(bgcolor= 'rgba(14,23,38,255)'),
                                  font = {"size": 9, "color":"White"},
                                  titlefont = {"size": 15, "color":"White"},
                                  margin={"r":0,"t":40,"l":0,"b":0},
                                  paper_bgcolor='rgba(14,23,38,255)',
                                  plot_bgcolor='rgba(14,23,38,255)',
                                  ))

            fig.update_layout(
                title_text=f' ',
                geo=dict(
                    showframe=False,
                    showcoastlines=False,
                    projection_type="orthographic",
                    bgcolor= 'rgba(14,23,38,255)',
                    
                ),
            )
            choro=fig.to_html(full_html=False)
            return choro

    def plot_bar_chart_go(self,df1,srch):
        colors=["gold","purple","red","green","blue","yellow"]
        fig = go.Figure()
        for i in range(len(df1.columns)):
            fig.add_trace(
                go.Bar(x=df1[str(srch).split()].index,
                             y=df1[str(srch).split()[i]],
                             name=str(str(srch).split()[i].upper()),
                             marker=dict(color = colors[i],)))
        fig.update_layout(
            barmode='group',
            xaxis_tickangle=-45,
            height=320,
            width= 660,
            plot_bgcolor= "#0e1726",
            paper_bgcolor="#0e1726",
            font={'size':14, 'color':'gold','family':'Courier New (monospace)'},
            xaxis={'showgrid': False},
            yaxis={'showgrid': False},

        )
        fig=fig.to_html(full_html=False)
        return fig
