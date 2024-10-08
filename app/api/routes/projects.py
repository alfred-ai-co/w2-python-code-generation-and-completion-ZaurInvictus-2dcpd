# Project Endpoints
from typing import List
from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from fastapi import Depends

import app.db_models.crud as crud
from app.api_models.projects import ProjectCreate, ProjectResponse
from app.api.dependencies.sqldb import get_db


router = APIRouter()


@router.post('', response_model=ProjectResponse)
async def create_project(project: ProjectCreate, db: Session = Depends(get_db)):
    db_project = crud.create_project(
        db, 
        project.name, 
        project.description
        )
    return db_project

# http://0.0.0.0:8000/api/projects?skip=0&limit=2
@router.get('', response_model=List[ProjectResponse])
async def list_projects(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Endpoint to list projects with pagination.
    example: http://0.0.0.0:8000/api/projects?skip=0&limit=2
    Query Parameters:
    - skip: Number of records to skip (default: 0)
    - limit: Maximum number of records to return (default: 10)
    """
    projects = crud.get_projects(db, skip=skip, limit=limit)
    return projects


@router.get('/{project_id}', response_model=ProjectResponse)
async def read_project(project_id: int, db: Session = Depends(get_db)):
    db_project = crud.get_project(db, project_id)
    return db_project

@router.put('/{project_id}', response_model=ProjectResponse)
async def update_project(project_id: int, project: ProjectCreate, db: Session = Depends(get_db)):
    db_project = crud.update_project(
        db, 
        project_id, 
        project.name, 
        project.description
        )
    return db_project

@router.delete('/{project_id}')
async def delete_project(project_id: int, db: Session = Depends(get_db)):
    crud.delete_project(db, project_id)
    return {'message': f'Project with id {project_id} deleted'}