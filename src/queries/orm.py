from sqlalchemy import select, cast, func, Integer, and_
from sqlalchemy.orm import aliased, joinedload, selectinload

from database import engine, Base, session_factory

from models import RawVacancys, Resumes, Workload


def create_tables():
    Base.metadata.drop_all(engine)
    # Base.metadata.create_all(engine)



def insert_resumes():
    with session_factory() as session:
        raw_vacancy_1 = RawVacancys(
            name="vacansy 1"
        )
        raw_vacancy_2 = RawVacancys(
            name="vacansy 2"
        )
        raw_vacancy_3 = RawVacancys(
            name="vacansy 3"
        )


        resume_1 = Resumes(
            title="Python dev", compensation_min=100, compensation_max=200, workload=Workload.parttime, raw_vacancy_id=1
        )
        resume_2 = Resumes(
            title="Python dev", compensation_min=150, compensation_max=300, workload=Workload.parttime, raw_vacancy_id=1
        )
        resume_3 = Resumes(
            title="Python dev", compensation_min=100, compensation_max=400, workload=Workload.parttime, raw_vacancy_id=2
        )
        resume_4 = Resumes(
            title="Python dev", compensation_min=1000, compensation_max=2000, workload=Workload.fulltime, raw_vacancy_id=3
        )
        session.add_all([raw_vacancy_1, raw_vacancy_2, raw_vacancy_3])
        session.add_all([resume_1, resume_2, resume_3, resume_4]) # add_all
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

def select_resume_by_title():
    with session_factory() as session:
        query = (
            select(
                Resumes.workload,
                cast(func.avg(Resumes.compensation_max), Integer).label("avg_compensation_max"),
            )
            .select_from(Resumes)
            .where(and_(
                Resumes.title.contains("Python"),
                Resumes.compensation_max > 10
            ))
            .group_by(Resumes.workload)
            # .having(cast(func.avg(Resumes.compensation_max), Integer) > 100)
        )
        result_query = session.execute(query)
        result = result_query.all()
        print(result)

def join_cte_subquery_window_func():
    with session_factory() as session:
        r = aliased(Resumes)
        v = aliased(RawVacancys)

        subq = (
            select(
                r,
                v,
                # v.id.lavel("raw_va")
                func.avg(r.compensation_max).over(partition_by=r.workload).cast(Integer).label("avg_workload_compensation")
            )
            .select_from(r)
            .join(v, r.raw_vacancy_id == v.id).subquery("helper1")
        )

        cte = (
            select(
                subq.c.id,
                subq.c.title,
                subq.c.name,
                subq.c.compensation_max,
                subq.c.workload,
                subq.c.avg_workload_compensation,
                (subq.c.avg_workload_compensation - subq.c.compensation_max).label("compensation_diff")
            )
            .cte("helper2")
        )

        query = (
            select(cte)
            .order_by(cte.c.compensation_diff.desc())
        )

        res = session.execute(query).all()

        print(res)


def select_raw_vacancies_with_lazy_relationship():
    with session_factory() as session:
        query = (
            select(RawVacancys)
        )

        res = session.execute(query)
        result = res.scalars().all()

        worker_1_resumes = result[0].resumes
        print(worker_1_resumes)

        worker_2_resumes = result[1].resumes
        print(worker_2_resumes)


def select_raw_vacancies_with_joinedload_relationship():
    with session_factory() as session:
        query = (
            select(RawVacancys)
            .options(joinedload(Resumes))
        )

        res = session.execute(query)
        result = res.unique().scalars().all()

        worker_1_resumes = result[0].resumes
        print(worker_1_resumes)

        worker_2_resumes = result[1].resumes
        print(worker_2_resumes)

def select_raw_vacancies_with_selectinload_relationship():
    with session_factory() as session:
        query = (
            select(RawVacancys)
            .options(selectinload(RawVacancys.resumes))
        )

        res = session.execute(query)
        result = res.unique().scalars().all()

        worker_1_resumes = result[0].resumes
        print(worker_1_resumes)

        worker_2_resumes = result[1].resumes
        print(worker_2_resumes)