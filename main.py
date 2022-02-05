from fastapi import FastAPI

# Routers
from api.routes import users, sections, courses

tags_metadata = [
    {
        "name": "Users",
        "description": "Operations with **users**. The **create** logic is also here.",
    },
    {
        "name": "Courses",
        "description": "Operations with **courses**. The **create** logic is also here.",
    },
    {
        "name": "Sections",
        "description": "Operations with **sections**. The **create** logic is also here.",
    },
]

app = FastAPI(
    title="LMS Backend",
    description="Here you'll find the endpoints to a CRUD backend for a Learning Management Systems",
    version="0.0.1",
    contact={"name": "Noer Is Amazing", "email": "noer@lightworksweb.nl"},
    docs_url="/documentation",
    openapi_tags=tags_metadata,
)

app.include_router(users.router)
app.include_router(sections.router)
app.include_router(courses.router)
