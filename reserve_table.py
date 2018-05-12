from flask import Flask, request, redirect, url_for

from reservedb import get_posts, add_post

app = Flask(__name__)

# HTML template for the forum page
HTML_WRAP = '''\
<!DOCTYPE html>
<html>
<head>
  <title> Reserve Table</title>
    <style>
    h1, form {text-align: :center;}
    </style>
  </head>
  <body>
    <h1>Reserve Table</h1>
    <form method="post">
      <div>
        <label for="fName">First Name</label>
        <input type="text" id="fName" name="fName">
        <label for="lName">Last Name</label>
        <input type="text" id="lName" name="lName">
      </div>
      <p>
      <div>
        <label for="date">Date</label>:
        <input type="date" id="date" name="date">
        <label for="time">Time</label>
        <input type="time" id="time" name="time">
      </div>
      <p>
      <div>
        <label for="tableFor">Table For</label>
        <select id="tableFor" name="tableFor">
          <option value="1">1</option>
          <option value="2">2</option>
          <option value="3">3</option>
          <option value="4">4</option>
          <option value="5">5</option>
          <option value="5">5</option>
          <option value="5">5</option>
        </select>
        <p>
        <input type="submit" name="" value="Submit">
      </div>
    </form>
    %s
  </body>
</html>
'''

## HTML template for an individual reservation
POST = '''\
    <div class=post><em class=date>%s</em><br>%s</div>
'''

@app.route('/', methods=['GET'])
def main():
  '''Main page of the forum.'''
  posts = "".join(POST % (date, text) for text, date in get_posts())
  html = HTML_WRAP % posts
  return html


@app.route('/', methods=['POST'])
def post():
  '''New post submission.'''
  message = request.form['content']
  add_post(message)
  return redirect(url_for('main'))


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000)
