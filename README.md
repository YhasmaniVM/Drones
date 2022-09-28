# Drones

```bash
How to Run:
 * python manage.py runserver  - Run django server.
 * python test_api.py          - Consume API test.
```
How api works?
***
* Method GET
***
$BASE_URL/drones/ --> Get the list of all Drones

$BASE_URL/drones/<:id> --> Check info for a given drone

$BASE_URL/drones/<:id>/medications --> Checking loaded medication items for a given drone

$BASE_URL/drones/<:id>/battery --> Check drone battery level for a given drone

$BASE_URL/drones/availables --> Check available drones for loading
***
* Method POST
***
$BASE_URL/drones/ --> registering a drone
***
* Method PUT
***
$BASE_URL/drones/<:id> --> Update a drone data
***
* Method DELETE
***
$BASE_URL/drones/<:id> --> Delete a drone
