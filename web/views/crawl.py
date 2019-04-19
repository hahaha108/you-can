import os

from application import app
from flask import Blueprint,jsonify,request
from crawler import parse
import uuid

route_crawl = Blueprint('crawl',__name__)

@route_crawl.route("/",methods = [ "GET","POST" ])
def crawl():
    data = {}
    if request.method == "POST":
        url = request.form['urlTextBox']
        video_id = str(uuid.uuid1())
        path = os.path.join(app.static_folder + '/cache',video_id)
        if parse(url,video_id,path=path):
            data['filename'] = video_id + '.mp4'
    return jsonify(data)