from flask import Flask, render_template,url_for,request,jsonify,send_file
# from  werkzeug import secure_filename
#from models import img
import boto3
import snowflake.connector

app=Flask(__name__)
@app.route('/',methods=['POST','GET'])
def index():
	if request.method == "POST":
		try:
			con = snowflake.connector.connect(
            user='swethaMP',
            password='@200500yS',
            account='pe60001.ap-southeast-1',
            database='TESTDATA',
            warehouse='compute_wh'
   			)
			email = str(request.form['email'])
			# password = request.form['password']
			age = request.form['age']
			gender = request.form['gender']
			phoneno = request.form['phnu']
			
			# print(img)
			cur = con.cursor()
			
			q = "insert into public.samle_table values('"+email+"',"+age+",'"+gender+"',"+phoneno+");"
			cur.execute(q)
			one_row = cur.fetchall()
			print(one_row)
			img = request.files['file']
			img.save("tag.jpg")
			s3 = boto3.resource(
    		service_name='s3',
    		region_name='ap-southeast-1',
    		aws_access_key_id='AKIAZQNBXQVS3IAL5DPP',
    		aws_secret_access_key='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'
			)
			# for bucket in s3.buckets.all():
			# 	print(bucket.name)
			s3.Bucket('diseasebuck').upload_file(Filename='tag.jpg', Key='Images/'+img.filename+'.jpg')

			# fname= img.filename
			# mtype = img.mimetype
			# image= Img(img-pic.read,mimetype=mtype,name=fname)
			# image.save(fname)
			return "<p>Data loaded successfully!!!Processing</p><center><img height=250px width=250px  src = 'https://blog.wf-education.com/wp-content/uploads/2020/08/Book-Doctor-GIF222.gif' ></center>"
		# except:
		# 	return "failed"
		finally:
			cur.close()
			# con.close()return "success"
	return render_template('index.html')
if __name__=="__main__":
	app.run(debug=True)