INSERT OVERWRITE DIRECTORY "s3://{OUTPUT2}"
SELECT pagename, popularity_trend 
FROM step02_output 
ORDER BY popularity_trend DESC LIMIT 100;