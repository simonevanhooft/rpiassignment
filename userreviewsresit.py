#importing and reading the csv file
import csv
import time

startTime = time.time()

with open('userReviews.csv', encoding='utf-8-sig') as reviews:
    reader = csv.DictReader(reviews, delimiter=';')
    reviews_df = list(reader)

#compute the average of the user score for step up over all reviews, (m)
    A = list()
    for row in reviews_df:
        if row['movieName'] == 'step-up':
            A.append(row['Metascore_w'])
            
    a = list(map(int, A))
    def Average(a):
        return sum(a) / len(a)
    m = Average(a)
    print('m = ', round(m,2))    
    
#Create a list with all the authors who made a review about Step Up
    B = list()
    for row in reviews_df:
        if row['movieName'] == 'step-up':
            B.append(row['Author'])
    Bset = set(B)
    Blist = list(Bset)
            
#Print out all the movies who has been seen by the author and have the same or a higher score
    D = []
    for row in reviews_df:
        if row['Author'] in B and row['Metascore_w'] >= '7.35':
            D.append(row['movieName'])
    dset = set(D)
    dlist = list(dset)

#Export list D            
rows = zip(dlist)
with open('List D.csv', 'w') as f:
    writer = csv.writer(f)
    for row in rows:
        writer.writerow(row)

#calculate the execution time
executionTime = (time.time() - startTime)
print('Execution time in seconds: ' +str(executionTime))
        