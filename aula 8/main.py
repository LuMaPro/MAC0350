from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

curtidas_count = 0
ABAS = ["curtidas", "jupiter", "professor"]

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        request=request, 
        name="jupiter.html", 
        context={"request": request}
    )

@app.get("/aba/{nome_aba}", response_class=HTMLResponse)
async def get_aba(request: Request, nome_aba: str):
    if nome_aba not in ABAS:
        nome_aba = "curtidas"
    
    proxima_aba = ABAS[(ABAS.index(nome_aba) + 1) % len(ABAS)]
    
    return templates.TemplateResponse(
        request=request,
        name=f"{nome_aba}.html",
        context={
            "request": request,
            "curtidas": curtidas_count,
            "aba_ativa": nome_aba,
            "proxima_aba": proxima_aba
        }
    )

@app.post("/curtir", response_class=HTMLResponse)
async def curtir(acao: str = "incrementar"):
    global curtidas_count
    
    if acao == "zerar":
        curtidas_count = 0
    else:
        curtidas_count += 1
        
    return f'<span id="contador-curtidas">{curtidas_count}</span>'