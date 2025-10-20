from sqlalchemy import select

from database import engine, Base, session_factory

from models import RawVacancys, Resumes


def create_tables():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)



def insert_resume(title:str):
    with session_factory() as session:
        resume = Resumes(title=title)
        session.add(resume) # add_all
        session.commit()

def select_by_id_resume(resume_id:int = 1):
    with session_factory() as session:
        result_resume = session.get(Resumes, resume_id) # по pk
        return result_resume

def select_all_resume():
    with session_factory() as session:
        query = select(Resumes)
        result = session.execute(query)
        result = result.scalars().all()
        return result

def update_resume(resume_id:int, new_title:str):
    with session_factory() as session:
        resume = session.get(Resumes, resume_id)
        resume.title = new_title
        session.commit()