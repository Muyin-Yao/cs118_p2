DROP TABLE IF EXISTS step02_output;
CREATE TABLE step02_output (
    page_name STRING, 
    access_date STRING, 
    page_view STRING,
    total_pageview int,
    popularity_trend int
    pageviews STRING) 
ROW FORMAT DELIMITED 
FIELDS TERMINATED BY '\t' 
LINES TERMINATED BY '\n' 
STORED AS TEXTFILE
LOCATION "${INPUT}";


INSERT OVERWRITE DIRECTORY "${OUTPUT1}"
SELECT page_name, total_pageview 
FROM step02_output 
ORDER BY total_pageview DESC LIMIT 100;


INSERT OVERWRITE DIRECTORY "${OUTPUT2}"
SELECT pagename, popularity_trend 
FROM step02_output 
ORDER BY popularity_trend DESC LIMIT 100;

INSERT OVERWRITE DIRECTORY "${OUTPUT3}"
SELECT * 
FROM step02_output 
WHERE INSTR(pagename, '${SEARCHTERM}') != 0;

