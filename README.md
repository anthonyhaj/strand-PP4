# Strand Restaurant and Bar

![Am I Responsive](docs/am-i-responsive.png)

**Developer: Anthony Haj Ibrahim**

[Visit live website](https://strand-pp4-d640c87ff185.herokuapp.com/)  

## Table of Contents
  - [About](#about)
  - [User Goals](#user-goals)
  - [Site Owner Goals](#site-owner-goals)
  - [User Stories](#user-stories)
  - [Design](#design)
    - [Colours](#colours)
    - [Fonts](#fonts)
    - [Structure](#structure)
      - [Website pages](#website-pages)
      - [Database](#database)
  - [Technologies Used](#technologies-used)
  - [Features](#features)
  - [Validation](#validation)
  - [Testing](#testing)
    - [Manual testing](#manual-testing)
    - [Tests on various devices](#tests-on-various-devices)
    - [Browser compatibility](#browser-compatibility)
  - [Bugs](#bugs)
  - [Heroku Deployment](#heroku-deployment)
  - [Credits](#credits)
  - [Acknowledgements](#acknowledgements)


## About 

Strand Restaurant and bar is a business where users can book a table, 
create an account, see the menu, or contact the business.

### User Goals

- To be able to view the business menu
- To be able to create an account
- To be able to book a table
- To be able to edit or cancel bookings
- To be able to contact the business 
- To be able to find the business

### Site-owner goals

- To provide a well organized and responsive site
- To have 

## User Stories

### Users

1. As a **User** I can **use the navbar, footer, and social icons** so that I can **navigate the business site**
2. As a **User**, I want to **be able to contact the business using a form** so that **the business can see my contact information and message**
3. As a **User**, I want to see the **restaurant's opening hours and location** so that I can **plan my visit.**
4. As a **user**, I want to see the **menu page** so that **I can explore the dishes offered by the restaurant**
5. As a **user**, I want to **create an account** so that **I can make a booking.**
6. As a **user**, I want to **log in to my account** to **manage my bookings and personal details.**
7. As a **user**, I want to **see my login status (logged in or logged out) and who I am logged in as (username or email) displayed on the website**, so I can **easily understand my current session status**
8. As a **User**, I want to **book a table** so that **I can ensure I have a place at a convenient time.**
9. As a **User**, I cannot **choose a past date while booking** so that **a booking is on a valid date**
10. As a **User**, I am **notified** so that **I know my booking has been booked successfully**
11. As a **user**, I want to **be able to view a booking I have already made** so that **I can see my booking information**
12. As a **user**, I want to **modify my booking details (like time, date, or number of guests)** so that I can **change my plans if needed.**
13. As a **User**, I am **notified when changing my booking information** so that **I know it has been changed successfully**
14. As a **User**, I want to **be able to cancel a booking that I have made**
15. As a **user**, I want **know if I have successfully logged out of my account** 

### Admin

16. As an **Admin**, I want to **be able to log in to the admin interface** so that **I can interact with my app data.**
17. As a **Admin**, I want to **confirm or reject online booking requests** so that **I can manage the restaurant's seating capacity.**
18. As an **Admin**, I want to be able to **create, update, read, and delete** the menu items so that **customers can see current menu and prices**
19. As a **Admin**, I want to **see when a user has submited a contact form with user information and message** so that **I can contact the user**

### Site Owner
20. As a **Site Owner**, I can **ensure that my site is fully responsive** so that **it can be used across all devices**
21. As a **Site Owner**, I can **ensure that my site has data validation** so that **all submitted data is validated to avoid errors**

### Epics and Github Projects
- Github projects was used to track and create user stories
- Epics were created using milestones

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

## Design

### Colors

- The colors I chose consist of dark grays and gold keeping the colors balanced and contrasted well
as a dark theme

<details><summary>See color pallet</summary>
<img src="docs/palette.png">
</details>

### Fonts

- The fonts used were the default Montserrat and sans-serif

## Structure

The site was structured using a basic logo and navigation layout showing all relevant links
and hamburger menu for smaller devices. The footer consists of 3 social media links

### Pages
- Home page with a welcome message, carousel of restaurant images, how to find us section
and contact information/opening hours
- Menu page with all food and drink items shown in cards and sorted by type retrieved from
the database
- Book a Table page where logged in user can fill a form for booking a table at the restaurant
and if a user is not logged in then login_required page will ask user to log in to book
- My bookings page displays all current users bookings and allows user to change or 
cancel a booking they have made
- Change booking page shows a form in which allows the user can change their booking information
- Cancel booking page allows a user to delete a booking they have made and also from the database
- Contact Us page allows a user to submit a contact form with a message with a where to find us and 
contact information/opening hours below the form
- Register page allows the user to register for an account in order to book a table
- Log In page allows user to log into their account to interact with bookings

### Database
- Built with Python and Django with a Postgres database
- Database schema created using dbdiagram.io

<details><summary>See diagram</summary>
<img src="docs/db-schema.png">
</details>

#### User Model

The User Model contains:

- user_id
- password
- last_login
- is_superuser
- username
- first_name
- last_name
- email
- is_staff
- is_active
- date_joined

#### FoodItem Model

The FoodItem Model contains

- id 
- food_name
- description
- type
- price

#### DrinkItem Model

The DrinkItem Model contains:

- id 
- food_name
- description
- type
- price

#### Booking Model

The Booking Model contains:

- booking_id (PK)
- created_date
- requested_date
- requested_time
- table (FK)
- guest (FK)
- seats
- guest_count

#### Table Model

The Table Model contains:

- id (PK)
- table_name
- max_seats
- available

#### Contact Model 

The Contact Model contains:

- id (PK)
- name (FK)
- email (FK)
- phone (FK)
- message

## Technologies Used 

### Languages & Frameworks

- HTML
- CSS
- Javascript
- Python
- Django

### Libraries & Tools

- Am I Responsive
- Bootstrap 5
- Font Awesome
- Chrome dev tools
- Pexels.com
- Cloudinary
- Pycharm
- Git
- GitHub
- Heroku 
- jQuery
- Postgres