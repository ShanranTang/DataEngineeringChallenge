The source code was programed by applicant Shanran Tang using Python 3.7 and was tested in both windows 10 and Linux Ubuntu systems.

The main data structure is a list in which each item is a dictionary. The index of items represents the hour in time. The keys and values of a dictionary represent the name of the stocks (string type) and the price of the stocks (float type), respecetively.
The actual.txt and predicted.txt files are read line by line as string variables. Each line is splited and converted into three variables: hour (integer), stock name (string), and stock price (float). These variables are assigned to the two main lists, one list for the actual data, one for the predicted data.
In the error calculation, a for-loop is established to go through all the items (hours) in the two lists for an averaging window. In the same hour, the stock price values in actual item and in the predicted item are compared. Then the averaged error of a window is computed at the end of the window loop. Another for-loop is estabished outside the window for-loop to go through all the hours in time, in which the window-averaged errors are written to the 'comparison.txt' file line by line following the specified format.

It is assumed that the input data are listed in in chronological order and pipe-delimited.
