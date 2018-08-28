# The following codes are programmed by Shanran Tang
# for Insight Data Engineering coding challenge.

import sys

# Open the window.txt file and read the averanging window size
with open(sys.argv[1],'r') as file1:
#with open('window.txt','r') as file1:
    window=int(file1.read())
print('The size of averaging window is %d.' % window)


# Open the actual.txt file and read the data into a list of dictionaries
print('processing actual data ...')
Actual=[]
i=0
with open(sys.argv[2],'r') as file2:
#with open('actual-test.txt','r') as file2:
    actual_data=file2.readlines()
    
    # Read each line and put the data into a list assuming pipe-delimited
    for line in actual_data:
        line_list=line.split('|')
        actual_hour=float(line_list[0])
        actual_hour=int(round(actual_hour))
        actual_stock=line_list[1]
        actual_price=float(line_list[2])
        actual_price=round(actual_price,2)
        
        # Add an item at the end of the list when it reads the data of the next hour
        # assuming the data are listed in chronological order
        if actual_hour-i>0:
            Actual.append({})
            i=i+1
            
        Actual[actual_hour-1][actual_stock]=actual_price    


# Open the predicted.txt file and read the data into a list of dictionaries
print('processing predicted data ...')
Predicted=[]
i=0
with open(sys.argv[3],'r') as file3:
    predict_data=file3.readlines()
    # Read each line and put the data into a list assuming pipe-delimited
    for line in predict_data:
        line_list=line.split('|')
        predict_hour=float(line_list[0])
        predict_hour=int(round(predict_hour))
        predict_stock=line_list[1]
        predict_price=float(line_list[2])
        predict_price=round(predict_price,2)
        
        # Add an item at the end of the list when it reads the data of the next hour
        # assuming the data are listed in chronological order
        if predict_hour-i>0:
            Predicted.append({})
            i=i+1
            
        Predicted[predict_hour-1][predict_stock]=predict_price


# Compute the hourly-averaged error and write the results in 'comparison.txt'
print('computing window-averaged errors ...')
with open(sys.argv[4],'w') as file4:
    for i in range(len(Predicted)-window+1):
        number=0 #'number' is the counter for the number of valid predictions found in one window
        error=0  #'error' is the sum of all the errors in one window
        for j in range(i,window+i): # Scan through all the hourly records in one window
            for stock in Predicted[j]: # Scan through all the stock in one dictionary in the lists
                if stock in Actual[j]:
                    error=error+abs(Predicted[j][stock]-Actual[j][stock])
                    number=number+1
        if number>0:
            c='%.2f' %(error/number)
        else: # Ouput 'NA' when there is no valid prediction found in one window
            c='NA'
        # Write the pipe-delimited data in 'comparison.txt'
        a=str(i+1)
        b=str(i+window)
        line_str=a+'|'+b+'|'+c+'\n'
        file4.write(line_str)    
print('Comparison has been done successfully!')

