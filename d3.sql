INSERT OVERWRITE DIRECTORY "s3://hiveoutput118/outputthree/champion/"
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t'
SELECT page_name, access_date, page_view ,total_pageview, popularity_trend FROM step02_output 
    WHERE (lower(page_name) LIKE '%champion%' )
    ORDER BY total_pageview DESC;

INSERT OVERWRITE DIRECTORY "s3://hiveoutput118/outputthree/set/"
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t'
SELECT page_name, access_date, page_view ,total_pageview, popularity_trend FROM step02_output 
    WHERE (lower(page_name)LIKE'%set%')
    ORDER BY total_pageview DESC;

INSERT OVERWRITE DIRECTORY "s3://hiveoutput118/outputthree/accent/"
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t'
SELECT page_name, access_date, page_view ,total_pageview, popularity_trend FROM step02_output 
    WHERE (lower(page_name)LIKE'%accent%')
    ORDER BY total_pageview DESC;


INSERT OVERWRITE DIRECTORY "s3://hiveoutput118/outputthree/world/"
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t'
SELECT page_name, access_date, page_view ,total_pageview, popularity_trend FROM step02_output 
    WHERE (lower(page_name)LIKE'%world%')
    ORDER BY total_pageview DESC;
