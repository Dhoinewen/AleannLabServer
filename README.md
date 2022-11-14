# Test Task
## For setting up project: 
1. Clone the repository
2. Create your own virtual environment
3. Install requirements
4. Set up MySQL database
5. Make your migrations
6. Create a new superuser
7. python manage.py runserver

## Routers
1.  http://localhost:8000/api/v1/users/ - get all users
2.  http://localhost:8000/api/v1/ranks/ - get all ranks
3.  http://localhost:8000/api/v1/users/x - get solo user (where x is user Id)
4. http://localhost:8000/api/v1/ranks/x - get solo rank
5.  http://localhost:8000/doctors/?sort_rank=x - sort by rank queue (desc, asc or none)
