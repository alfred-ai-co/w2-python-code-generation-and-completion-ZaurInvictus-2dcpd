from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from fastapi import HTTPException

from app.db_models.base import Project, Ticket

# CRUD operations for Project

# CREATE
# PROMPT - Define a function called create_project that adds a new project record to the database. 
# The function should accept a database session and two parameters: 'name' and 'description'. 
# It should create a new instance of the 'Project' model with the provided 'name' and 'description', add it to the session, commit the transaction, refresh the instance, and return the newly created project.
def create_project(db: Session, name: str, description: str) -> Project:
    new_project = Project(name=name, description=description)
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return new_project


# GET BY ID
# PROMPT - Define a function called get_project that retrieves a project record from the database by its ID. 
# The function should accept a database session and a project ID as parameters. 
# It should query the database for the project with the specified ID and return the first result found.
def get_project(db: Session, project_id: int) -> Project:
    try:
        return db.query(Project).filter(Project.id == project_id).one()
    except NoResultFound:
        raise HTTPException(status_code=404, detail=f"Project with ID {project_id} does not exist.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")


# UPDATE
# PROMPT -  Define a function called update_project that updates an existing project in the database. 
# The function should accept a database session, a project ID, a name, and a description. It should query the database for the project with the specified ID, update its name and description, commit the changes, refresh the project instance, and return the updated project.
def update_project(db: Session, project_id: int, name: str, description: str) -> Project:
    try:
        project = db.query(Project).filter(Project.id == project_id).one()
        project.name = name
        project.description = description
        db.commit()
        db.refresh(project)
        return project
    except NoResultFound:
        raise HTTPException(status_code=404, detail=f"Project with ID {project_id} does not exist.")
    except Exception as e:
        db.rollback()  # Rollback the session in case of any error
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")
    

# DELETE
# PROMPT - Define a function called delete_project that removes a project record from the database by its ID. 
# The function should accept a database session and a project ID as parameters. 
# It should first check if the project exists, then delete the project from the session and commit the transaction.
def delete_project(db: Session, project_id: int) -> bool:
    try:
        project = db.query(Project).filter(Project.id == project_id).one()
        db.delete(project)
        db.commit()
        return True
    except NoResultFound:
        raise HTTPException(status_code=404, detail=f"Project with ID {project_id} does not exist.")
    except Exception as e:
        db.rollback()  # Rollback the session in case of any error
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")


# CRUD operations for TICKET
# CREATE
def create_ticket(db: Session, title: str, description: str, project_id: int, status: str, priority: str) -> Ticket:
    new_ticket = Ticket(
        title=title, 
        description=description, 
        project_id=project_id, 
        status=status, 
        priority=priority
    )
    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)
    return new_ticket


# GET BY ID
def get_ticket(db: Session, ticket_id: int) -> Ticket:
    try:
        return db.query(Ticket).filter(Ticket.id == ticket_id).one()
    except NoResultFound:
        raise HTTPException(status_code=404, detail=f"Ticket with ID {ticket_id} does not exist.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")


# UPDATE
def update_ticket(
        db: Session, 
        ticket_id: int, 
        title: str, 
        description: str, 
        project_id: int, 
        status: str, 
        priority: str
        ) -> Ticket:
    try:
        ticket = db.query(Ticket).filter(Ticket.id == ticket_id).one()
        ticket.title = title
        ticket.description = description
        ticket.project_id = project_id
        ticket.status = status
        ticket.priority = priority
        db.commit()
        db.refresh(ticket)
        return ticket
    except NoResultFound:
        raise HTTPException(status_code=404, detail=f"Ticket with ID {ticket_id} does not exist.")
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")
  

# DELETE
def delete_ticket(db: Session, ticket_id: int) -> bool:
    try:
        ticket = db.query(Ticket).filter(Ticket.id == ticket_id).one()
        db.delete(ticket)
        db.commit()
        return True
    except NoResultFound:
        raise HTTPException(status_code=404, detail=f"Ticket with ID {ticket_id} does not exist.")
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")