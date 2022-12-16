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
LOCATION "s3://outputstep2/outputall2/";

