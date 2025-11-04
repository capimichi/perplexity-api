from injector import inject
from fastapi import APIRouter, HTTPException, status


class ChatController:

    @inject
    def __init__(self):
        self.router = APIRouter(prefix="/s", tags=["Nones"])
        self._register_routes()
    
    def _register_routes(self):
        """Registra le rotte per il controller"""
        self.router.add_api_route("", self.get_s, methods=["GET"])
        self.router.add_api_route("/{_id}", self.get_, methods=["GET"])
        self.router.add_api_route("", self.create_, methods=["POST"])
        self.router.add_api_route("/{_id}", self.update_, methods=["PUT"])
        self.router.add_api_route("/{_id}", self.delete_, methods=["DELETE"])
    
    async def get_s(self):
        """Ottiene tutti i s"""
        # Implementazione provvisoria
        return {"s": []}
    
    async def get_(self, _id: str):
        """Ottiene un  specifico per ID"""
        # Implementazione provvisoria
        return {"_id": _id, "name": "None di esempio"}
    
    async def create_(self, _data: dict):
        """Crea un nuovo """
        # Implementazione provvisoria
        return {"message": "None creato con successo", "": _data}
    
    async def update_(self, _id: str, _data: dict):
        """Aggiorna un  esistente"""
        # Implementazione provvisoria
        return {"message": "None aggiornato con successo", "_id": _id}
    
    async def delete_(self, _id: str):
        """Elimina un """
        # Implementazione provvisoria
        return {"message": "None eliminato con successo", "_id": _id}