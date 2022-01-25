# Paul's Kitchen

## Introduction

Welcome to my project which is a website for a fictional restaurant called "Paul's Kitchen".

A live version of the website can be found here: https://paulskitchen.herokuapp.com/

## [Table of Contents](#1-ux)

- 1. [UX](##1.UX)

  - ​	1.1. Strategy
    - Project Goals
      - User Stories
  - 1.2 Structure
  - 1.3 Skeleton
  - 1.4 Surface

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

https://share.balsamiq.com/c/4NTKVmHWXeuBzJobAdpYLR.png

https://res.cloudinary.com/p-modaley/image/upload/v1643128938/Paul_s_Kitchen_wireframe_jmf2up.png

#### Surface

The colour schemes and typography used are consistent with my vision for the brand, Paul's Kitchen.

## 2. Features

[Back to top](#table-of-contents)

**Single page design:**

- Navigation bar will be placed at the top of the screen to enable easy access for the user. It collapses to a hamburger-style menu on smaller screens. As a sticky navigation bar, it will remain at the top of the screen as the user scrolls.
- The company logo will also feature at the top of the page.
- In the footer, users may access links to social media pages.

**Sections:**

The site design is comprised of several pages. Which of the sections are accessible via the navigation bar depends on whether or not the user is logged in. 

<u>Home</u>

This first section includes introductory text position to the right of a hero image situated in an angled div to add visual appeal to the page. This section is separated from the remained of the page by a div featuring the text, 'RXM Enables Brands To...' 

<u>Menu</u>

In the 'Get Found' section, users will be able to read about the importance of improving visibility online and how to make themselves more attractive to potential customers. 

There will be a video in this section that users can watch entitled, 'Introduction to Customer Reviews and Star Ratings'.

A 'back to the top' link will enable the user to return to the top navigation menu.

<u>Login</u>

Distinguished from the previous section by its light grey background colour, 'Get Chosen' explains to users how customers choose businesses online.

A bar graph illustrates influences on the customer purchase decision. Such data provided in a visual way is appealing to Reputation customers.

<u>Make A Booking</u>

A darker grey background distinguishes this section from 'Get Chosen'. Here, the user can read about how customer feedback can enable businesses to enhance the customer experience. 

Also, the '3Cs for the Optimal Customer Experience' will feature toward the bottom of this section in 3 darker coloured boxes which enhance the visual appeal of the page.

<u>Manage Booking</u>

In this section, users may view a video explaining the capabilities of the the Reputation platform. At the bottom of the section, there is a form which users may complete to signal their interest in receiving a demo of the platform.

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

### 4. Testing

[Back to top](#table-of-contents)

**Google Developer Tools**

During the process of coding the website, I used Google Developer Tools to view the affects of changes to the code. Occasionally, I would alter code within Google Developer Tools to observe changes before deciding whether or not to incorporate these changes within the code in GitPod. 

**Responsivity and Mobile-first Approach**

To ensure mobile responsivity, I made extensive use of Google Developer Tool's 'responsive' options, viewing my site on a range of devices, including iPhone 5/6/7/X. Bootstrap also contributed significantly to the website's mobile responsivity.

**Validator Tools**

Error identification and HTML validation was conducted using [W3C Markup](https://validator.w3.org/#validate_by_input+with_options) while [W3C CSS Validation](https://jigsaw.w3.org/css-validator/) enabled me to identify errors within my project's CSS.

#### **Testing Process**

The site was tested thoroughly for mobile and web responsivity and full CRUD functionality. Mainly, manual testing was employed. 

## 5. Development Cycle

[Back to top](#table-of-contents)

Having established a clear vision for the project as illustrated through wireframes, the development cycle was fairly linear without a great deal of deviation from the original plan. 

However, there were a few changes made during the development cycle which were not accounted for during the planning process.  The changes were made following discussions with other developers who offered constructive criticism of the site during its development. 

#### Form

- A form was added to replace the 'Get a Demo Button'
- The form presents one major advantage over the 'Get a Demo' button - it reduces the number of clicks needed before the user can access the form and avoids the need for opening new tabs.

#### Navigation

- Following discussion with my mentor, I implemented a sticky navigation to enhance the user experience.

#### Shadows

- To enhance the visual appearance, I added a box shadow effect at the bar graphs and boxes including the form.

## 6. Deployment

I deployed my project through GitHub. The process was as follows:

- From my repository, select 'Settings'.
- Select pages.
- Select 'Branch: master' under the 'Source' heading
- Select publish

## 7. End Product

[Back to top](#table-of-contents)

![image-20220125165633145](C:\Users\Paul Modaley\AppData\Roaming\Typora\typora-user-images\image-20220125165633145.png)

The site may be viewed via this link: https://paulskitchen.herokuapp.com/

## 8. Known Bugs

[Back to top](#table-of-contents)

- On desktop view in particular, the YouTube videos appear somewhat larger than would be ideal.
- Form inputs were not aligned. This has been remedied by adding a width of 100px to the CSS input 'label'.

## 9. Credits

[Back to top](#table-of-contents)

#### Code

- The angled div came from [Suman Biswas at Codepen](https://codepen.io/biswassuman/pen/NWGqKwd)
- The transparent text box over the hero image in mobile view came from [Rob Doyle Creative](https://robdoylecreative.com/how-to-add-a-transparent-text-box-over-an-image-using-css/)
- The bar graph in the 'Get Chosen' section came from [W3 Schools](https://www.w3schools.com/howto/howto_css_skill_bar.asp)
- The responsive navigation bar came from [W3 Schools](https://www.w3schools.com/howto/howto_js_topnav_responsive.asp)
- The responsive iframes came from [W3 Schools](https://www.w3schools.com/howto/howto_css_responsive_iframes.asp)
- Fonts came from [Google Fonts](https://fonts.google.com/)
- Icons in the footer came from [https://fontawesome.com/](https://fontawesome.com/)
- Code for hover effect on demo button came from [W3 Schools](https://www.w3schools.com/howto/howto_css_zoom_hover.asp)

#### Content

- Text content and statistics came from Reputation's ['RXM Guide: What is Reputation Experience Management?'](https://go.reputation.com/hubfs/Downloadable%20Assets/2020%20RXM%20Guide%20EN.pdf)
- Images came from [Getty Images](gettyimages.co.uk)
- Videos came from [Reputation's YouTube channel](https://www.youtube.com/channel/UCzgjQHzKoKoCHAXhRB45pfg)
- Logo image came from Reputation
- Branding and colour scheme came from Reputation



