"""
## Flapi
A free and open source api for devs to get data of their given api structure. 
it helps to make development faster without the headache of data collection.
"""


from fastapi import FastAPI, Response
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.requests import Request
from fastapi.middleware.cors import CORSMiddleware
from routers import v1
from routers.pages import info

static = StaticFiles(directory="templates/static")
templates = Jinja2Templates(directory="templates")

app = FastAPI(
    title="Flapi",
    version="1.0.1",
    description="A free and open source api for devs to get data of their given api structure. it helps to make development faster without the headache of data collection.",
)
app.mount("/static", static)



# Setup CORSE
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(info.router)
app.include_router(v1.apiv1)


@app.route("/", ["GET", "POST"])
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
