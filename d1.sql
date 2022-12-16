INSERT OVERWRITE DIRECTORY "s3://hiveoutput118/outputone/"
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t'
SELECT page_name, total_pageview 
FROM step02_output 
ORDER BY total_pageview DESC LIMIT 100;