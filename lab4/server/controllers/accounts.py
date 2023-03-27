from fastapi import APIRouter
from fastapi import Response
from fastapi import HTTPException

from lab4.server.db import Session
from lab4.server.repositories import CardAccountRepository

from lab4.server.dto import CardAccountDTO


card_account_repository = CardAccountRepository(Session)
router = APIRouter()


@router.get("/accounts")
def get_accounts() -> list[CardAccountDTO]:
    return card_account_repository.get_all()


@router.get("/accounts/{id}")
def get_account_by_id(id: int) -> CardAccountDTO:
    account = card_account_repository.get_by_id(id)
    if account is not None:
        return account
    else:
        raise HTTPException(
            status_code=404,
            detail=f"Resource Not Found. Account '{id}' could not be found."
        )


@router.post("/accounts")
def add_accounts(new_account: CardAccountDTO) -> Response:
    card_account_repository.save(new_account)
    return Response(status_code=200)


@router.post("/accounts/{id}")
def update_account(updated_account: CardAccountDTO, id: int) -> Response:
    updated_account.id = id
    card_account_repository.update(updated_account)
    return Response(status_code=200)


@router.delete("/accounts/{id}")
def delete_account(id: int) -> Response:
    card_account_repository.delete_by_id(id)
    return Response(status_code=200)
