from starlette.templating import Jinja2Templates
from starlette.requests import Request
import fastapi

router = fastapi.APIRouter()

templates = Jinja2Templates("Templates")


@router.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@router.get("/favicon.ico")
def favicon():
    return fastapi.responses.RedirectResponse(url="/static/img/favicon.ico")
