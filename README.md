# Sparepart-API
Hajusrakendused
Exercise 3 - Varuosade API 

## List of requests and their paramaters

### GET /parts
#### Parameters
| Parameter | Value | Example | Description | Notes | 
| ----------- | ----------- | ----------- | ----------- | ----------- |
| page | Integer of page number | /parts?page=6 | returns sixth page | Default value is 0. Attempting to view page that doesn't exist returns 404 |
| page_size | Integer of results per page | /parts?page_size=10 | Returns 10 responses per page | Maximum integer limit is 20, default is 5 |
| search_by | String of the search category | /parts?search_by=name | Searches category "Name" for search | If empty returns all parts |
| search | String of the keyword for the search | /parts?search=engine | Returns everything that includes engine in its name | If empty returns all parts |
| sort_by | String of the sorting category  | /parts?sort_by=name  | Sorts the field by the category | Default value is name |
| decending | Boolean  | /part?decending=True | Reverses the sort | Default value is false |


