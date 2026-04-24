USE murder_mystery;

-- Crime Scene Report
SELECT *
FROM crime_scene_report
WHERE type = 'murder'
      and date = 20180115
      and city = 'SQL City';
      
-- Find Witnesses

-- Witness #1
SELECT *
FROM person
WHERE address_street_name = 'Northwestern Dr'
ORDER BY address_number DESC
LIMIT 1;

-- Witness #2, named Annabel on Franklin Ave
SELECT *
FROM person
WHERE name LIKE 'Annabel%'
           AND address_street_name = 'Franklin Ave';
-- Get their Real IDs
SELECT person_id
FROM interview;
    
-- Interview Transcripts
SELECT *
FROM interview
WHERE person_id IN (14887, 16371);
-- Both witnesses mentioned a "Get Fit Now Gym" bag that had a membership number starting with 48Z
-- Then a car plate containing H42W
SELECT p.name,
       p.id
FROM person p 
JOIN get_fit_now_member gfm ON p.id = gfm.person_id
JOIN get_fit_now_check_in gfc ON gfm.id = gfc.membership_id
WHERE gfm.id LIKE '48z%'
             AND gfm.membership_status = 'Gold'
			 AND gfc.check_in_date = 20180109;
-- Read Suspects Interviews
SELECT * 
FROM interview 
WHERE person_id IN (67318, 28073);

-- So who hired him to kill the victim?
-- Find out who he was hired by
SELECT p.name,
       p.id
FROM person p 
JOIN drivers_license dl ON p.license_id = dl.id
JOIN facebook_event_checkin fb ON p.id = fb.person_id
WHERE dl.gender = 'female'
AND dl.hair_color = 'red'
AND dl.car_make = 'tesla'
AND dl.car_model = 'model S'
AND dl.height BETWEEN 65 AND 67
AND fb.event_name = 'SQL symphony concert'
AND fb.date BETWEEN 20171201 AND 20171231
GROUP BY p.id, p.name
HAVING count(*) = 3;

-- Our suspect is Miranda Priestly ID# 99716