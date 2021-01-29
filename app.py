
import math

from flask import Flask, render_template,request, url_for

from datetime import datetime
from flask import abort
from flask import redirect
from flask import url_for
import time


import crawring



kj_sub_list,kj_ref_list = crawring.kj()




app = Flask(__name__)


ip='0.0.0.0'
port = '5000'


@app.route('/')

def hello():
    return render_template('index.html',
                           ip= ip,
                           port=port,
                           title='깜슈니',
                           sub = kj_sub_list,
                           ref= kj_ref_list,
                           ref_len=len(kj_ref_list))
    print(ref)




if __name__ == '__main__':
    app.debug = True
    app.run(host=ip,port=port)
    app.run(debug=True)
