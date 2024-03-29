# Paul's Kitchen

## Introduction

Welcome to my project which is a website for a fictional restaurant called "Paul's Kitchen".

![](https://res.cloudinary.com/p-modaley/image/upload/v1643129983/paul_s_kitchen_end_product_dezz07.jpg)

A live version of the website can be found here: https://paulskitchen.herokuapp.com/

## [Table of Contents](#1-ux)

- 1. [UX](##1.UX)

  -  1.1. Strategy
     - Project Goals
       - User Stories
  -  1.2 Structure
  -  1.3 Skeleton
  -  1.4 Surface

- 2. [Features](##2. Features)

- 3. Technologies Used

- 4. Testing

- 5. Development Cycle

- 6. Deployment

- 7. End Product

- 8. Known Bugs

- 9. Credits



## 1.UX

[Back to top](#table-of-contents)

This website aims to enable people seeking information about Paul's Kitchen to view the menu, contact the restaurant, register with the restaurant, and make, edit and delete bookings. 

### 1.1 Strategy

[Back to top](#table-of-contents)

#### Project Goals

The goals of the website are to:

1) Enable customer to make, edit and delete bookings
2) Register their details with the restaurant by creating a profile and login credentials.
3) Enable an admin to manage bookings and customer details in the system
4) Showcase the restaurant's style and its menu

#### User Stories:

- As a **customer**, I can **make table booking** so that **I can reserve a table for a particular number of diners for a specified date and time.**
- As a **customer**, I can **register my details with the restaurant** so that **I can login and use my profile to make bookings.**
- As a **customer**, I can **manage bookings** so that **I can add or remove diners or change the date/time of my booking.**
- As a **customer**, I can **contact the restaurant** so that **I can provide the venue with additional information or make a query.*
- As an **administrator**, I can **manage customers' bookings** so that **I can add/remove diners and change the date/time of booking**
- As an **administrator**, I can **edit customer accounts** so that **I can update and/or delete customer details.**
- As a **customer**, I can **read an about the venue** so that **I can learn more about the restaurant's style and menu.**
- As a **customer**, I can **view the restaurant's menu** so that **I can consider what to order ahead of visiting the venue.**
- As a **customer*, I can **connect with the restaurant on social media** so that **I can suggest the venue to social media contacts and ask questions.**

#### Structure

The site will feature distinct pages, including home, menu, login, make a booking, and edit bookings. Users may navigate between the sections via the main navigation situated at the top of the page. 

- Responsive on all devices sizes.
- Navigation bar changes to a 'hamburger' style menu (top centre of screen) on smaller screens
- Footer at the bottom of the page links to social media pages.
- All elements will be comply with Paul's Kitchen's (fictional) branding, including colours, font size and typography.

#### Skeleton

I generated designs for the website using wireframes in Balsamiq. 

**Wire Frames**

![](https://res.cloudinary.com/p-modaley/image/upload/v1643128938/Paul_s_Kitchen_wireframe_jmf2up.png)

#### Surface

The colour schemes and typography used are consistent with my vision for the brand, Paul's Kitchen.

## 2. Features

[Back to top](#table-of-contents)

**Single page design:**

- Navigation bar will be placed at the top of the screen to enable easy access for the user. It collapses to a hamburger-style menu on smaller screens. As a sticky navigation bar, it will remain at the top of the screen as the user scrolls.
- The company logo will also feature at the top of the page.
- In the footer, users may access links to social media pages.

**Pages:**

The site design is comprised of several pages. Which of the sections are accessible via the navigation bar depends on whether or not the user is logged in. 

<u>Home</u>

The home page features images of the types of food served by the restaurant. 

<u>Menu</u>

A hamburger style menu is employed to facilitate browsing on various screen sizes. The hamburger icon expands or collapses when it is clicked.

<u>Login</u>

Here, users will be prompted to enter login in details or to register. If users are already logged in, a 'success' message will appear and the users' account information will be displayed on a profile page.

<u>Make A Booking</u>

Users can make bookings provided they are logged in to the site. To make a booking, users must supply their preferred date and time as well as the number of guests attending.

<u>Manage Booking</u>

Users wishing to amend or cancel their booking(s) can do so via the 'manage bookings' page by typing or clicking in the form fields and selecting the 'cancel' or 'edit' icon as desired.

### 3. Technologies Used

[Back to top](#table-of-contents)

The following is a non-exhaustive list of the technologies employed in the creation of the website:

- HTML5 
- Python
- Bootstrap
- CSS3
- JavaScript
- Chrome Developer Tools (for debugging and testing)
- [Balsamiq](https://balsamiq.com/wireframes/?gclid=CjwKCAjwt8uGBhBAEiwAayu_9Re_SESOK5WbZcH6AhP1IRIE_hxODw8EmSBYSkPiRQ41fvAERHT38hoCClQQAvD_BwE) (for developing wireframes during the initial design process)
- [Google Fonts](https://fonts.google.com/)
- [Font Awesome](https://fontawesome.com/)
- [GitHub](https://github.com/) (project repository)
- [GitPod](https://gitpod.io) (code line interface)
- [Typora](https://typora.io/) (for creating this readme file)
- [W3C Validator tools](https://validator.w3.org/) (for validating code and error checking)
- Heroku for app deployment
- Django for building the backend, including allauth for user authentication
- Postgresql for the database
- Cloudinary for media storage
- [Sweet Alert](https://sweetalert.js.org/) was used to display flash messages to the user to indicate successful actions.

### 4. Testing

[Back to top](#table-of-contents)

**Google Developer Tools**

During the process of coding the website, I used Google Developer Tools to view the affects of changes to the code. Occasionally, I would alter code within Google Developer Tools to observe changes before deciding whether or not to incorporate these changes within the code in GitPod. 

**Responsivity and Mobile-first Approach**

To ensure mobile responsivity, I made extensive use of Google Developer Tool's 'responsive' options, viewing my site on a range of devices, including iPhone 5/6/7/X. Bootstrap also contributed significantly to the website's mobile responsivity.

**Validator Tools**

Error identification and HTML validation was conducted using [W3C Markup](https://validator.w3.org/#validate_by_input+with_options) while [W3C CSS Validation](https://jigsaw.w3.org/css-validator/) enabled me to identify errors within my project's CSS. Python testing was conducted using [Pep8 Online](http://pep8online.com/).

#### **Testing Process**

The site was tested thoroughly for mobile and web responsivity and full CRUD functionality. Mainly, manual testing was employed. 

## 5. Development Cycle

[Back to top](#table-of-contents)

Having established a clear vision for the project as illustrated through wireframes, the development cycle was fairly linear without a great deal of deviation from the original plan. 

However, there were a few changes made during the development cycle which were not accounted for during the planning process.  The changes were made following discussions with other developers who offered constructive criticism of the site during its development. 

Throughout the project I used the GitHub projects as my project management tool which enabled me to create user stories and build website functionality according to these. Completed tasks (user stories) would be moved to 'done' once completed to a satisfactory standard.

## 6. Deployment

- Process for local deployment:

  1. Create a GitHub repository.
  2. Clone the repository on GitPod.
  3. Open the terminal within GitPod.
  4. Enter "python3 manage.py runserver into the terminal.
  5. Go to local host address in web browser.
  6. Check that changes are reflected in browser.

  Process for the final Heroku deployment:

  1. Uncomment the PostgreSQL databse from my settings.py file.
  2. Set debug = False in my settings.py file.
  3. Commit and push all files to GitHub
  4. In Heroku, remove the DISABLE_COLLECTSTATIC config var.
  5. In the deploy tab, go to the manual deploy sections and click deploy branch.

## 7. End Product

[Back to top](#table-of-contents)

![](https://res.cloudinary.com/p-modaley/image/upload/v1643129983/paul_s_kitchen_end_product_dezz07.jpg)

The site may be viewed via this link: https://paulskitchen.herokuapp.com/

## 8. Known Bugs

[Back to top](#table-of-contents)

- Minor styling issues, including image sizes and button alignment, on certain screen sizes. 

## 9. Credits

[Back to top](#table-of-contents)

#### Code

- The responsive navigation bar came from [W3 Schools](https://www.w3schools.com/howto/howto_js_topnav_responsive.asp)
- Fonts came from [Google Fonts](https://fonts.google.com/)
- Icons in the footer came from [https://fontawesome.com/](https://fontawesome.com/)
- Code for hover effect on demo button came from [W3 Schools](https://www.w3schools.com/howto/howto_css_zoom_hover.asp)

#### Content

- Images came from [Getty Images](gettyimages.co.uk) and W3Layouts