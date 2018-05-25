--
-- CREATE VIEWS FOR logs_analysis_project.py
--

CREATE OR REPLACE VIEW total_group AS
(SELECT to_char(time, 'Month DD, YYYY') as date, count(status)as total
FROM log GROUP BY to_char(time,'Month DD, YYYY'));

CREATE OR REPLACE VIEW errors_group AS
(SELECT to_char(time, 'Month DD, YYYY') as date, count(status)as errors
FROM log WHERE status NOT LIKE '%200%' GROUP BY to_char(time,'Month DD, YYYY'));

CREATE OR REPLACE VIEW errors_rate_group AS
(SELECT total_group.date, total_group.total, errors_group.errors,
CAST(((CAST(errors_group.errors as float)/CAST(total_group.total as float))*100)
as decimal(9,2)) as rate  FROM total_group LEFT JOIN errors_group ON
total_group.date = errors_group.date);
