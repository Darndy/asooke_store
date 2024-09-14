# How to Run the project

* Create a virtual environment
* Install requirements from requirements.txt file
* run project with the following command

```bash

python manage.py runserver

```
# Project Name
Ajoke Alasooke Store

# Introduction
Introduction
Welcome to Ajoke Alasooke, a premium local fabrics store that offers not only a wide selection of high-quality fabrics but also top-tier gele styling services. Our mission is to celebrate and promote traditional fashion while blending it with modern trends, making it accessible and fashionable for all.

This project is a fully functional web application built using Django, aimed at providing customers with an easy and seamless online shopping experience for purchasing fabrics and booking gele styling appointments. With a clean, responsive interface, users can explore our products, learn more about our services, and effortlessly interact with the platform on any device.

Key Features:
Fabric Store: Browse a curated collection of local fabrics with detailed descriptions and images.
Gele Stylist: Learn about our styling services and book appointments for personalized gele styling.
User Accounts: Register and log in to manage purchases, track orders, and book appointments.
Secure Payments: Integrated secure payment system for easy and safe transactions.
Admin Dashboard: An admin panel for managing inventory, services, users, and orders.
Ajoke Alasooke’s website is designed to provide a seamless, engaging experience that showcases the beauty and richness of local textiles. Whether you're looking for the perfect fabric for an event or expert gele styling, we have you covered!

# installation

To run the Ajoke Alasooke project locally, follow these steps to set up the environment on your machine:

Prerequisites
Ensure you have the following installed on your system:

Python 3.8+
Git
pip (Python package installer)
Virtualenv (optional but recommended for isolated environments)
Step 1: Clone the Repository
First, clone the project repository from GitHub to your local machine.

bash
Copy code
git clone https://github.com/your-username/ajoke-alasooke.git
cd ajoke-alasooke

Step 2: Create and Activate a Virtual Environment (optional but recommended)
To avoid potential conflicts with other Python projects, it's recommended to create a virtual environment:

bash
Copy code
# Create a virtual environment
python -m venv env

# Activate the virtual environment
# On Windows
.\env\Scripts\activate

# On macOS/Linux
source env/bin/activate
Step 3: Install Dependencies
Install the required Python packages from the requirements.txt file:

bash
Copy code
pip install -r requirements.txt
Step 4: Set Up the Database
Apply the initial database migrations to set up the SQLite database (or your preferred database).

bash
Copy code
python manage.py migrate
Step 5: Create a Superuser (Admin Account)
Create an admin account to access the Django Admin dashboard:

bash
Copy code
python manage.py createsuperuser
Follow the on-screen instructions to set the username, email, and password.

Step 6: Collect Static Files
Run the following command to collect all static files (CSS, JavaScript, images) into a single directory:

bash
Copy code
python manage.py collectstatic
Step 7: Run the Development Server
Start the Django development server:

bash
Copy code
python manage.py runserver
Open your browser and navigate to http://127.0.0.1:8000/ to access the application.

Optional: Running Tests
To ensure that everything is working as expected, you can run the automated tests provided:

bash
Copy code
python manage.py test
This installation guide assumes the user has basic knowledge of Python and Django, and it's designed to help them quickly get the project up and running locally. Adjust the repository URL and any specific details as needed for your project.

# Usage

Once the project is up and running, you can explore the various features of the Ajoke Alasooke website. Below are the main functionalities and how to use them:

1. Accessing the Website
After starting the development server, open a browser and navigate to the following URL to view the website:

arduino
Copy code
http://127.0.0.1:8000/
You will see the homepage of Ajoke Alasooke, showcasing local fabrics and styling services like gele tying.

2. Register an Account
To start using personalized services, you need to register for an account:

Click on the Register button in the navigation bar or in the login section.
Fill out the registration form with your username, email, and password.
After successful registration, you can log in to your account.
3. Logging In
Once you have an account, you can log in:

Navigate to the Login page via the link in the header or main menu.
Enter your username and password to log in.
If you provide incorrect credentials, an error message will be displayed.
4. Browse Fabrics and Services
Fabrics: Explore a wide range of local fabrics on the website. Each fabric includes detailed descriptions, pricing, and availability.
Gele Stylist Services: You can book services for gele styling for your events.
5. Admin Access
As an admin user, you can access the Django Admin Panel to manage fabrics, services, and users:

Log in with your admin credentials.

Visit the Admin panel at:

arduino
Copy code
http://127.0.0.1:8000/admin/
Here, you can:

Add, update, or delete fabrics and services.
Manage user accounts and permissions.
6. Contact and Booking Form
Users can fill out a contact form to make inquiries or book styling services:

Navigate to the Contact or Book Appointment section.
Enter your details and message.
Submit the form to reach out for more information or booking services.
7. Viewing Orders and Services
Once logged in, users can:

