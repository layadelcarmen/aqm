-- View Sum per Year for measure: 'Number of days with maximum 8-hour average ozone concentration over the National Ambient Air Quality Standard'


--Query 1

CREATE OR REPLACE VIEW vw_sum_no_days_with_max_avg_over_ozone_concentration_per_year AS

SELECT SUM(value) AS sum_days, reportyear 
FROM 
  public.measures_air_quality
WHERE measurename = 'Number of days with maximum 8-hour average ozone concentration over the National Ambient Air Quality Standard'
GROUP BY reportyear
ORDER BY reportyear DESC
;

--Query 2


CREATE OR REPLACE VIEW vw_year_with_max_no_days_ozone_conc AS
WITH sum_no_days_year as ( 
  SELECT SUM(value) AS sum_days, reportyear 
  FROM public.measures_air_quality
  WHERE measurename = 'Number of days with maximum 8-hour average ozone concentration over the National Ambient Air Quality Standard'
    and reportyear >= 2008
  GROUP BY reportyear
  ORDER BY reportyear DESC
)
SELECT
   reportyear
FROM 
   sum_no_days_year 
WHERE sum_no_days_year.sum_days = (select MAX(sum_days) from sum_no_days_year)
;

--Query 3: Max value for each measure per state


CREATE OR REPLACE VIEW vw_max_measure_value_per_state AS

SELECT  
  measurename,
  statename,
  MAX(value) AS max_measure_value
FROM 
  public.measures_air_quality
GROUP BY measurename, statename
;    
    
    
 -- Query 4: avg Number of person-days with PM2.5 per year and state
 
CREATE OR REPLACE VIEW vw_avg_persons_day_with_pm25_per_year_state AS

SELECT 
  reportyear,
  statename,
  AVG(value) as avg_person_day_pm25

FROM 
  public.measures_air_quality
WHERE 
  measurename = 'Number of person-days with PM2.5 over the National Ambient Air Quality Standard (monitor and modeled data)'
GROUP BY reportyear, statename
ORDER BY reportyear, statename ASC
;
	

--Query 5: State with max accumulate 'Number of days with maximum 8-hour average ozone concentration over the National Ambient Air Quality Standard

CREATE OR REPLACE VIEW vw_max_accumulate_no_days_with_avg_ozone_concent_per_state AS
WITH accumulate_state AS (
  SELECT 
    SUM(value) AS sum_days,
    statename 
  FROM 
    public.measures_air_quality
  WHERE measurename = 'Number of days with maximum 8-hour average ozone concentration over the National Ambient Air Quality Standard'   
  GROUP BY statename
) 
SELECT 
  statename,
  sum_days
FROM
  accumulate_state
WHERE
  sum_days = (SELECT MAX(sum_days) FROM accumulate_state)
;
  
  
-- Query 6: AVG Number of person-days with maximum 8-hour average ozone concentration in state Florida

CREATE OR REPLACE VIEW vw_avg_person_day_wt_max_8hr_state AS

SELECT 
  AVG(value) AS avg_days, 
  statename 
FROM 
   public.measures_air_quality
WHERE 
   measurename = 'Number of person-days with maximum 8-hour average ozone concentration over the National Ambient Air Quality Standard'   
   and statename = 'Florida'
GROUP BY 
   statename
;  
   
   --Query 7: County with min 'Number of days with maximum 8-hour average ozone concentration over the National Ambient Air Quality Standard'
   --per state per year
   
CREATE OR REPLACE VIEW vw_county_with_min_no_days_avg_ozone_concent_per_state_year AS
SELECT 
  countyname,
  statename,
  reportyear,
  value
FROM
(
SELECT 
  value,
  reportyear,
  countyname,
  statename,
  MIN(value) OVER (PARTITION BY measurename,reportyear,statename) AS min_state_val
FROM 
  measures_air_quality
WHERE measurename = 'Number of days with maximum 8-hour average ozone concentration over the National Ambient Air Quality Standard'
)min_state_values
WHERE 
  value  = min_state_val

ORDER BY reportyear, statename, countyname ASC
