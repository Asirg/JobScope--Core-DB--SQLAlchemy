from database import engine
from sqlalchemy import select, text



# def select_resumes():
#     with  engine.connect() as conn:
#         query = text("""SELECT * FROM resumes""")
#         res = conn.execute(query)
#         print(res.all())

def insert_resume(title:str):
    with engine.connect() as conn:
        stmt = text("""INSERT INTO resumes (title) VALUES
            (:title);
        """)
        stmt = stmt.bindparams(title=title)
        conn.execute(stmt)
        conn.commit()


def update_resumes(resume_id:int, new_title:str):
    with engine.connect() as conn:
        stmt = text("""UPDATE resumes SET title=:new_title WHERE id=:resume_id""")
        stmt = stmt.bindparams(new_title = new_title, resume_id = resume_id)
        conn.execute(stmt)
        conn.commit()