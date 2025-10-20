import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from src.queries.core import insert_resume, update_resumes
from src.queries.orm import create_tables, select_by_id_resume, insert_resume, update_resume

create_tables()


insert_resume("resume 1")
resume = select_by_id_resume()
print(resume.title)

update_resume(1, "resume 100")

resume = select_by_id_resume()
print(resume.title)