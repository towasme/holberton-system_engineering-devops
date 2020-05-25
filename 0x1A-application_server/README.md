## Application server
---

### Description
---


    A README.md file, at the root of the folder of the project, is mandatory
    Everything Python-related must be done using python3
    All config files must have comments

### Task
Name|Task
---|---
 0. Set up development with Python | Let’s serve what you built for AirBnB clone v2 - Web framework on web-01. This task is an exercise in setting up your development environment, which is used for testing and debugging your code before deploying it to production.
 1. Set up production with Gunicorn | Now that you have your development environment set up, let’s get your production application server set up with Gunicorn on web-01, port 5000. You’ll need to install Gunicorn and any libraries required by your application. Your Flask application object will serve as a WSGI entry point into your application. This will be your production environment. As you can see we want the production and development of your application to use the same port, so the conditions for serving your dynamic content are the same in both environments.
 2. Serve a page with Nginx | Building on your work in the previous tasks, configure Nginx to serve your page from the route /airbnb-onepage/
 3. Add a route with query parameters | Building on what you did in the previous tasks, let’s expand our web application by adding another service for Gunicorn to handle.
 4. Let's do this for your API | Let’s serve what you built for AirBnB clone v3 - RESTful API on web-01.
 5. Serve your AirBnB clone | Let’s serve what you built for AirBnB clone - Web dynamic on web-01.
