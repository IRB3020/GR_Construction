---
Title: "Professional Communication: Learning and Reflection"
---
**Learnings**
	Initially, the project was initialized as a Git repository, where version control was used to manage changes to the project codebase throughout Sprint 01 development. Git, a widely used version control system, was employed. Commits were made to track changes made to the codebase. Each commit had a meaningful commit message describing the changes made.
	![[Pasted image 20240406125410.png]]When implementing functionality for a user to create an item (aka a client), a view function was create to handle the HTTP POST request sent by the user when submitting the item creation form. Within this view function, a form instance was created from the Django Form class corresponding to the item creation form. The form's "is_valid()" method was used to check whether the submitted data was valid. If so, the form's "save()" method was called to create a new item instance with the validated data. After a successful creation, the user is redirected to a success page where they can return to the page where the item creation form is located.
	![[Pasted image 20240406205242.png]]
	Similarly, a view function was created to retrieve a list of items from the database using a Django ORM query. The retrieved list of items was passed to a template for rendering. In the template, HTML markup was used along the template tags and filters provided by Django to iterate over the list of items and display them correctly.
	![[Pasted image 20240406131738.png]]
	Bootstrap's predefined CSS classes and components were utilized to implement a responsive navigation menu. The "Navbar" component provided by Bootstrap was employed to create a two-option navigation bar. As seen below, Bootstrap classes were used to structure the navigation bar and make it responsive.
	![[Pasted image 20240406132342.png]]
	By applying these classes and components, the navigation menu was styled and made compatible with different screen sizes, ensuring a consistent experience across devices.
	![[Pasted image 20240406143925.png]]


