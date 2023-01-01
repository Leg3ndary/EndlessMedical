"""
Client
"""

import asyncio
from typing import Dict

import aiohttp

from . import session


class Client:
    """
    Client for accessing everything
    """

    def __init__(
        self, sesh: aiohttp.ClientSession = None, auto_accept: bool = False
    ) -> None:
        """
        Initiation of the client
        """
        self.sesh = sesh if sesh else aiohttp.ClientSession()
        self.loop: asyncio.BaseEventLoop = asyncio.get_event_loop()
        self.sessions: Dict[str, session.Session] = {}
        self.auto_accept = auto_accept

    async def request(self, method: str, url: str, **kwargs) -> Dict:
        """
        Make a request to the API
        """
        async with self.sesh.request(
            method, f"https://api.endlessmedical.com/v1/dx{url}", **kwargs
        ) as response:
            data = await response.json()
            return data

    async def close(self) -> None:
        """
        Close the client
        """
        await self.sesh.close()

    def clear_sessions(self) -> None:
        """
        Clear all medical sessions
        """
        self.sessions = {}

    async def create_session(self, default: bool = False) -> session.Session:
        """
        Create a session and return it
        """
        if default:
            return session.Session("default", default=True)
        response = await self.request("POST", "/InitSession")
        return session.Session(self.loop, response["SessionID"])
