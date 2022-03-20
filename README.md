## Car Booking System: Customer Api
Flask Customer data  CRUD app for Car Booking system

# ERD for the Car Booking DB Design
including relationships, contraints, and data types

![ERD](https://user-images.githubusercontent.com/46499432/159168138-835d9b6b-2f0d-4255-bec5-ae4883ee83b5.png)
Full, executable SQL code included in repo root.

## Customer API Features
Fully integrated app with Flask backend connected to MySQL database, a simple Jinja powered frontend, and real-time JavaScript HTTP fetch calls for PUT and DELETE requests. Fetch api was used because HTML doeesn't support PUT and DELETE methods, and while it was possible to use GET/POST as alternatives, PUT and DELETE for updates and deletions are more architecturally sound and confroming to RESTFUL standards.

# Flask API endpoints:

- `/`: Main webapp Interface
- `/add`: to add new customers, with GET and POST routes for rendering interface and handling data.
- `/get`: customer query interface
- `/get/all`: list all customers' details on the database
- `/get/<id>`: get customer details by id
- `/update`: to update existing customer, with a GET route for input UI and a PUT route for hadling js fetch put reqeuests
- `/delete`: (GET) render deletion input interface, with real-time confirmation per request
- `/delete/<id>`: handles js fetch DELETE requests and perform deletions, rejects browser url GET requests
- 
# Front-end features:

- Simple interface that navigates the app, responds to erros, and fulfills all api needs

Main page:
![index](https://user-images.githubusercontent.com/46499432/159170022-806d4415-2427-4456-a5d8-c49a47abcc18.png)

Query page:
![get](https://user-images.githubusercontent.com/46499432/159170036-e6ea13e1-0cae-490f-921d-94eac45edaec.png)

Add customr:
![add](https://user-images.githubusercontent.com/46499432/159170088-eb5f0b95-814c-4d9f-b1a6-1ebcf46c8be5.png)

Update customer:
![update](https://user-images.githubusercontent.com/46499432/159170111-bd1075f2-3891-4312-9aa7-5ab98a45ae14.png)

Delete customer:
![delete](https://user-images.githubusercontent.com/46499432/159170176-b3c224e8-0415-47f1-bcd5-ffda8330e111.png)

Confirmation page for POST (add) reqeusts:
![success](https://user-images.githubusercontent.com/46499432/159170391-104c85c0-2d11-4a47-b999-3f2aa76da056.png)

Successful PUT/DELETE operations are confimed dinamically with a notifcation:
![delete-res](https://user-images.githubusercontent.com/46499432/159170236-936e4b47-1a4d-4e20-b8a0-db8d5f0606c1.png)

# USAGE

The app is fully functional. All that needs to be edited is the .yaml file for DB credentials and the SQL be code executed on an MySQL server.

