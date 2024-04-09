from fastapi import FastAPI
import uvicorn
from app.authentication import endpoint as userendpoint
from app.src import routes
from app.src.smtp import endpoint as smtpendpoint

app = FastAPI()


app.include_router(userendpoint.router)
app.include_router(routes.router)



@app.get("/")
def welcome():
    return {"msg" : "welcome"}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True

    )
