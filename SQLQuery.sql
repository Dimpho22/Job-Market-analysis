SELECT *
FROM jobs;

SELECT TOP 10 * FROM jobs;

SELECT COUNT(*) AS total_jobs FROM jobs;

SELECT COUNT(DISTINCT Company) AS unique_companies FROM jobs;

SELECT TOP 10
       Company,
       COUNT(*) AS total_jobs
FROM jobs
GROUP BY Company
ORDER BY total_jobs DESC;

SELECT TOP 10
       [Job_Title],
       COUNT(*) AS total_postings
FROM jobs
GROUP BY [Job_Title]
ORDER BY total_postings DESC;


SELECT TOP 10
       Location,
       COUNT(*) AS total_jobs
FROM jobs
GROUP BY Location
ORDER BY total_jobs DESC;

SELECT Company,
       Location,
       COUNT(*) AS total_jobs
FROM jobs
GROUP BY Company, Location
ORDER BY total_jobs DESC;


SELECT *
FROM jobs
WHERE Company = 'Payne, Roberts and Davis';

SELECT *
FROM jobs
WHERE [Job_Title] LIKE '%Developer%';

SELECT
    COUNT(*) AS total_jobs,
    COUNT(DISTINCT Company) AS unique_companies
FROM jobs;

CREATE VIEW company_job_summary AS
SELECT Company,
       COUNT(*) AS total_jobs
FROM jobs
GROUP BY Company;

SELECT *
FROM company_job_summary;

SELECT
    Company,
    [Job_Title],
    Location
FROM jobs
ORDER BY Company ASC;


