INSERT OVERWRITE DIRECTORY "s3://{OUTPUT3}"
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t'
SELECT page_name, access_date, total_pageview, popularity_trend FROM step02_output 
    WHERE (lower(page_name) LIKE '%champion%' OR lower(page_name)LIKE'%set%' OR  lower(page_name)LIKE'%accent%' OR  lower(page_name)LIKE'%world%' )
    ORDER BY total_pageview DESC;
