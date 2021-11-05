-- Delete existing table that's maybe made earlier on
DROP TABLE recommendationsBasedOnTitleFieldStepUp;

-- Rank is computed with the text search function (ts rank). In this text search function has input arguments from the title field of the favorite movie. 
UPDATE movies6
SET rank = ts_rank(lexemesTitle,plainto_tsquery(
(  
SELECT Title FROM movies6 WHERE url='step-up'
)
));

-- the top 50 of recommended movies is stored in a table. The 50 movies are sorted in rank order from biggest to smallest. 
CREATE TABLE IF NOT EXISTS recommendationsBasedOnTitleFieldStepUp AS 
SELECT url, rank FROM movies6 WHERE rank < 0.99 ORDER BY rank DESC LIMIT 50;

-- the created table with top 50 movies is saved in the given folder.
\copy (SELECT * FROM recommendationsBasedOnTitleFieldStepUp) to '/home/pi/RSL/top50recommendationstitlestepup.csv' WITH csv;
