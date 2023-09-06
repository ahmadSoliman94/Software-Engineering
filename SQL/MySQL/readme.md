## SQL


### 1. To select database
```bash 
USE `database_name`; 
```

###  2.  Select all columns from table that match the condition
```bash
SELECT * FROM `table_name`  # *: means all columns
WHERE `column_name` = 'value'; # WHERE: condition
```

### 3. if the column is a number, we can add to the values 
```bash
SELECT `column_name + 1 FROM `table_name`; AS 'name' # +1: add 1 to the value, AS 'name' : rename the column (Alias)
```

### 4. To select distinct values from a column
```bash
SELECT DISTINCT `column_name` FROM `table_name`; # DISTINCT: distinct values means no duplicates.
```

### 5. Where clause
```bash 
SELECT * FROM `table_name` WHERE  NOT `column_name` = 'value'; # WHERE NOT: not equal to
```

### 6. Where clause with multiple conditions
```bash
SELECT * FROM `table_name` WHERE `column_name` = 'value' AND `column_name` = 'value'; # AND: both conditions must be true
SELECT * FROM `table_name` WHERE `column_name` = 'value' OR `column_name` = 'value'; # OR: one of the conditions must be true
```

```bash
SELECT * FROM `table_name` WHERE `column_name` IN ('value', 'value'); # IN: one of the conditions must be true
```

```bash
SELECT * FROM `table_name` WHERE `column_name` BETWEEN 'value' AND 'value'; # BETWEEN: value must be between the two values
```

```bash
SELECT * FROM `table_name` WHERE `column_name` LIKE '%b%'; # LIKE: value must contain the letter b
```

```bash
SELECT * FROM `table_name` WHERE `column_name` LIKE 'b%'; # LIKE: value must start with the letter b
```

```bash	
SELECT * FROM `table_name` WHERE `column_name`  REGEXP '^[0-9]'; # REGEXP: value must be a nmber between 0 and 9 (you can use any regular expression)
```

 ```bash
 SELECT * FROM `table_name` ORDER BY `column_name` ASC; # ORDER BY: sort the values in ascending order
 ```

```bash
SELECT * FROM `table_name` ORDER BY `column_name` DESC; # ORDER BY: sort the values in descending order
```

```bash
SELECT * FROM `table_name` ORDER BY `column_name` ASC, `column_name` DESC; # ORDER BY: sort the values in ascending order and then in descending order
```

```bash
SELECT * FROM `table_name` ORDER BY `column_name` ASC LIMIT 2,2; # LIMIT: show only 2 rows starting from the 3rd row
```

---- 

### INNER JOIN: is used to combine each row from one table with every row from another table if the join condition is true.

![1](images/1.png)

```bash
SELECT * FROM `table_name` t INNER JOIN `table_name` ON `table_name`.`column_name` = `table_name`.`column_name`; # INNER JOIN: combine each row from one table with every row from another table if the join condition is true., t: alias
```


### JOIN CONDITION: is used to combine each row from one table with every row from another table if the join condition is true.

```bash
SELECT * FROM `table_name` t INNER JOIN `table_name` ON `table_name`.`column_name` = `table_name`.`column_name`AND  `table_name`.`column_name` = `table_name`.`column_name`;  # AND: join condition
````

### Outer Join: is used to combine each row from one table with every row from another table regardless of the join condition. if the query does not have a match in the table, the result set will contain NULL.

```bash	
SELECT * FROM `table_name` t LEFT JOIN `table_name` ON `table_name`.`column_name` = `table_name`.`column_name`; # LEFT OUTER JOIN: combine each row from one table with every row from another table regardless of the join condition. if the query does not have a match in the table, the result set will contain NULL., t: alias
```

### USING(): is used to specify a column that exists in both tables to join them instead of using the ON clause.

```bash
SELECT * FROM `table_name` t LEFT JOIN `table_name` USING(`column_name`); # USING(): specify a column that exists in both tables to join them., t: alias
```

