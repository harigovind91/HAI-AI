from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import sqlite3

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

class ProjectData(BaseModel):
    user_id: int
    project_name: str
    code: str

@app.post("/api/save-project")
async def save_project(data: ProjectData):
    conn = sqlite3.connect('hai_global.db')
    c = conn.cursor()
    c.execute("INSERT INTO projects (user_id, name, code) VALUES (?,?,?)", (data.user_id, data.project_name, data.code))
    conn.commit()
    conn.close()
    return {"status": "success"}

@app.get("/api/user-projects/{user_id}")
async def get_projects(user_id: int):
    conn = sqlite3.connect('hai_global.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("SELECT * FROM projects WHERE user_id = ?", (user_id,))
    return [dict(r) for r in c.fetchall()]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

