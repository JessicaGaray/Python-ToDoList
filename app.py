from flask import Flask, render_template, request, session, redirect, url_for, escape, make_response
from datetime import datetime, date

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'



@app.route('/', methods = ['GET'])
def add_item():
   return render_template('add_item.html')

@app.route('/add_item', methods = ['POST'])
def addsession():
      get_itemdes = request.form['itemdes']
      get_deadline = request.form['deadline']

      # get_deadline = datetime.strftime(deadline , '%m/%d/%Y')

      if 'item_list' in session:
         session_item_list = session['item_list']
         session_dl_list = session['dl_list']
      else:
         session_item_list = []
         session_dl_list = []
      

      session_item_list.append(get_itemdes)
      session_dl_list.append(get_deadline)

      session['item_list'] = session_item_list
      session['dl_list'] = session_dl_list

      return redirect(url_for('todolist'))

@app.route('/todolist')
def todolist():
   
   if 'item_list' in session:
      itemdes = session['item_list']
   else:
      itemdes = []
   if 'dl_list' in session:
      deadline = session['dl_list']
   else:
      deadline = []

   currentDate = datetime.now()
   return render_template('todo_list.html', itemdes=itemdes, deadline=deadline, currentDate = currentDate)

@app.route('/delete', methods=['get'])
def deleteitem():
   if 'item_list' in session:
      itemdes = session['item_list']
   else:
      itemdes = []
   if 'dl_list' in session:
      deadline = session['dl_list']
   else:
      deadline = []
   
   deleteId = int(request.args['id'])
   del itemdes[deleteId]
   del deadline[deleteId]

   session['item_list'] = itemdes
   session['dl_list'] = deadline
   
   return redirect(url_for('todolist'))

if __name__ == '__main__':
   app.run(debug=True)