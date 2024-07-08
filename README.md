# TechGiants

The Tech Giants website is an online shop specializing in the latest smartphones and laptops. It offers a range of products from top brands like Apple, Samsung, and Google, with special discounts and promotions. The site features categories for phones and laptops, a section for featured products, and options to sign up for a newsletter for updates on new collections and articles. The website also provides contact information and support for users.

## Table of Contents
1. [Introduction](#1-introduction)
2. [User Experience](#2-user-experience)
   - [Strategy](#21-strategy)
     - [Target Users](#target-users)
     - [What the User Would Look For](#what-the-user-would-look-for)
     - [User Stories](#user-stories)
   - [Scope](#22-scope)
     - [Sprint 1](#sprint-1)
     - [Sprint 2](#sprint-2)
     - [Future Sprints](#future-sprints)
   - [Structure](#23-structure)
3. [Project Applications](#3-project-applications)
4. [Project Databases](#4-project-databases)
   - [Post Model](#post-model)
   - [Upload](#upload)
5. [Skeleton](#5-skeleton)
   - [Wireframes](#wireframes)
6. [Features](#6-features)
   - [Existing Features](#existing-features)
     - [Home](#home)
     - [Profile page](#profile-page)
     - [Upload page](#upload-page)
     - [Search](#search)
     - [Nav bar](#nav-bar)
     - [Post detail](#post-detail)
     - [Comments](#comments)
     - [Delete / Edit comments](#delete--edit-comments)
7. [Technologies Used](#7-technologies-used)
   - [Languages](#languages)
   - [Tools](#tools)
   - [Styling](#styling)
8. [Validation](#8-validation)
   - [Code Validation](#code-validation)
   - [Responsiveness](#responsiveness)
9. [Bugs](#9-bugs)
10. [Deployment](#10-deployment)
   - [Create Application](#create-application)
   - [Final Repo Preparations](#final-repo-preparations)
11. [Credits](#11-credits)

---
## 1. Introduction
The Django E-Commerce project is an advanced online platform designed for purchasing laptops and phones. It offers a robust e-commerce experience where users can browse products, securely place orders using Stripe, and provide feedback through product reviews.

![Screenshot 2024-07-08 064513](https://github.com/IsaLubs/TechGiants/assets/147058041/4f1fab35-2db3-4e6d-abcd-f7a1405e0c43)



## 2. User Experience

### 2.1 Strategy

#### Target Users
The primary target audience includes tech-savvy individuals aged 18 and older who prefer the convenience of online shopping for electronics.

#### What the User Would Look For
Users seek a seamless shopping experience with a diverse product catalog, intuitive navigation, secure payment options, and the ability to share product experiences through reviews.

#### User Stories
- As a user, I want to explore a variety of laptops and phones to make informed purchase decisions.
- As a user, I want a straightforward sign-in process to access personalized features and complete purchases securely.
- As a user, I want to checkout quickly and securely using Stripe to finalize my purchase.
- As a user, I want to leave detailed reviews to help other shoppers make informed decisions.

### 2.2 Scope

#### Sprint 1
Implemented essential functionalities including the homepage, navigation bar, user registration and login, and detailed product pages.

#### Sprint 2
Enhanced user experience with a streamlined checkout process, a responsive shopping cart, and comprehensive order details display.

#### Future Sprints
Planned expansions include enabling new sellers to list their products for sale, fostering a dynamic marketplace environment.

### 2.3 Structure
The project is meticulously structured to ensure efficient development and user engagement. Applications are modularized to handle distinct tasks, while databases are optimized for scalability and data integrity.

---

## 3. Project Applications.
- **User Authentication**: Secure authentication system for user management.
- **Product Catalog**: Comprehensive catalog of laptops and phones.
- **Shopping Cart**: Interactive cart management for seamless shopping experiences.
- **Checkout**: Secure payment gateway integration with Stripe for hassle-free transactions.

---

## 4. Project Databases

5 databases can be found in the “brush_app” application, which enable the user to create the profile required to upload posts. I created a database in the begining to support the functionality created by my user stories. The first sql map is included here and was an over zealous approach to my goal. Through timing and scope my databases changed and morphed over the duration of creating it. The most up to date map is shown as well.

![output (1)](https://github.com/IsaLubs/TechGiants/assets/147058041/f0f42fba-ab04-41b9-9eb7-0bb997650fe8)


### Post Model
Captures user-generated content including product titles, user-friendly URLs (slugs), author details, product descriptions, uploaded images, and user reviews for products.

### Upload
Manages uploaded product details such as titles, descriptions, images, and pricing information.

---
## 5. Skeleton

### Wireframes

#### Home Page

![Screenshot 2024-07-07 003942](https://github.com/IsaLubs/TechGiants/assets/147058041/ccc08712-f6b6-44da-9a7c-cc5e574b26a1)

![Screenshot 2024-07-07 004000](https://github.com/IsaLubs/TechGiants/assets/147058041/719135d1-4178-415b-9bb7-485364a7e8aa)

![Screenshot 2024-07-07 004031](https://github.com/IsaLubs/TechGiants/assets/147058041/505ce62a-aef4-4bd5-a6c5-eb6289e477ef)

#### Product Page

![Screenshot 2024-07-07 004059](https://github.com/IsaLubs/TechGiants/assets/147058041/c0480235-d27b-4ff2-adb6-f046741711a9)

#### SignIn Page

![Screenshot 2024-07-07 004226](https://github.com/IsaLubs/TechGiants/assets/147058041/98d412e0-2b44-4ed0-a3f0-9aa8bc0c55b1)

#### SignUp Page

![Screenshot 2024-07-07 004238](https://github.com/IsaLubs/TechGiants/assets/147058041/91e2890b-abe3-4442-9390-913e663595e1)

#### ContactUs Page  

![Screenshot 2024-07-07 004157](https://github.com/IsaLubs/TechGiants/assets/147058041/2b7b9cef-05ec-4f18-bd48-8e94659d5a32)

---
## 6. Features

### Existing Features

#### Home
- Presents a visually appealing and informative landing page showcasing featured products and promotional offers.

#### Profile page
- Allows users to manage personal information, view order history, and update preferences.

#### Upload page
- Enables sellers to upload product details, including images and descriptions, to list items for sale.

#### Search
- Facilitates easy navigation through a robust search functionality that retrieves relevant products based on user queries.

#### Nav bar
- Provides intuitive navigation with a responsive navbar that adapts seamlessly across different device sizes.
![Screenshot 2024-07-08 081712](https://github.com/IsaLubs/TechGiants/assets/147058041/6a05000d-1ccf-4b66-a6d1-ee63294cb215)

#### Post detail
- Displays comprehensive product details including specifications, pricing, and customer reviews for informed purchasing decisions.

#### Comments
- Enables users to leave feedback and engage in discussions about products through interactive commenting features.

#### Delete / Edit comments
- Allows users to manage their reviews by editing or removing.
![Screenshot 2024-07-08 063659](https://github.com/IsaLubs/TechGiants/assets/147058041/0347440f-2c71-46db-9984-90adbe35df7f)


---
## 7. Technologies Used

### Languages
- **HTML**: Used for creating structured Django templates.
- **CSS**: Stylesheets for customizing the website's visual presentation.
- **JavaScript**: Enhances interactivity and dynamic content on the frontend.
- **Python**: Primary language for backend development using Django's framework.

### Tools
- **Django**: Framework for rapid development and robust web application management.
- **Crispy Forms**: Integrates forms seamlessly into Django templates for improved user interaction.
- **GitHub**: Version control and collaborative development platform.
- **Illustrator**: Used for creating detailed wireframes and visual assets.

### Styling
- **Bootstrap**: Provides pre-built components and responsive layout utilities for frontend design.
- **Google Fonts**: Adds visually appealing typography options to enhance readability and aesthetics.

---
## 8. Validation

### Code Validation

#### W3C CSS Validator
- My css passed as well when it came to testing as I was frequently testing it in the validator.

![Screenshot 2024-07-06 222140](https://github.com/IsaLubs/TechGiants/assets/147058041/ba3557dd-fd8b-43af-b0d5-6a7baa34e224)

![Screenshot 2024-07-06 222208](https://github.com/IsaLubs/TechGiants/assets/147058041/28df3540-f107-4abe-93b6-4cc97985fd95)

![Screenshot 2024-07-06 222237](https://github.com/IsaLubs/TechGiants/assets/147058041/434bebc6-a146-4ca8-89b4-88def80e27b0)

#### CI Python checker
- I checked all of my python files with the Code Institute python checker and recieved no issues with any of the files.

![Screenshot 2024-07-06 223131](https://github.com/IsaLubs/TechGiants/assets/147058041/ede41c3b-e876-4d7d-897b-af125bb0373e)

### Responsiveness

The responsiveness of the design was manually checked using the Chrome Developer Tools for various screens.

This included:

- iPhone SE
- Pixel 5
- Samsung Galaxy S8, S20 Ultra
- iPad Air and Mini
- Galaxy Fold
- Nest Hub and Hub Max
  
I also opted to use the responsiveness option and checked the screens at the following width sizes:

- 350px
- 768px
- 992px
- 1400px

No issues arose, due to the simple layout of the site.

---
## 9. Bugs

- While adding placeholders to the pages, I faced an issue where the post didn't show the Cloudinary link placeholder when no image was provided by the user. This happened because the model's placeholder didn't match properly. I fixed it by directly linking the placeholder in the HTML.

- There was an issue with the JavaScript redirecting the user to a post detail page after a successful upload. The script expected a JSON response but didn't receive it. I added a check to see what it was receiving, which then allowed it to redirect correctly.

- I had trouble selecting parts of a form generated by Django in the template because there was no HTML to work with. I used the developer tools to see the structure and fixed the issue of the form overflowing on the page.

- The slugs for post details were based on the post titles. During manual testing, I found that errors occurred when creating or editing a post with the same title as another. I solved this by generating a random slug for each post, allowing titles to be the same without causing issues.

---
# Deployment

## Create Application

1. If you don't have a Heroku account, start by signing up and logging in.
2. To establish a new application, click the "new" button located at the top right corner of the dashboard, then select "Create new app."
3. Pick a distinct name for the application, indicate your residing region, and proceed by clicking "Create App."

## ElephantSQL
1. Visit elephantsql.com, log in using GitHub, and establish a fresh instance.
2. Once your project instance is set up, copy the URL. You can store this value as an environment variable to match the DATABASES variable in settings.py.
3. Utilize pip3 install dj_database_url==0.5.0 to install the dj-database-url package version 0.5.0. This will format the URL into a Django-compatible format and necessitate an update to the requirements.txt file.

## Cloudinary

1. Set up a Cloudinary account.
2. Upload relevant project images to the "Media Library."
3. Retrieve the Cloudinary API URL from your dashboard.

## Final Repo Preparations
1. Execute necessary project migrations by entering python3 manage.py makemigrations followed by python3 manage.py migrate in the terminal.
2. Integrate a Procfile into the project, including the line web: gunicorn [project_name].wsgi:application.

## Heroku Deploy
1. Return to Heroku and navigate to the Project’s page. Open the "Settings" tab and locate the "Config Vars" section.
2. Within "Config Vars," input the following key-value pairs:
   Key = PORT : Value = 8000
   Key = SECRET_KEY : Value = Your Django Secret Key from settings.py
   Key = DATABASE_URL : Value = ElephantSQL URL (from step 5)
   Key = CLOUDINARY_URL : Value = Cloudinary API URL (from step 9)
3. Proceed to the "Deploy" tab and scroll to the GitHub deployment method.
4. Search and connect to the appropriate repository by selecting the "Connect" button.
5. Continue scrolling to the bottom of the "Deploy" Page and choose your desired deployment method. Opt for "Automatically Deploy" to 
   trigger deployment with each new code push, or manually deploy by selecting the button at the page's bottom.

Your application is now successfully deployed!
----
## 11. Credits

- [Stack Overflow](https://stackoverflow.com) provided valuable assistance with problem-solving.
- [MDN Web Docs](https://developer.mozilla.org) contained a wealth of useful information for building the project.
- [W3Schools](https://www.w3schools.com) always has very helpful tutorials and references on various coding topics.
- [GitHub](https://github.com) offered numerous repositories that significantly aided in coding.
- [GeeksforGeeks](https://www.geeksforgeeks.org) had extensive information on Python and other programming languages.

  ## Follow Us on Facebook

Stay updated with our latest news and offers by following us on Facebook.

<a href="https://www.facebook.com/profile.php?id=61561756724837&sk=photos" target="_blank">
  <img src="https://github.com/IsaLubs/TechGiants/assets/147058041/e943ac6e-5ebc-4c0d-bf63-f46ec20d5fbb" alt="Facebook Page">
</a>

Click the image above to visit our Facebook page.


