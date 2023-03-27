from fastapi import APIRouter
from fastapi import Response
from fastapi import HTTPException

from lab4.server.db import Session
from lab4.server.repositories import CardRepository

from lab4.server.dto import CardDTO


card_repository = CardRepository(Session)
router = APIRouter()


@router.get("/cards")
def get_cards() -> list[CardDTO]:
    return card_repository.get_all()


@router.get("/cards/{id}")
def get_card_by_id(id: int) -> CardDTO:
    card = card_repository.get_by_id(id)
    if card is not None:
        return card
    else:
        raise HTTPException(
            status_code=404,
            detail=f"Resource Not Found. Card '{id}' could not be found."
        )


@router.get("/cards/by-number/{number}")
def get_card_by_number(number: str) -> CardDTO:
    card = card_repository.get_by_number(number)
    if card is not None:
        return card
    else:
        raise HTTPException(
            status_code=404,
            detail=f"Resource Not Found. Card '{number}' could not be found."
        )


@router.post("/cards")
def add_card(new_card: CardDTO) -> Response:
    card_repository.save(new_card)
    return Response(status_code=200)


@router.post("/cards/{id}")
def update_card(updated_card: CardDTO, id: int) -> Response:
    updated_card.id = id
    card_repository.update(updated_card)
    return Response(status_code=200)


@router.delete("/cards/{id}")
def delete_card(id: int) -> Response:
    card_repository.delete_by_id(id)
    return Response(status_code=200)
