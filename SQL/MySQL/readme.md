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