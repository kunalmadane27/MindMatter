# MindMatter

MindMatter is a full-featured blogging platform designed to provide users with an intuitive interface for creating, editing, and managing blog posts. Whether you're a casual writer or a professional blogger, MindMatter makes it easy to share your stories, thoughts, and ideas with the world.

## Features

- *User Authentication*: Secure sign-up, login, and profile management.
- *Rich Text Editor*: Write and format posts with a built-in WYSIWYG editor.
- *Commenting System*: Engage readers with a user-friendly commenting feature.
- *Categories and Tags*: Organize posts for easier navigation and searchability.
- *Responsive Design*: Optimized for both desktop and mobile devices.
- *Admin Panel*: Manage users, moderate comments, and oversee content with an admin dashboard.
- *SEO-Friendly*: Built with SEO best practices to improve visibility on search engines.

## Installation

1. *Clone the Repository*  
    ```bash
   git clone https://github.com/Arfa-zaffar-khan/MindMatter.git

2. **Create a Python Virtual Environment**:
     ```bash
    python -m venv venv

3. *Activate the Python Environment*: 
     ```bash
    venv\Scripts\activate

4. **Install Dependencies**:
    ```bash
   pip install -r requirements.txt

5. *Change to the Project Directory*:
   ```bash
   cd src

6. *Create a .env File*:
   #Add the following environment variables in a new .env file in the src folder:
   ```plaintext
   SECRET_KEY=<your_secret_key>
   DEBUG=<True/False>
   NAME=<database_name>
   USER=<database_user>
   PASSWORD=<database_password>
   PORT=<database_port>
   HOST=<database_host>

7.*Import Workspace and Collection*:
    ```plaintext
    1.Click on Import.
    2.Select the file shared with you.
    3.Create an environment.
    4.Add the DEVURL variable as specified.