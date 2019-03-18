# Flask-Vue-Docker

## Full-stack SPA:

* NGINX
* Gunicorn
* Vue
* Flask
* PostgreSQL
 
Must add a config.py file to the server directory.

Setup SQLAlchemy database URI and other Flask env's variables you want to in it.

There is no docker service to Postgres because I opted to use an RDS free tier database instance.

To execute the development env:

    docker-compose up

To execute the production env:

    docker-compose -f docker-compose.yml -f docker-compose.prod.yml up


## References:

  https://ldirer.com/deploy-docker-app/
  https://testdriven.io/blog/developing-a-single-page-app-with-flask-and-vuejs/
  https://medium.com/@matthew.rosendin/dockerizing-a-full-stack-application-89a7d69e11e9
