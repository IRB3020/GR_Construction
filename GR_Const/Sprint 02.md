---
Title: Team Roles Contributions and Reflection
---
**Learnings**
	Initially, I attempted to add model classes first before groups. But I decided instead to start over and follow this guide: [(32) User Registration and Login Authentication | Django (3.0) Crash Course Tutorials (pt 14) - YouTube](https://www.youtube.com/watch?v=tUqUdu0Sjyc&list=PL-51WBLyFTg2vW-_6XBoUpE7vpmoR3ztO&index=16&ab_channel=DennisIvy)


**Sprint 02 Projects Requirements**
1. After pushing our changes, we create and switch to the branch for this sprint, "Sprint02". Due to some unrelated histories, PyCache files were forcefully merged but no errors were seen.
![[Pasted image 20240415115555.png]]
2. I re-edited my settings.py file to include a path for the login page.
![[Pasted image 20240415223428.png]]
3. I downloaded the registration.zip file provided in the slides and made corresponding paths for the login and register HTML files.
![[Pasted image 20240417110118.png]]
4. I created a group capable of manipulating the object I created.
![[Pasted image 20240416131745.png]]
5. I'm in the process of making said group's user's model class.
![[Pasted image 20240417105811.png]]
6. I make the newly created model in my website migrate.
![[Pasted image 20240416225446.png]]
7. I then create view function to handle login and register pages.
![[Pasted image 20240417105353.png]]
8. I then create a user form that will take in info to make a new user.
![[Pasted image 20240417105907.png]]
9. At this point, my register page is appearing properly but no  change occurs when a user is added. So I reedited views.py:
![[Pasted image 20240417191620.png]]
10. I reedited my navigational menu to include routes for the pages.
![[Pasted image 20240417191919.png]]
11. Clicking on "Register", we now create a Project Manager user.
![[Pasted image 20240417192157.png]]
12. After creation, we log into the system as the new user. Currently, there's no change to the website itself after login (returns home).
![[Pasted image 20240417190624.png]]
13. However, it's seen that two users are now active in the web.
![[Pasted image 20240417190950.png]]
14. By logging in as a new user, we're kicked out of the Admin Web.
![[Pasted image 20240417191034.png]]
15. Before deleting, we confirm that the user belonged to the group.
![[Pasted image 20240417191156.png]]
16. We will now start the process of sectioning of roles based off users that are logged in + the permissions set in their group.

