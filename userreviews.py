#importing and reading the csv file
import csv
import time

startTime = time.time()

with open('userReviews.csv', encoding='utf-8-sig') as reviews:
    reader = csv.DictReader(reviews, delimiter=';')
    
    reviews_df = list(reader)

#devined author as variable of interest and save contents in list X
    X = list()
    for row in reviews_df:
        X.append(row['Author'])
    

#filtert on my favorite movie: Step Up, list with only the authors who wrote a review of my favorite movie and saved in list Y
    Y = list()
    for row in reviews_df:
        if row['movieName'] == 'step-up':
            Y.append(row['Author'])
   

#for every author in list Y, checked which other films has been watched by these authors and saved in list Z
    Z = list()
    for row in reviews_df:
        if row['Author'] in Y:
            Z.append(row['movieName'])
            
    
#export all three the lists in three individual csv files
rows = zip(X)
with open('List X.csv', 'w') as f:
    writer = csv.writer(f)
    for row in rows:
        writer.writerow(row)
        
rows2 = zip(Y)
with open('List Y.csv', 'w') as f:
    writer = csv.writer(f)
    for row in rows2:
        writer.writerow(row)

rows3 = zip(Z)
with open('List Z.csv', 'w') as f:
    writer = csv.writer(f)
    for row in rows3:
        writer.writerow(row)

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' +str(executionTime))

    
    






