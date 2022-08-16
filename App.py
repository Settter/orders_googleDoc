from fastapi import FastAPI
from starlette.requests import Request
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from init import app, UV

templates = Jinja2Templates(directory="templates")
app.mount('/static', StaticFiles(directory='static'), name='static')


@app.get("/")
async def main(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})


if __name__ == '__main__':
    UV.run(app)
