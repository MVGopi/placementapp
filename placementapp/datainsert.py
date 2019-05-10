from flask import Flask, render_template, request
#from werkzeug import secure_filename
import csv
import sqlite3
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('fileupload.html')
@app.route('/upload_file', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      d=open(f,'r')
      csv_info = csv.reader(d)
      conn=sqlite3.connect('placeddata.db')
      cur=conn.cursor()
      #cur.execute("drop table placement if exits")
      cur.execute("create table placement('S.No' text,'College Name' text,'Student Name' text,'Rollno' text primary key,'Trained On - Program Name' text,'Placed Company Name' text,'Package per Annum' text,'Location' text,'Date of Join' text,'Offer Letter URL' text,'Trainer Name' text)")
      conn.commit()
      for record in csv_info:
         cur.execute("insert into placemnet values(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8],record[9],record[10])")
         conn.commit()
      return 'file uploaded successfully'
		
if __name__ == '__main__':
   app.run(debug = True)
