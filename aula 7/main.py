from typing import List
from sqlmodel import Field, Relationship, SQLModel, create_engine, select, Session


class Aluno(SQLModel, table=True):
    nusp: int | None = Field(default=None, primary_key=True)
    nome: str
    idade: int

    tarefas: List["Tarefa"] = Relationship(back_populates="aluno")


class Tarefa(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nome: str
    duracao: int
    aluno_nusp: int = Field(foreign_key="aluno.nusp")

    aluno: Aluno = Relationship(back_populates="tarefas")

from fastapi import FastAPI, HTTPException

arquivo_sqlite = "exercicio_7.db"
url_sqlite = f"sqlite:///{arquivo_sqlite}"

engine = create_engine(url_sqlite)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
def on_startup() -> None:
    create_db_and_tables()


@app.post("/alunos")
def criar_aluno(aluno: Aluno):
    with Session(engine) as session:
        session.add(aluno)
        session.commit()
        session.refresh(aluno)
        return aluno


@app.post("/tarefas")
def criar_tarefa(tarefa: Tarefa):
    with Session(engine) as session:
        session.add(tarefa)
        session.commit()
        session.refresh(tarefa)
        return tarefa


@app.get("/alunos")
def listar_alunos():
    with Session(engine) as session:
        return session.exec(select(Aluno)).all()


@app.get("/tarefas")
def listar_tarefas():
    with Session(engine) as session:
        return session.exec(select(Tarefa)).all()


@app.get("/alunos/{aluno_nusp}/tarefas")
def listar_tarefas_do_aluno(aluno_nusp: int):
    with Session(engine) as session:
        aluno = session.get(Aluno, aluno_nusp)
        if not aluno:
            raise HTTPException(status_code=404, detail="Aluno não encontrado")
        return aluno.tarefas