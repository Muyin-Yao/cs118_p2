INSERT OVERWRITE DIRECTORY "s3://hiveoutput118/outputtwo/"
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t'
SELECT page_name, popularity_trend 
FROM step02_output 
ORDER BY popularity_trend DESC LIMIT 100;