# Mongo DB in Flask Demo
Covers basic CRUD operations using `pymongo`, and connecting to a MongoDB client. 

## Challenges
- 1) Create a clear post route that deletes everything
- 2) Format the dates in Month, Day, Year format using your `model.py` and the `datetime` library

## Key Points
- After a POST request, use `redirect("/route")` instead of `render_template()` if you want your user to navigate to another page.
- The general format of a mongoDB entry is:
```
{
    "field_name" : "field_value",
    "field_name_2" : "field_value_2",
    ...
    "field_name_n" : "field_value_n"
}
```
- A **query** is/are field(s) and value(s) used to look up entries with matching field(s)/value(s), e.g `{"date" : "12-23-08"}`
- Your CRUD operations are
  - (CREATE) `insert_one(entry)` and `insert_many(entries)`,
  - (READ) `find_one(query)` and `find_many(query)`,
  - (UPDATE) `update_one(query, new_val)` and `update_many(query, new_val)`,
  - (DELETE) `delete_one(query)` and `delete_many(query)`.
- You can use loops in Jinja3 with `{% statement %}`. 