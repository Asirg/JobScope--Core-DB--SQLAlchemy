import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from src.queries.core import insert_resume, update_resumes
from src.queries.orm import (
    create_tables, select_by_id_resume, insert_resumes, 
    update_resume, select_all_resume, select_resume_by_title, 
    join_cte_subquery_window_func, select_raw_vacancies_with_lazy_relationship
    ,select_raw_vacancies_with_selectinload_relationship
)

create_tables()


insert_resumes()
# select_resume_by_title()

# join_cte_subquery_window_func()

# select_raw_vacancies_with_selectinload_relationship()