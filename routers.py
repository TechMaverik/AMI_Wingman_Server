from fastapi import FastAPI
from services import Services as wingman_services
from Data_Models.waypoint_model import waypoints
from fastapi.middleware.cors import CORSMiddleware
import loggers
import uvicorn

wingman = FastAPI()
wingman.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@wingman.get("/")
def get_api_version():
    version = wingman_services.get_api_version()
    return version


@wingman.post("/launch")
def launch(waypoints_data: waypoints):
    wingman_services().get_waypoints(waypoints_data)
    return True


@wingman.post("/stop")
def stop():
    return True


@wingman.post("/rtb")
def rtb():
    return True


if __name__ == "__main__":
    uvicorn.run(wingman, host="192.168.1.4", port=5000)