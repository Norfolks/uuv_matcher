## Installation
```pip install -r requirements.txt```
## Setup Request
Put Initial coordinates in `init_coordinates`

Put New coordinates in `new_coordinates`

Coordinates Format: `distance(meters) horizontal_angel(rad) vertical_angel(rad)`

Example: 
```
6.58245 2.65978 0.206813
6.55242 2.66962 0.206813
...
3.58898 -0.988201 0.334841
3.53194 -0.978368 0.334841
```
## Run
First run flask server:

```flask --app main run```

Then execute distance endpoint:

```curl http://127.0.0.1:5000/get_distance```

Output example: `1.793046`

