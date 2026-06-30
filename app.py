
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Design System Gateway")

# السماح لواجهة الويب (React) بالاتصال بالخادم
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/projects")
def get_generated_projects():
    projects_dir = "projects"
    if not os.path.exists(projects_dir):
        return {"projects": []}
    
    project_list = []
    for proj_name in os.listdir(projects_dir):
        proj_path = os.path.join(projects_dir, proj_name)
        if os.path.isdir(proj_path):
            files = os.listdir(proj_path)
            project_list.append({
                "name": proj_name,
                "files_count": len(files),
                "files": files
            })
            
    return {"status": "success", "projects": project_list}
