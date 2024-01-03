# Family Static API

This project was designed to give us more practice with data structures and creating an API using Python, but specifically through a class-based structure instead of a function based structure. We used Postman to test our endpoints. 

My code can be found within the "src" folder. 

## Project Notes 
- Install the project dependencies by running `$ pipenv install`.
- Get inside the virtual environment by running `$ pipenv shell`
- Start the server by running `$ pipenv run start`
- Test your code by running `$ pipenv run test` --> Automatic grading!

## 📝 Instructions

1) Create the code needed to implement the API endpoints described further below.  

2) The only two files you have to edit are:  

- `src/datastructure.py`: Contains the class with the rules on how to manage the family members.  
- `src/app.py`: Contains the API, it uses the Family as data structure.  

## Data structures

Every **member** of the Jackson family must be a dictionary - the equivalent of [Objects Literals in JS](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_Objects) - and have these values:

```python
    + id: Int
    + first_name: String
    + last_name: String (Always Jackson)
    + age: Int > 0
    + lucky_numbers: Array of int
```
The **family** data-structure will be a class with the following structure:

```python
class Family:

    def __init__(self, last_name):
        self.last_name = last_name
        # example list of members
        self._members = [{
            "id": self._generateId(),
            "first_name": "John",
            "last_name": last_name
        }]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return random.randint(0, 99999999) //import random 

    def add_member(self, member):
        ## you have to implement this method
        ## append the member to the list of _members
        pass

    def delete_member(self, id):
        ## you have to implement this method
        ## loop the list and delete the member with the given id
        pass

    def update_member(self, id, member):
        ## you have to implement this method
        ## loop the list and replace the member with the given id
        pass

    def get_member(self, id):
        ## you have to implement this method
        ## loop all the members and return the one with the given id
        pass

    def get_all_members(self):
        return self._members
```

Note: don't forget to initialize the class: `jackson_family = FamilyStructure('Jackson')` *before* the routes.

## These are the initial Family Members

```md
John Jackson
33 Years old
Lucky Numbers: 7, 13, 22

Jane Jackson
35 Years old
Lucky Numbers: 10, 14, 3

Jimmy Jackson
5 Years old
Lucky Numbers: 1
```

## Endpoints

This API must have 4 endpoints. They all return JSON:

### 1) Get all family members:

Which returns all members of the family.

```md
GET /members

status_code: 200 if success. 400 if bad request (wrong info) screw up, 500 if the server encounter an error

RESPONSE BODY (content-type: application/json):

[], // List of members.

```

### 2) Retrieve one member

Which returns the member of the family where `id == member_id`.

```md
GET /member/<int:member_id>

RESPONSE (content_type: application/json):

status_code: 200 if success. 400 if bad request (wrong info) screw up, 500 if the server encounter an error

body: //the member's json object

{
    "id": Int,
    "first_name": String,
    "age": Int,
    "lucky_numbers": List
}

```

### 3) Add (POST) new member

Which adds a new member to the family data structure.

```md
POST /member

REQUEST BODY (content_type: application/json):

{
    first_name: String,
    age: Int,
    lucky_numbers: [],
    id: Int *optional
}

RESPONSE (content_type: application/json):

status_code: 200 if success. 400 if a bad request (wrong info) screw up, 500 if the server encounters an error

body: empty
```

Keep in mind that POST request data dictionary may contain a key and a value for this new member `id`.
- If it does not, your API should randomly generate one when adding family members.
- If it does include it, that is the value to be used for such end.

### 4) DELETE one member

Which deletes a family member with `id == member_id`

```md
DELETE /member/<int:member_id>

RESPONSE (content_type: application/json):

status_code: 200 if success. 400 if a bad request (wrong info) screw up, 500 if the server encounters an error

body: {
    done: True
}    

```

## Requirements

- All requests and responses should be in content/type: application/json
- Response codes must be `200` for success, `400` for bad request or `404` for not found.
- These exercises do not include a database, everything must be done in Runtime (RAM).
