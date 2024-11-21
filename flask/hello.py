from flask import Flask     
app = Flask(__name__) 
@app.route('/hello') 

# binding to the function of route 
def hello_world():     
    return 'hello world' 

if __name__=='__main__':
    app.run(debug = True) 