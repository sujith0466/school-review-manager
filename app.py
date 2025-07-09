from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
from config import DB_CONFIG

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Use a secure random string

def get_db_connection():
    return mysql.connector.connect(
        host=DB_CONFIG["HOST"],
        user=DB_CONFIG["USER"],
        password=DB_CONFIG["PASSWORD"],
        database=DB_CONFIG["DATABASE"]
    )

@app.route('/')
def home():
    return redirect(url_for('add_review'))

@app.route('/add-review', methods=['GET', 'POST'])
def add_review():
    if request.method == 'POST':
        school_name = request.form.get('school_name', '').strip()
        reviewer_name = request.form.get('reviewer_name', '').strip()
        rating = request.form.get('rating', '').strip()
        comment = request.form.get('comment', '').strip()

        # Basic validation
        if not (school_name and reviewer_name and rating and comment):
            flash('❌ Please fill out all fields.', 'danger')
            return redirect(url_for('add_review'))

        try:
            rating = int(rating)
            if not (1 <= rating <= 5):
                flash('❌ Rating must be between 1 and 5.', 'danger')
                return redirect(url_for('add_review'))

            conn = get_db_connection()
            cursor = conn.cursor()
            query = """
                INSERT INTO reviews (school_name, reviewer_name, rating, comment)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query, (school_name, reviewer_name, rating, comment))
            conn.commit()
            cursor.close()
            conn.close()

            flash('✅ Review submitted successfully!', 'success')
            return redirect(url_for('view_reviews'))

        except Exception as e:
            flash(f'❌ Error submitting review: {str(e)}', 'danger')
            return redirect(url_for('add_review'))

    return render_template('add_review.html')

@app.route('/reviews')
def view_reviews():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM reviews ORDER BY id DESC")
        reviews = cursor.fetchall()
        cursor.close()
        conn.close()
        return render_template('reviews.html', reviews=reviews)
    except Exception as e:
        flash(f'❌ Failed to load reviews: {str(e)}', 'danger')
        return render_template('reviews.html', reviews=[])

if __name__ == '__main__':
    app.run(debug=True)
