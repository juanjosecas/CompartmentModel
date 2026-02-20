import yaml
from typing import List, Dict
from pydantic import BaseModel, validator


class Flow(BaseModel):
    from_: str
    to: str
    rate: str


class ModelSchema(BaseModel):
    compartments: List[str]
    parameters: Dict[str, float]
    flows: List[Flow]
    initial_conditions: Dict[str, float]
    t_span: List[float]

    @validator("compartments")
    def unique_compartments(cls, v):
        if len(v) != len(set(v)):
            raise ValueError("Compartments must be unique")
        return v


def load_yaml(path: str) -> ModelSchema:
    with open(path) as f:
        data = yaml.safe_load(f)
    return ModelSchema(**data)