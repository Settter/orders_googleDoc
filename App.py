import time
from threading import Thread

from starlette.requests import Request
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from db_methods import total
from doc_save import save_db_values
from init import app, UV
from bot import mass_message, start_bot
from matplot import graf_img

# add templates
templates = Jinja2Templates(directory="templates")
# add static files path
app.mount('/static', StaticFiles(directory='static'), name='static')


# render main site page
@app.get("/")
def main(request: Request):
    print('render html')
    return templates.TemplateResponse('index.html', {'request': request, 'total': total()})


# updating db table and chart on site and check bot mass mailing
def autoupdate():
    while True:
        save_db_values()
        graf_img()
        mass_message()
        time.sleep(60)
    pass


# run site
def run_app():
    UV.run(app)


if __name__ == '__main__':
    Thread(target=autoupdate).start()
    Thread(target=run_app).start()
    Thread(target=start_bot).start()
