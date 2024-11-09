from dataclasses import dataclass
from typing import Callable, Any

@dataclass
class Event:
    _type: str
    _sender: object
    _params: dict
    def __init__(self, type: str, sender: object, params: dict[str, Any] = {}) -> None:
        self._type = type
        self._sender = sender
        self._params = params
    
    def get_type(self) -> str:
        return self._type
    

    def get_sender(self) -> object: 
        return self._sender
    
    def get_params(self) -> dict:
        return self._params


class EventEmitter:
    _listeners: list[dict[str, Callable[[Event], None]]]
    _lazy_check: bool

    def __init__(self, lazy_check = False) -> None:
        self._listeners = []
        self._lazy_check = lazy_check

    @classmethod
    def initialize(cls, lazy_check = False) -> "EventEmitter":
        return cls(lazy_check = lazy_check)


    def has_listener(self, type: str, listener: Callable[[Event], None] | None = None) -> bool:
        if listener != None:
            for item in self._listeners:
                if item["type"] == type and item["listener"] == listener:
                    return True
        else:
            for item in self._listeners:
                if item["type"] == type:
                    return True 
        return False
    

    def on(self, type: str, listener: Callable[[Event], None]) -> bool:
        if self._lazy_check == False:
            if not self.has_listener(type, listener):
                self._listeners.append({"type": type, "listener": listener})
                return True
        else:
            if not self.has_listener(type):
                self._listeners.append({"type": type, "listener": listener})
                return True
        return False
    

    def off(self, type: str, listener: Callable[[Event], None]) -> bool:
        if self._lazy_check == False:
            if self.has_listener(type, listener):
                # i = 0
                # while(i < len(self._listeners)):
                #     if self._listeners[i]["type"] == type and self._listeners[i]["listener"] == listener:
                #         del self._listeners[i]
                #     i += 1
                for item in self._listeners:
                    if item["type"] == type and item["listener"] == listener:
                        self._listeners.remove(item)
                        return True
        else:
            if self.has_listener(type):
                for item in self._listeners:
                    if item["type"] == type:
                        self._listeners.remove(item)
                        return True

        return False
    

    def emit(self, event: Event) -> bool:
        ret = False
        for item in self._listeners:
            if item["type"] == event.get_type():
                item["listener"](event)
                ret = True
        return ret

    

    def get_listeners(self) -> list:
        return self._listeners
    

    def get_lazy_check(self) -> bool:
        return self._lazy_check
    
    def set_lazy_check(self, value: bool) -> None:
        self._lazy_check = value
    

    def __str__(self) -> str:
        return f"EventEmitter(_listeners={self.get_listeners()})"
    
    def __repr__(self) -> str:
        return self.__str__()