### UNION: is used to combine the result set of two or more SELECT statements. Each SELECT statement within UNION must have the same number of columns. The columns must also have similar data types. Also, the columns in each SELECT statement must be in the same order.

```bash	
SELECT * FROM `table_name` UNION SELECT * FROM `table_name`; # UNION: combine the result set of two or more SELECT statements.
```

### LABLING EXAMPLE:
    
```bash
select
 customer_id, 
 first_name, 
 points, 
 'Bronze' as Labels
from customers
where points < 2000
union
select
 customer_id, 
 first_name, 
 points, 
 'Silver' as Labels
from customers
where points between 2000 and 3000
union
select
 customer_id, 
 first_name, 
 points, 
 'Gold' as Labels
from customers
where points > 3000 
```

--- 

### INSERT INTO: is used to insert new rows into the table.

```bash
INSERT INTO `table_name` (`column_name`, `column_name`) VALUES ('value', 'value'); 
AUTO_INCREMENT: is used to generate a unique number automatically when a new record is inserted into a table.
NOT NULL: is used to specify that a column cannot contain NULL value.
DEFAULT: is used to set a default value for a column when no value is specified.
```

### INSERT multiple rows into the table.

```bash
INSERT INTO `table_name` (`column_name`, `column_name`) VALUES ('value', 'value'), ('value', 'value'), ('value', 'value'); 
```


### LAST_INSERT_ID(): is used to get the last value inserted into an AUTO_INCREMENT column.

```bash
INSERT INTO `table_name` (`column_name`, `column_name`) VALUES ('value', 'value');
INSERT INTO `table_name2` (`column_name`, `column_name`) VALUES (LAST_INSERT_ID(), 'value'); # in this case, the value of the column_name will be the last value inserted into an  the new table with the column_name
```

### SUBQUERY: is a query nested inside another query such as SELECT, INSERT, UPDATE or DELETE.

```bash
CREATE TABLE `table_name` AS SELECT * FROM `table_name`; # CREATE TABLE: create a new table based on the result set of a SELECT statement.
```

----

### UPDATE: is used to modify existing records in a table.

```bash
UPDATE `table_name` SET `column_name` = 'value', `column_name` = 'value' WHERE `column_name` = 'value'; # UPDATE: modify existing records in a table.
```

```bash
UPDATE `table_name` SET `column_name` = 'value', `column_name` = 'value' WHERE `column_name` IN ('value', 'value'); # UPDATE: modify existing records in a table., IN('value', 'value') that means the value must be one of the values in the list
```

```bash	
use sql_store;
update orders
set comments = 'GOLD'
where customer_id in (

select customer from customers
where points > 3000
);
```

### this query will:

1. Switch to the sql_store database.
2. Update the orders table.
3. Change the value of the comments field to 'GOLD' for all orders where the customer_id is in the list of customers who have more than 3000 points.

---

### aggregate functions: are used to perform calculations on a set of values and return a single value.

```bash
MAX(): is used to return the maximum value in a column.
MIN(): is used to return the minimum value in a column.
SUM(): is used to return the sum of the values in a column.
AVG(): is used to return the average value in a column.
COUNT(): is used to return the number of rows in a table.
```

---

### GROUP BY: is used to group the result set based on one or more columns.

```bash
SELECT `column_name`, `aggregate_function`(`column_name`) FROM `table_name` GROUP BY `column_name`; # GROUP BY: group the result set based on one or more columns.
```

#### HAVING: is used to filter records that work on summarized GROUP BY results.

```bash
SELECT `column_name`, `aggregate_function`(`column_name`) FROM `table_name` GROUP BY `column_name` HAVING `aggregate_function`(`column_name`) > value; # HAVING: filter records that work on summarized GROUP BY results.
```

### HAVING vs WHERE: 
#### WHERE clause is used to filter records before any groupings are made. It acts on a row-by-row basis.

#### HAVING clause is used to filter records after the groupings are made. It acts on the summarized or aggregated data.