DROP TABLE IF EXISTS step02_output;
CREATE TABLE step02_output (
    page_name STRING, 
    access_date STRING, 
    page_view STRING,
    total_pageview INT,
    popularity_trend INT,
    pageviews STRING) 
ROW FORMAT DELIMITED 
FIELDS TERMINATED BY '\t' 
LINES TERMINATED BY '\n' 
STORED AS TEXTFILE
LOCATION "s3://outputstep2/output2v2/";

INSERT OVERWRITE DIRECTORY "s3://hiveoutput118/sample1/"
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t'
SELECT page_name, total_pageview 
FROM step02_output 
ORDER BY total_pageview DESC LIMIT 100;

INSERT OVERWRITE DIRECTORY "s3://hiveoutput118/sample2/"
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t'
SELECT page_name, popularity_trend 
FROM step02_output 
ORDER BY popularity_trend DESC LIMIT 100;

INSERT OVERWRITE DIRECTORY "s3://hiveoutput118/sample3/"
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t'
SELECT page_name, access_date, page_view ,total_pageview, popularity_trend FROM step02_output 
    WHERE (lower(page_name)LIKE'champion')
    ORDER BY total_pageview DESC;
