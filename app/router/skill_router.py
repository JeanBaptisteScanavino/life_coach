from core.schemas.Skill import Skill, SkillStatus
from fastapi import APIRouter

skill_router = APIRouter(
    prefix="/skill",
    tags=["skill"],
)


@skill_router.get("/")
def get_all_skill():
    return {"skill": {"cat 1": ["1", "2"], "cat 2": ["voila", "aitre"]}}


# @skill_router.get("/{id}")
# def get_one_skill(id: int):
#     return {"skill": id}


@skill_router.post("/")
def create_skill(value: str, category_id: int, month_id: int):
    # create use case new skill
    new_skill = Skill(value=value, category_id=category_id, month_id=month_id)
    return {"skill": new_skill}


@skill_router.put("/{id}")
def update_skill(id: int, status: SkillStatus):
    # Use case Update status
    return {"skill": status}


@skill_router.get("/{id}/delete")
def desactivate_skill(id: int):
    # skill.active = false
    return {"skill": "is deleted"}
