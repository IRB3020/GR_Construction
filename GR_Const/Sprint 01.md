---
Title: "Professional Communication: Learning and Reflection"
---
Initially, the project was initialized as a Git repository, where version control was used to manage changes to the project codebase throughout Sprint 01 development. Git, a widely used version control system, was employed.
1. We first prepare the existing website's directory to be added to Github. After pushing our changes into our local directory, we create and switch to the branch for this sprint, "Sprint01".
**![](https://lh7-us.googleusercontent.com/lp3rfkZPxB4M2uH5aXnmgGgqOksqh86tR1UlBkCwUhHZT0IF6zLOomnM5eQMtuzeq8EV6p-uggabrhDoqk-BAkfwfCm1chGAFjj8ky6-msSp6jivt3Dqkcp5KlaY-6Z72mE-yvbeDHuPqBIWvTHMV5M)**
2. We can now activate our virtual environment on a separate Windows PowerShell. Once activated, we create a new application inside the existing directory.
![[Pasted image 20240406111243.png]]
3. We open this section of the directory using PyCharm. We edit the "settings.py" file, allowing for authentication of users and allowed applications
**![](https://lh7-us.googleusercontent.com/i3Fa-6tElUoatoPEghTMwHkSVGATJDYYdmNiqmoFJm99EUULqY3XLpWG5UOfd7fq79-mE6aiunXx9Mc57AX8fap00yod1LngRB4M_7H8X5rXGC4mEZe1uyNSsqU1M78Obgr8XUDDFDwmDPGfrSnD0fc)**
4. We also update the "views.py" file by defining the following homepage view (notice the return statement; the rendering arguments will be explained later).
![[Pasted image 20240406115200.png]]
5. We also create a "urls.py" file and define a set path for the website's landing index or homepage (notice the other defined paths, which will be explained later).
![[Pasted image 20240406115001.png]]
6. Notice that a folder labeled "templates" exists within the existing directory. Inside this folder, we create a second folder titled after the existing directory, where we shall store a base_template.html.
![[Pasted image 20240406122845.png]]
7. Inside this same folder, we create and store an index.html.
![[Pasted image 20240406123143.png]]
8. Inside the virtual environment, we run our server, ignoring the migration warning.
9. We open , where the website's homepage may finally be viewed.
