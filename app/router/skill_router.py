from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.repository.skill import SkillRepository
from core.use_case.skill.create import CreateSkill
from core.use_case.skill.delete import DeleteSkill
from core.use_case.skill.get_all import GetAllSkill
from core.use_case.skill.update import UpdateSkill
from database.models.Skill import Skill
from database.database import get_db

from core.schemas.Skill import SkillSchema

skill_router = APIRouter(
    prefix="/skill",
    tags=["skill"],
)
dependencies = {}
dependencies["skill_repository"] = SkillRepository
dependencies["skill_model"] = Skill

@skill_router.get("/")
def get_all_skill(db: Session = Depends(get_db)):
    dependencies["db"] = db
    skills = GetAllSkill(dependencies).execute()
    return {"skill": skills}


# @skill_router.get("/{id}")
# def get_one_skill(id: int):
#     return {"skill": id}


@skill_router.post("/")
def create_skill(skill: SkillSchema, db: Session = Depends(get_db)):
    # create use case new skill
    dependencies["db"] = db
    new_skill = CreateSkill(dependencies).execute(skill)
    return {"skill": new_skill}


@skill_router.put("/{id}")
def update_skill(id: int, skill: SkillSchema, db: Session = Depends(get_db)):
    # Use case Update status
    dependencies["db"] = db
    updated_skill = UpdateSkill(dependencies).execute(id, skill)
    return {"skill": updated_skill}


@skill_router.get("/{id}/delete")
def delete_skill(id: int, db: Session = Depends(get_db)):
    # skill.active = false
    dependencies["db"] = db
    try:
        DeleteSkill(dependencies).execute(id)
        return {"waiting_list": "IS_DELETED"}
    except Exception:
        return Exception
