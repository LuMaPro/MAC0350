from fastapi import FastAPI, Request, Response, Cookie, Depends, HTTPException, status
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import time

class User(BaseModel):
    name: str
    password: str
    bio: str

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

users = []

@app.middleware("http")
async def log_request_time(request: Request, call_next):
    start = time.perf_counter()
    response = await call_next(request)
    elapsed = time.perf_counter() - start
    response.headers["X-Process-Time"] = f"{elapsed:.4f}"
    print(f"[LOG] {request.method} {request.url.path} -> {elapsed:.4f}s")
    return response

def get_active_user(session: str = Cookie(None)):
    if not session:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Acesso negado")
    found = next((u for u in users if u.name == session), None)
    if not found:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Sessão inválida")
    return found

@app.get("/register")
def register_get(request: Request):
    return templates.TemplateResponse(request=request, name="register.html")

@app.post("/register")
async def register_post(user: User):
    for db_user in users:
        if db_user.name == user.name:
            return {"success": False, "user": user.name}
    users.append(user)
    return {"success": True, "user": user.name}

@app.get("/login")
def login_get(request: Request):
    return templates.TemplateResponse(request=request, name="login.html")

@app.post("/login")
def login_post(user: User, response: Response):
    for db_user in users:
        if db_user.name == user.name:
            if db_user.password == user.password:
                response.set_cookie(key="session", value=user.name, httponly=True)
                return {"success": True, "user": user.name}
            else:
                return {"success": False, "error": "Senha errada!"}
    return {"success": False, "error": "Nome de usuário não existente!"}

@app.get("/profile")
def profile(request: Request, user: User = Depends(get_active_user)):
    return templates.TemplateResponse(
        "profile.html",
        {
            "request": request,
            "user": user
        }
    )