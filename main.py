from flask import Flask, render_template, request
from BankAccount import BankAccount
from Repository import Repository

app = Flask('app')
account = BankAccount(0)  #object
name = BankAccount.name
table = Repository  #object


#Each app route is a new page/function
@app.route('/', methods=["POST", "GET"])  #homepage
def main_page():
  return render_template('main.html')


@app.route("/show", methods=["POST", "GET"])
def show():
  if request.method == "POST":
    amount = request.form['amount']
    account.deposit(int(amount))
    #new code alert
    #This adds the value of amount to object account, then we can call it at return
    account.get_amount(amount)
    #Returns transaction type from the drop down menu
    name = request.form['category']
    account.get_type(name)
    print(name)  #print works
    #end new code alert

  return render_template('main.html',
                         balance=account.balance,
                         name=account.name,
                         amount=account.amount)

app.run(host='0.0.0.0', port=8080)

#GOAL!!! Find a way to call functions in this page
# in java, the easiest way to call functions from bankaccount,
# is to create an object here in main.py

#New Idea: Have a list of transactions. When the user deposit/withdraw money, it #adds to a list, which is then displayed in Transactions
