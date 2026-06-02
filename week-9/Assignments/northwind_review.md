# Table: Categories

-- Primary Key: CategoryID
-- Parent Tables (foreign keys joint to): none

# CategoryID
-- Represents: Unique ID for each category
-- Primary Key? Yes
-- Foreign Key? No
-- Keep in Power BI? Yes - needed to link to products table 
-- Name appropriate? Yes (though its a key, not shown in reports)
-- Power BI data type: Whole number 
-- Possible calculations: COUNT of categories

# CategoryName
-- Represents: The name of the category
-- Primary Key? No
-- Foreign Key? No
-- Keep in Power BI? Yes - useful label for grouping/filtering
-- Name appropriate? Rename to "Category" for cleaner reports
-- Power BI data type: Text
-- Possible calculations: GROUP BY category, COUNT products per category

# Description
-- Represents: Long text description of the category
-- Primary Key? No
-- Foreign Key? No
-- Keep in Power BI? No - too long for analysis, not aggregatable
-- Power BI data type: Text
-- Possible calculations: None

# Picture
-- Represents: Long text description of the category
-- Primary Key? No 
-- Foreign Key? No
-- Keep in Power BI? No - binary data, can't be used in visuals
-- Power BI data type: N/A
-- Possible calculations: None