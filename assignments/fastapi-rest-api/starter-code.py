"""
Starter code for FastAPI REST API Assignment
Student Name: _______________
Date: _______________
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional

# Initialize FastAPI app
app = FastAPI(
    title="To-Do List API",
    description="A simple REST API for managing tasks",
    version="1.0.0"
)

# TODO: Define your Task model using Pydantic BaseModel
# class Task(BaseModel):
#     id: int
#     title: str = Field(..., min_length=3, max_length=100)
#     description: Optional[str] = Field(None, max_length=500)
#     completed: bool = False


# In-memory storage for tasks (will reset when server restarts)
tasks_db = []
next_id = 1


@app.get("/")
async def root():
    """Welcome endpoint - TODO: Return a welcome message"""
    pass


# TODO: Implement GET /tasks endpoint to list all tasks


# TODO: Implement GET /tasks/{task_id} endpoint to get a specific task


# TODO: Implement POST /tasks endpoint to create a new task


# TODO: Implement PUT /tasks/{task_id} endpoint to update a task


# TODO: Implement DELETE /tasks/{task_id} endpoint to delete a task


# Run the server with: uvicorn starter-code:app --reload
