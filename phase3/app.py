from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('5.html')

@app.route('/add_song', methods=['POST'])
def add_song():
    song = request.get_json()
    name = song['song_name']
    duration = song['duration']
    conn = sqlite3.connect('playlist.db')
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM playlist WHERE song_name=?", (name,))
    result = c.fetchone()
    if result[0] == 0:
        c.execute("INSERT INTO playlist (song_name, duration) VALUES (?, ?)", (name, duration))
        conn.commit()
    conn.close()
    return ('', 204)

@app.route('/playlist.html')
def display_table():
    conn = sqlite3.connect('playlist.db')
    cursor = conn.cursor()

    # Fetch data from the database
    cursor.execute('SELECT * FROM playlist')
    data = cursor.fetchall()

    # Close the database connection
    cursor.close()
    conn.close()

    return render_template('playlist.html', data=data)

@app.route('/remove', methods=['GET', 'POST'])
def remove_element():
    conn = sqlite3.connect('playlist.db')
    cursor = conn.cursor()

    if request.method == 'POST':
        row_id = request.form['row_id']
        cursor.execute('DELETE FROM playlist WHERE id = ?', (row_id,))
        conn.commit()

    cursor.execute('SELECT * FROM playlist')
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('playlist.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)