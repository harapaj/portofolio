import os
import csv
from flask import Flask, render_template, send_from_directory, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_pages(page_name):
    return render_template(page_name)


def write_dat(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n \n {email},  {subject},   {message}')


def write_data_csv(data):
    with open('database.csv', mode='a') as databasecsv:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_write = csv.writer(databasecsv, delimiter='\t', quotechar="+", quoting=csv.QUOTE_MINIMAL)
        csv_write.writerow([email, subject, message])


@app.route('/information', methods=['POST', 'GET'])
def info_contact():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_data_csv(data)
        return redirect('/information.html')
    else:
        return 'Something didn\'t work when trying to contact!'

# @app.route('/works.html')
# def works():
#     return render_template('works.html')
#
#
# @app.route('/about.html')
# def about():
#     return render_template('about.html')
#
#
# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')
#

# @app.route('/components.html')
# def components():
#     return render_template('components.html')
