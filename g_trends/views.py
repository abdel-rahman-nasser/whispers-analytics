import datetime
from unittest.util import sorted_list_difference
from django.shortcuts import render,redirect
from django.http import JsonResponse
from g_trends.models import Data_Save
import pandas as pd
from g_trends.classes.data_visualization import Data_Visualize as dv
from g_trends.classes.get_trends import Trends_Collection as gt
import operator

def get_g_trends(request):
    if request.user.is_authenticated:
        return render(request, "scrape_trends/trends_page.html")
    else:
        return redirect("welcome")

def g_trends_search(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            if 'kw' in request.GET:
                srch = request.GET.get("kw")
                try:
                    trends_list = []
                    time_s = []
                    rltd_dict = []
                    # Query to get the stored data about the entered keyword from the database, if exists
                    for p in Data_Save.objects.raw("select * from g_trends_data_Save where trend=%s", [str(srch)]):
                        trends_list.append(p.df)
                        time_s.append(p.time_df)
                        rltd_dict.append(p.rltd_dict)

                    # Checking if the keyword was cached and stored in the database or not
                    # If Not, scrape for the new data using the new keyword, then store it in the model "caching"
                    if not trends_list:
                        print("Empty")
                        t = gt()
                    # Scraping for trends "OverTime-ByRegion-RelatedDictionaries"
                        tm_df, df1, r_dict = t.trends_scraping(
                            kw=str(srch).split())

                    # Sorting desacendingly to get the most popular Regions
                    #  that search for entered Keyword
                        df1 = df1.sort_values(by=str(srch).split(), ascending=[
                                                False for x in range(len(df1.columns))])
                        df1_model = Data_Save(
                            trend=str(srch), df=df1, time_df=tm_df, rltd_dict=r_dict)
                        df1_model.save()

                    # If it exists, just return the dataframe from the database
                    else:
                        df1 = trends_list[0]
                        tm_df = time_s[0]
                        r_dict=rltd_dict[0]
                        #print(tm_df.index)
                        #print(df1)

                    queries={}
                    #preparing top related queries to be visualized
                    for i in range(len(str(srch).split())):
                        for j in range(len(r_dict[str(srch).split()[i]]["top"]["query"])):
                            qq=r_dict[str(srch).split()[i]]["top"]["query"][j]
                            val=r_dict[str(srch).split()[i]]["top"]["value"][j]
                            queries[qq]=val 

                    top_queries={k: v for k, v in sorted(queries.items(), key=lambda item: item[1],reverse=True)}
                    print(top_queries)   
                    

                    vis = dv()
                    # bar = vis.plot_bar_chart_go(df1.head(), srch)
                    # time_series = vis.plot_time_series_go(tm_df, srch)

                    # Plotting a choropleth map using the "implemented plot_bar_chart_go function"
                    choro = vis.plot_choropleth_go(df1, srch)
                    
                    g_results = {
                        "choro": choro,
                        "srch":str(srch),
                        "top_queries":top_queries
                    }

                    return render(request, "scrape_trends/trends_search.html", g_results)

                except Exception as e:
                    print(e)
                    df1 = pd.DataFrame({})
                    return redirect("g_trends")

    else:
        return redirect("welcome")

def bar_chart(request,query):
    trends_list = []
    time_s = []
    rltd_dict = []
    # Query to get the stored data about the entered keyword from the database, if exists
    for p in Data_Save.objects.raw("select * from g_trends_data_Save where trend=%s", [str(query)]):
        trends_list.append(p.df)
        time_s.append(p.time_df)

    # Checking if the keyword was cached and stored in the database or not
    # If Not, scrape for the new data using the new keyword, then store it in the model "caching"
    if not trends_list:
        print("Empty")
        t = gt()
    # Scraping for trends "OverTime-ByRegion-RelatedDictionaries"
        tm_df, df1, r_dict = t.trends_scraping(
            kw=str(query).split())

    # Sorting desacendingly to get the most popular Regions
    #  that search for entered Keyword
        df1 = df1.sort_values(by=str(query).split(), ascending=[
                                False for x in range(len(df1.columns))])
        # df1_model = Data_Save(
        #     trend=str(query), df=df1, time_df=tm_df, rltd_dict=r_dict)
        # df1_model.save()

    # If it exists, just return the dataframe from the database
    else:
        df1 = trends_list[0]
        tm_df = time_s[0]

    labels=list(df1.head().index)
    data=[]
    for i in range(len(df1.head().columns)):
        y=df1.head()[str(query).split()[i]]
        data.append(list(y)) 

    clr=["#5c1ac3", "#e2a03f", "#e7515a", "#1abc9c", "#e0e6ed"]
    
    datasets=[]
    for i in range(len(data)):
        datasets.append({
                    'label': df1.head().columns[i],
                    'backgroundColor': clr[i],
                    'data': data[i],
                    'borderRadius': 7,
                },)
    #print(datasets)
    return JsonResponse(data={
        'labels': labels,
        'datasets': datasets,
    })


def time_series(request,query):
    trends_list = []
    time_s = []
    rltd_dict = []
    # Query to get the stored data about the entered keyword from the database, if exists
    for p in Data_Save.objects.raw("select * from g_trends_data_Save where trend=%s", [str(query)]):
        trends_list.append(p.df)
        time_s.append(p.time_df)

    # Checking if the keyword was cached and stored in the database or not
    # If Not, scrape for the new data using the new keyword, then store it in the model "caching"
    if not trends_list:
        print("Empty")
        t = gt()
    # Scraping for trends "OverTime-ByRegion-RelatedDictionaries"
        tm_df, df1, r_dict = t.trends_scraping(
            kw=str(query).split())

    # Sorting desacendingly to get the most popular Regions
    #  that search for entered Keyword
        df1 = df1.sort_values(by=str(query).split(), ascending=[
                                False for x in range(len(df1.columns))])
        # df1_model = Data_Save(
        #     trend=str(query), df=df1, time_df=tm_df, rltd_dict=r_dict)
        # df1_model.save()

    # If it exists, just return the dataframe from the database
    else:
        df1 = trends_list[0]
        tm_df = time_s[0]
    
    labels=list(tm_df.index[0::10])
    formatted_labels=[x.strftime('%d %b') for x in labels]
    #print(formatted_labels)
    data=[]
    
    for i in range(len(tm_df.columns)):
        y=tm_df[str(query).split()[i]][0::10]
        data.append(list(y)) 

    
    clr=["#5c1ac3", "#e2a03f", "#e7515a", "#1abc9c", "#e0e6ed"]
    bck_grnd=["rgba(92, 26, 195,0.2)","rgba(226, 160, 63,0.2)"
             ,"rgba(231, 81, 90,0.2)","rgba(26, 188, 156,0.2)",
             "rgba(224, 230, 237,0.2)"
             ]
    datasets=[]
    for i in range(len(data)):
        datasets.append({
                    'label': tm_df.head().columns[i],
                    'backgroundColor': bck_grnd[i],
                    'data': data[i],
                    'borderRadius': 7,
				    'borderColor':clr[i],
                    'borderWidth': 1,
				    'fill':True,
             
                },)
    #print(datasets)
    return JsonResponse(data={
        'labels': formatted_labels,
        'datasets': datasets,
    })