View their order history for fabric purchases.
Check the status of their bookings with the gele stylist.
8. Logging Out
To log out of your account, click the Logout button located in the top right corner of the navigation bar.

Example Workflow:
Register an account → Login → Browse fabrics and services → Book a gele stylist service.
Admin workflow: Login with admin credentials → Access Admin Panel → Manage products or User accounts.
This Usage section provides a basic overview of how to interact with the website, both as a regular user and an admin. You can adjust this section based on additional features you implement in your project.

# Contributing
Contributions are welcome and appreciated! If you’d like to help improve Ajoke Alasooke, here’s how you can get started:

1. Fork the Repository
Fork the repository to your GitHub account by clicking the Fork button at the top right corner of this page.
After forking, clone the repository to your local machine:
bash
Copy code
git clone https://github.com/YOUR-USERNAME/Ajoke-Alasooke.git
2. Set Up a Local Environment
Follow the Installation instructions in this README.md to set up the project locally.
Make sure everything works correctly by running the Django development server:
bash
Copy code
python manage.py runserver
3. Create a New Branch
Before making any changes, create a new branch for your feature or fix:
bash
Copy code
git checkout -b feature/your-feature-name
4. Make Changes
Add your feature, bug fix, or improvement. Ensure the code is clean and follows Django best practices.
Write unit tests for any new functionality where applicable.
Run all tests to make sure your changes don’t break existing functionality:
bash
Copy code
python manage.py test
5. Commit and Push Changes
Once you’re satisfied with your changes, commit them to your branch:
bash
Copy code
git add .
git commit -m "Add your message here"
Push your changes to your forked repository:
bash
Copy code
git push origin feature/your-feature-name
6. Create a Pull Request (PR)
Navigate to the original repository on GitHub and click the Compare & Pull Request button for your branch.
In the pull request description, include the details of what you have changed and why.
Wait for feedback or approval from the repository maintainers.
7. Code Review
Your pull request will undergo a code review by project maintainers.
You may be asked to make some adjustments or clarifications before your contribution can be merged.
Once approved, your changes will be merged into the main branch.
Guidelines for Contributions
Ensure your code follows PEP 8 standards.
Maintain clear and concise commit messages.
Be sure to add relevant comments where necessary, especially for complex logic.
Respect the current code structure and naming conventions.
For significant changes, open an issue first to discuss your idea.
8. Report Issues
If you come across any bugs or want to suggest new features, feel free to open an issue in the GitHub repository:

Go to the Issues tab.
Click New Issue.
Describe the issue or enhancement in detail and provide steps to reproduce the bug (if applicable).
We appreciate all contributions, no matter how big or small!
 #   Related Projects
If you’re interested in exploring more projects related to local fabrics, fashion, or similar web applications, here are some notable ones:

1. Fabric Store Management System
Description: A comprehensive system for managing fabric inventory, sales, and customer information. Built with Django and React.
Key Features: Inventory management, sales reporting, customer profiles, order tracking.
2. Fashion E-commerce Platform
Description: An online store for fashion products with features like user authentication, product management, and order processing.
Key Features: User accounts, product listings, shopping cart, payment integration.
3. Gele Styling Application
Description: A web application dedicated to gele styling services, including booking appointments and showcasing styles.
Key Features: Service booking, gallery of styles, user reviews, contact form.
4. Textile Design Portfolio
Description: A portfolio website showcasing textile designs, including fabric samples and design projects.
Key Features: Project galleries, design descriptions, contact form, responsive layout.
5. Local Crafts Marketplace
Description: A marketplace platform for local crafts and handmade goods, with features for sellers and buyers.
Key Features: Seller accounts, product listings, search and filter options, order management.
6. Fashion Trends Blog
Description: A blog focused on the latest trends in fashion, including fabric trends and styling tips.
Key Features: Blog posts, categories, comments, RSS feed.
Feel free to check out these projects for inspiration or to find additional tools and resources that may complement Ajoke Alasooke.


# License
This project is licensed under the ALX SE License. See the LICENSE file for details.

MIT License Summary
The MIT License is a permissive free software license originating at the Massachusetts Institute of Technology (MIT). It is a simple and easy-to-understand license that places very few restrictions on reuse, making it a popular choice for open source projects.

Key Points of the MIT License:

Permission: Allows for the use, copy, modification, merging, publishing, distribution, sublicensing, and/or selling of copies of the Software.
Attribution: Requires the inclusion of the original copyright notice and permission notice in all copies or substantial portions of the Software.
Warranty Disclaimer: The Software is provided "as is", without warranty of any kind. The authors are not liable for any claims, damages, or other liabilities.
For more details, you can review the full text of the MIT License included in the LICENSE file in this repository.