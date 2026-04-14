/*
a) actor_id, first_name, last_name, last_update
b) film_id, title, description, release_year, language_id, original_language, rental_duration, rental_rate, length, replacement_cost, rating, special_features, last_update
c) another table to view is in views
d) it includes 1000 rows of rental_id, inventory_id, customer_id, return_date, staff_id, last_update. It's a little hard to read right now, seeing all this information in a condensed view.
e) it includes inventory_id, film_id, store_id, and last_update
f) I would say inside views. These tables are related to eachother due to having actor_info, customer_list, and film_list within one another. 
*/

SELECT film_id FROM film;
SELECT actor_id FROM actor;