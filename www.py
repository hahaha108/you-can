from application import app

from web.views.index import route_index
from web.views.crawl import route_crawl

app.register_blueprint(route_index,url_prefix = "/" )
app.register_blueprint(route_crawl,url_prefix = "/crawl" )