**Sprint 01 Project Requirements**
1. We first prepare the existing website's directory to be added to Github. After pushing our changes into our local directory, we create and switch to the branch for this sprint, "Sprint01".
**![](https://lh7-us.googleusercontent.com/lp3rfkZPxB4M2uH5aXnmgGgqOksqh86tR1UlBkCwUhHZT0IF6zLOomnM5eQMtuzeq8EV6p-uggabrhDoqk-BAkfwfCm1chGAFjj8ky6-msSp6jivt3Dqkcp5KlaY-6Z72mE-yvbeDHuPqBIWvTHMV5M)**
2. We can now activate our virtual environment on a separate Windows PowerShell. Once activated, we create a new application inside the existing directory.
![[Pasted image 20240406111243.png]]
3. We open this section of the directory using PyCharm. We edit the "settings.py" file, allowing for authentication of users and allowed applications
**![](https://lh7-us.googleusercontent.com/i3Fa-6tElUoatoPEghTMwHkSVGATJDYYdmNiqmoFJm99EUULqY3XLpWG5UOfd7fq79-mE6aiunXx9Mc57AX8fap00yod1LngRB4M_7H8X5rXGC4mEZe1uyNSsqU1M78Obgr8XUDDFDwmDPGfrSnD0fc)**
4. We also update the "views.py" file by defining the following homepage view (notice the return statement; the rendering arguments will be explained later).
![[Pasted image 20240406115200.png]]
5. We also create a "urls.py" file and define a set path for the website's landing index or homepage (notice the other defined paths, which will be implemented later).
![[Pasted image 20240406205516.png]]
6. Notice that a folder labeled "templates" exists within the existing directory. Inside this folder, within a second folder titled after the existing directory, we shall create and store a base_template.html file.
![[Pasted image 20240406122845.png]]
7. Inside this same folder, we create and store an index.html file.
![[Pasted image 20240406123143.png]]
8. Inside the virtual environment, we run our server, ignoring the migration warning.
![[Pasted image 20240406132605.png]]
9. We open http://localhost:8000/, where the website's homepage may finally be viewed. The snapshot below demonstrates the state of the homepage *before* styling options and static images are implemented, steps which will be seen later.
![[Pasted image 20240406132832.png]]
10. We add the following styling options within the index.html, enhancing the overall user experience and fulfilling the project holder's requests for aesthetic and appearance.
```
<style>  
    body {  
        background-color: #ede3d8;  
        color: #333;  
        font-family: Arial, sans-serif;  
    }  
    .main-header {  
        background-color: #7172d8; /* Main banner color */  
        color: #fff; /* White text */  
        padding: 20px;  
        text-align: center;  
        border-bottom: 5px solid #f0b356; /* Secondary banner color */  
    }  
    .main-header h1 {  
        margin: 0;  
    }  
    .container {  
        max-width: 800px;  
        margin: 20px auto;  
        padding: 20px;  
        background-color: #fff;  
        border-radius: 10px;  
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);  
    }  
    .portfolio-container {  
        margin-bottom: 20px;  
        padding: 10px;  
        border: 1px solid #ccc;  
        border-radius: 5px;  
    }  
    .portfolio-container h2 {  
        color: #7172d8; /* Secondary banner color */  
    }  
    .portfolio-container p {  
        color: #666;  
    }  
    .btn {  
        display: inline-block;  
        background-color: #7172d8; /* Secondary banner color */  
        color: #fff;  
        padding: 10px 20px;  
        border: none;  
        border-radius: 5px;  
        cursor: pointer;  
        text-decoration: none;  
    }  
    .btn:hover {  
        background-color: #f0b356; /* Hover color */  
    }  
</style>
```
11. Inside the existing directory, we create a folder labeled "static", in which a folder labeled "images" will be stored. Here, we add a logo for the company's website.
![[Pasted image 20240406141516.png]]
12. After updating the settings.py file to tell Django where to find said folder, we check-in with the project holder, who sends over the images they wish the website to display. To accommodate edit the base_template.html to both display the contents of the "static/images" file but also allow the user to return to the homepage if desired.
![[Pasted image 20240406143518.png]]
13. Finally, we reload the website to see the newly added logos as well as the stylistic options integrated earlier, per the project holder's request.
![[Pasted image 20240406144437.png]]
14. We create a SuperUser and login to the Admin Panel, out of standard's sake and to test creating a Client model (Jane Doe) through the Django admin application.
**![](https://lh7-us.googleusercontent.com/gmquqyF4G6dyygN6TCWUV8_ifjR_jbsbce025azUWG7dugfVi6E4OH3qrFdZVg7K3HU1T_p3YBMZk-HZl1a4WRZGlu76I491RiIGGt3YMBY66b8NnQQAbY7PjVEqm_r2HyG80oCu7wErEwpHxbrnIpo)**
15. We create a Client Model in the existing directory by adding the structure to the models.py after registering the table into the admin.py file. Notice the attributes correlating to the model, including the required "status" attribute. 
**![](https://lh7-us.googleusercontent.com/6gH4q31BMsCt6-nxmZDXyZDLdB75FqfvYctyyi3k3hJtkZQhOoaffeN8Dv_o9IKvdISqDIHHpkzGUg0eoF1GRyWdYVF9g6vaD-_6wsQoilCwtPb1NG8SYy8v63NHkK2OZeKloU4v05aXwdujo1gvlVE)**
16. We perform migrations in Django to add the class model to the database.
**![](https://lh7-us.googleusercontent.com/l-hcUtBbsUF7Ag1OeexCvABua8RiXZ_ODFxm4N_LOd3zqHLgrlVK5RV1kvpUn265dAPKInYa9sMcpjYQFI-2xfJAQlIp91SMxynxUL4SKfGOOrBWyeos5_m-Z7zkQVqCltEHqL7jiDgQJoRz77y5unA)**
17. We now compile the following code into a client_detail.html file that will create a webpage displaying the details of a specified client from a list.
```
{% extends "gr_construction_web/base_template.html" %}  
  
{% block content %}  
  
<!doctype html>  
<html lang="en">  
<head>  
    <meta charset="utf-8">  
    <meta name="viewport" content="width=device-width, initial-scale=1">  
    <title>Client Detail</title>  
</head>  
<body>  
    <div class="container">  
        <h2>Client Detail</h2>  
        <p>Name: {{ client.name }}</p>  
        <p>Status: {{ client.status }}</p>  
        <p>Email: {{ client.email }}</p>  
        <p>Phone Number: {{ client.phone_number }}</p>  
        <p>Description: {{ client.description }}</p>  
        <a href="{% url 'clients-list' %}">Back to Clients List</a>  
    </div></body>  
</html>  
  
{% endblock %}
```
18. We also compile the following code into a clients_list.html file that will create a webpage displaying a list of all clients currently in the database.
```
{% extends "gr_construction_web/base_template.html" %}  
  
{% block content %}  
  
<!doctype html>  
<html lang="en">  
<head>  
    <meta charset="utf-8">  
    <meta name="viewport" content="width=device-width, initial-scale=1">  
    <title>Clients List</title>  
</head>  
<body>  
    <div class="container">  
        <h2>Clients List</h2>  
        <ul>            {% for client in clients %}  
                <li>{{ client.name }} - <a href="{% url 'client-detail' client.id %}">View</a>  
                    | <a href="{% url 'client-edit' client.id %}">Edit</a>  
                    | <a href="{% url 'client-delete' client.id %}">Delete</a></li>  
            {% endfor %}  
        </ul>  
        <a href="{% url 'add-client' %}">Create New Client</a>  
    </div></body>  
</html>  
  
{% endblock %}
```
19. It's important this list is accessible through the navigational bar implemented into the base_template.html. This list will allow users to view, edit, and delete existing clients.
![[Pasted image 20240406164445.png]]
20. The client_list.html requires a client_edit.html file to exist, which directs the user to a webpage where they may edit the details of an existing client.
![[Pasted image 20240406171919.png]]
21. The client_list.html also requires a client_delete.html file, which will verify the user's intent of removing the specified Client Model from the existing database.
![[Pasted image 20240406172059.png]]
22. We will now implement code that allows a user to create a Client Model within the existing website. This code will go into an add_client.html file.
```
{% load static %}  
  
  
<!DOCTYPE html>  
<html>  
<head>  
    <title>Add Client</title>  
    <!-- Bootstrap CSS link -->  
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet">  
</head>  
<body>  
<a class="navbar-brand" href="{% url 'index' %}">  
                <img src="{% static 'images/Main Logo.jpg' %}" alt="Main Logo">  
            </a><div class="container">  
    <h2>Add Client</h2>  
    <form method="post">  
        {% csrf_token %}  
        {{ form.as_p }}  
        <button type="submit" class="btn btn-primary">Submit</button>  
    </form></div>  
  
</body>  
</html>
```
22. Clicking on "Create New Client" will now allow the user to add new Client Models.
![[Pasted image 20240406172510.png]]
23. Once the model is successfully created, the project holder requested a success page, where the newly created model's details will be displayed to the user.
![[Pasted image 20240406172735.png]]
24. The user may now view their Client Models once redirected. The user may also now remove any existing models from the database after verifying their intent.
![[Pasted image 20240406172930.png]]
25. A demonstration of the website's capabilities may be found here:
	**[https://uccs1.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=68154755-cc62-42f2-bce5-b14a018521ea&start=0](https://uccs1.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=68154755-cc62-42f2-bce5-b14a018521ea&start=0)**
26. Update the main branch by merging it with the sprint01 branch code, making sure to tag the code as "Sprint 01". Do not delete the branch.


**Reflection**
	Reflecting on the sprint and full stack development utilizing agile methodologies, I found that breaking user stories into tasks was highly beneficial as it allowed for a clearer understanding of what needed to be done and facilitated better planning and time management. However, I noticed that sometimes tasks required more time than initially estimated, which highlights the importance of being flexible and adaptable in agile development. Other tasks took less time than estimated, mainly due to the prior documentation assembled throughout the course. While the estimates provided a rough guideline, utilizing version control, particularly Git, was instrumental in managing code changes as it provided a structured way to track modifications, revert changes if necessary, and ensure that I was working on the latest version of the codebase. This helped maintain code integrity and streamline the development process, enhancing overall productivity.
	One of my biggest successes during this sprint was successfully implementing key features of the project according to the user stories and design specifications. Additionally, creating a useful and easily referrable UML Diagram for the Client Model aided in it's implementation and later migration into the database.
	![[IMG_3269.jpg]]
	The most challenging aspect of the sprint was troubleshooting unexpected bugs or technical issues that arose during the development of deployment of lists and navigational bars with view, create, edit, or delete options. However, leveraging my previous online documentation and community resources proved invaluable in finding solutions and resolving these challenges efficiently. My biggest strength as a software developer lies in my problem-solving skills and ability to adapt to new technologies and frameworks. This allows me to overcome obstacles and deliver high-quality solutions within a set timeframe.
