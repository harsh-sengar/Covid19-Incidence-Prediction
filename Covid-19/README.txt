All the programs are python program and also shell script file is included for every question program. You can invoke any program from within the shell file. The programs should run in the Linux operating system.

Dependencies - Python Libraries (json, numpy, pandas, difflib, collections, requests, pandas, csv, operator)

Question 1:
Run command sh neighbor-districts-modified.sh in your linux terminal this will create neighbor-districts-modified.json file. Which is containing districts as per available in COVID - 19 portal and all the districts are sorted in alphabetical order. One more file will be created with this is district-id.csv that is containing districtid (101 onwards) and districts in alphabetical order.

Question 2:
Run command sh case-generator.sh in your linux terminal, it will generate three csv files cases-week.csv,  cases-month.csv,  cases-overall.csv. these files are containing districtwise information about COVID cases.

Question 3:
Run command sh edge-generator.sh in your linux terminal, it will generate one csv file edge-graph.csv. these files are containing districtwise information about COVID cases. Containing  (i, j) districts,
district i has an edge with district j,

Question 4:
Run command sh neighbor-generator.sh in your linux terminal, it will generate three csv files neighbor-week.csv,  neighbor-month.csv,  neighbor-overall.csv. these files are containing districtwise information about neighbormean, neighborstdev.

Question 5:
Run command sh state-generator.sh in your linux terminal, it will generate three csv files state-week.csv,  state-month.csv,  state-overall.csv. these files are containing districtwise information about the average and standard deviation of the number of cases of all the other districts in the state.

Question 6:
Run command sh zscore-generator.sh in your linux terminal, it will generate three csv files zscore-week.csv,  zscore-month.csv,  zscore-overall.csv. these files are containing districtwise information about z-score for every week, month, and overall, using separately the neighborhood and the state information.

Question 7:
Run command sh method-spot-generator.sh in your linux terminal, it will generate three csv files method-spot-week.csv,  method-spot-month.csv,  method-spot-overall.csv. these files are containing timse based week, month, overall information about Each hotspot/coldspot.

Question 8:
Run command sh top-generator.sh in your linux terminal, it will generate three csv files top-week.csv,  top-month.csv,  top-overall.csv. these files are containing timse based week, month, overall information about top 5 hotspot/coldspot.




