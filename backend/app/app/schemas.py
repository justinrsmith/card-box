from pydantic import BaseModel


class CardBase(BaseModel):
    player_name: str
    year: int


class CardCreate(CardBase):
    pass


class Card(CardBase):
    id: int

    class Config:
        orm_mode = True  # TODO: what is this for
