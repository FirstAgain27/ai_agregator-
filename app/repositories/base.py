from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import Generic, Type, TypeVar, Sequence, Optional 


ModelType = TypeVar("ModelType")

class BaseRepository(Generic[ModelType]):
    # Type[ModelType] нужно для гибкого поведения класса. 
    # Грубо говоря - передаём не сам объект класса, а определяем класс и уже его тип берем в конструктор. 
    def __init__(self, model: Type[ModelType], session: AsyncSession) -> None:
        self.session = session
        self.model = model

    async def get_by_id(self, id: int) -> Optional[ModelType]:
        result = await self.session.get(self.model, id)
        return result

    async def add(self, entity: ModelType) -> ModelType:
        self.session.add(entity)
        await self.session.flush()
        return entity
    
    async def delete(self, entity: ModelType) -> ModelType:
        await self.session.delete(entity)
        await self.session.flush()
        return entity

    async def delete_by_id(self, id: int) -> bool:
        entity = await self.get_by_id(id)
        if entity is not None:
            await self.session.delete(entity)
            return True 
        return False

