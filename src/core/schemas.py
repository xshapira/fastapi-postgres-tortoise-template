from tortoise.contrib.pydantic import pydantic_model_creator
from pydantic import BaseModel


class AppSchema(BaseModel):
    pass


class Status(AppSchema):
    message: str


# def generate_app_schema(
#     model: tortoise.models.Model,
#     name: str,
#     exclude_readonly: bool = False,
#     exclude: Tuple[str, ...] = (),

# ) -> BaseModel:
#     pydantic_model: BaseModel = pydantic_model_creator(
#         model,
#         exclude=exclude,
#         exclude_readonly=exclude_readonly
#     )

#     pydantic_app_model = type(
#         name,
#         (pydantic_model, AppSchema)
#     )
