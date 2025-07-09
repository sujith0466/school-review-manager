# 📘 School Review Manager

A Flask + MySQL web application where users can submit and view school reviews.  
Built as part of a web development internship task at **Edusaint**.

---

## 🎯 Features

- 📝 Submit school reviews via a clean web form
- 💾 Store and retrieve reviews using MySQL
- 🎨 Responsive UI using Bootstrap 5
- 🔐 Uses `.env` for secure config (no hardcoded secrets)
- ✅ Basic form validation with user feedback (using `flash()`)

---

## 📁 Project Structure
school_review_app/
├── app.py
├── config.py
├── requirements.txt
├── reviews.sql
├── .env.example
├── .gitignore
├── templates/
│ ├── add_review.html
│ └── reviews.html
└── static/

## 🚀 Setup Instructions

1. **Clone the repository** or download as ZIP:
   ```bash
   git clone https://github.com/sujith0466/school-review-manager.git
   cd school-review-manager
2. **Create a `.env` file** based on `.env.example`:
   ```env
   DB_HOST=localhost
   DB_USER=root
   DB_PASSWORD=yourpassword
   DB_NAME=school_reviews
   SECRET_KEY=your_secret_key_here
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the MySQL database**:
   - Open MySQL
   - Run the `reviews.sql` file to create the database and table:
     ```sql
     SOURCE path/to/reviews.sql;
     ```

5. **Run the Flask app**:
   ```bash
   python app.py
   ```

6. Open your browser and go to:
   ```
   http://localhost:5000
   ```

   ## 🙋‍♂️ Author
**Sanisetty Sujith Kumar**  
