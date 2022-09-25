from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__) #This gonna be the MAIN file to run

@app.route("/")         
def my_home():
        return render_template('index.html')

@app.route("/works.html")         
def my_works():
        return render_template('works.html')

@app.route("/about.html")         
def my_about():
        return render_template('about.html')

@app.route("/contact.html")         
def my_contact():
        return render_template('contact.html')

@app.route("/components.html")         
def my_components():
        return render_template('components.html')

@app.route("/thankyou.html")         
def my_thankyou():
        return render_template('thankyou.html')   
        

def write_to_file(data): #Store in .txt
    with open('sg1Operations.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file=database.write(f'\n{email},{subject},{message}')  

def write_to_csv(data): #Store in .csv (Excel)
    with open('halo_blackOps.csv', mode='a') as database_2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        #spamwriter = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer=csv.writer(database_2, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL) 
        #spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
        csv_writer.writerow([email,subject,message])

        
@app.route("/my_submit_form", methods=['POST', 'GET'])         
def my_submit_form():
        if request.method == 'POST':
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')

        else:
            return 'something went wrong. Try again!' 