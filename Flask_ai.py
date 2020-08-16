from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return '<h>hello moji_:)</h> <button style="height:20px,width:50px">do it</button><p>this is a big bang start .... </p>'


@app.route('/moji/bang/<name>', methods=['GET','POST'])
def bang(name):
    if request.method == 'GET':
        return 'this %s get' %name
    else:
        return  'this %s post' %name

@app.route('/<moji>')
def moji(moji):
    return render_template('firstpage.html', nme=moji)

if __name__ == '__main__':
    app.run(debug=True)


