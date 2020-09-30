# Explanation Task 1:

* I was asked to create a web app to plot some query data as a graph using dash.

* To do so, I created an abstract dbQuery class and then created a PSqlQuery class(derived one)
to connect to the wanted db.

* then I implemented in a server 2 functions -> get_table_columns, and get_2_numerical_columns =>

 ``` get_table_columns(list) =>```
 I was not sure weather to show all columns and then filter the results to get only numeric values, or to show from the beginning only numeric columns,
 so I implemented it both ways (and used the one where I show all columns)
 
 ```get_2_numerical_columns(col1, col2) => ```
 this function gets 2 columns and returns the values for a couple of numeric columns, else returns empty list(an empty graph will be plotted) 
