#!/usr/bin/env python
# coding: utf-8

# In[85]:


import pandas as pd


# In[86]:


# Let us create a dataframe that we would use for this exercise first
# We will be scraping through the web to do that

# Create url link variable
url_link = "https://en.wikipedia.org/wiki/List_of_highest-grossing_films"

# Create DataFrame
movies_data = pd.read_html(url_link)
# Subset dataframe at index 0- first table
movies_data = movies_data[0]

# Display the first 5 rows of the data
print(movies_data.head())


# In[87]:


### DATA INSPECTION


# In[88]:


# Get a statistical summary of the data, this is for only the numerical aspect of the data
movies_data.describe()


# In[89]:


# Checking the shape of the data showing how many rows and columns are in the data
movies_data.shape


# In[90]:


# This returns the size of the data and its usually number of rows multiplied by number of columns
movies_data.size


# In[91]:


# Returns concise information about a dataframe
movies_data.info()


# In[92]:


# Returns the column names in your data
movies_data.columns


# In[93]:


# Print the first 10 rows to inspect the data
movies_data.head(10)


# In[94]:


# Print the last 10 rows
movies_data.tail(10)


# In[95]:


### DATA CLEANING


# In[96]:


# Let us view a portion of the data
movies_data.head()


# In[97]:


# Business cases determine the kind of analysis to be carried out on a dataset
# We do not need the reference column in this data so we will be dropping it

del movies_data["Ref"]


# In[98]:


# Change the column name Worldwide gross to Global Gross($)
movies_data.rename(columns={"Worldwide gross":"Global Gross($)"}, inplace=True)


# In[99]:


# Proceed to clean the Global Gross($) column so we can have numerical values only for quantitative analysis
movies_data["Global Gross($)"] = movies_data["Global Gross($)"].str.replace("$","")
movies_data["Global Gross($)"] = movies_data["Global Gross($)"].str.replace(",","")


# In[100]:


# Let us inspect it to see if we have just numbers alone now
movies_data["Global Gross($)"].unique()

# Some portions of the data still have string vlaues like F, T in them


# In[101]:


# We can see that Global Gross($) still has some characters like "F" and "T" that need removing
movies_data["Global Gross($)"] = movies_data["Global Gross($)"].str.replace("T","")
movies_data["Global Gross($)"] = movies_data["Global Gross($)"].str.replace("F","")


# In[102]:


# Let us inspect it to see if we have just numbers alone now
movies_data["Global Gross($)"].unique()


# In[103]:


# A quick look at our Title column also reveals special characters that need to be dealt with
movies_data["Title"].unique()


# In[104]:


movies_data["Title"] = movies_data["Title"].str.replace("†","") #Remove special characters from the Title column


# In[105]:


# Cleaning Peak column for special characters
movies_data["Peak"] = movies_data["Peak"].str.replace("RK","")
movies_data["Peak"] = movies_data["Peak"].str.replace("TS","")
movies_data["Peak"] = movies_data["Peak"].str.replace(".","")


# In[106]:


movies_data["Peak"].unique()


# In[107]:


# A look at our data also reveals that Peak and Global Gross are objects and we need them in numerical formats
movies_data.info()


# In[108]:


movies_data[["Peak"]] = movies_data[["Peak"]].astype(int)
movies_data[["Global Gross($)"]] = movies_data[["Global Gross($)"]].astype(float)


# In[109]:


# Taking a last look at our data, the global gross for the fate of the furious has mysteriously jumped up, let's fix that
movies_data.loc[movies_data["Title"] == "The Fate of the Furious"]


# In[110]:


movies_data['Global Gross($)'].replace(81238764765, 1238764765, inplace=True)


# In[111]:


# View the data
movies_data

# Now we have a clean data to work with


# In[112]:


### ANALYSIS OF THE DATA TO GET INSIGHTS


# In[113]:


# What is the highest grossing film of all time worldwide?
gross = movies_data["Global Gross($)"].max()
movies_data[movies_data["Global Gross($)"] == gross]


# In[114]:


movies_data.groupby("Title")["Global Gross($)"]


# In[115]:


# Movies that have grossed over $2 billion worldwide?
movies_data[movies_data["Global Gross($)"] > 2000000000]


# In[116]:


# How many of the top 10 highest grossing films were released in the 21st century?
movies_data[(movies_data["Rank"] < 11) & (movies_data["Year"] > 2001)]


# In[117]:


# Sort the movies by years to uncover trends
gross_year = movies_data.groupby("Year")["Global Gross($)"].sum()
gross_year_sorted = gross_year.sort_values(ascending=False)
gross_year_sorted


# In[118]:


# Visualize the data
gross_year_sorted.plot(kind="bar", rot=60)


# In[ ]:# Export file as as csv file
movies_data.to_csv("Movies Data")





# In[ ]:





# In[ ]:





# In[ ]:




