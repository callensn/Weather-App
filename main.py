import fastapi
import uvicorn
from starlette.staticfiles import StaticFiles
from api import weather_api
from views import home

api = fastapi.FastAPI()


def configure():
    """
    Organizational function to group together commands and code that needs to run in order to make
    the api work. It's first call is to a function that has packaged all the mounting and routing
    together to start the api.
    """
    configure_routing()


def configure_routing():
    """
    Function for initializing the API routs that we pipe in from other files in this repo.
    This is called at runtime so that the website has all the correct routs specified as part
    of the API calls.
    """
    api.mount("/static", StaticFiles(directory="static"), name="static")
    api.include_router(home.router)
    api.include_router(weather_api.router)


if __name__ == "__main__":
    configure()
    uvicorn.run(api, port=8000, host="127.0.0.1")
else:  # this is needed for running in production
    configure()

# In production the line calling __name__ doesn't get called, so the else statement exists to be able to call
# the configure() function when the main function is not callable (such as in production)
