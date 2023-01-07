"""
Session information
"""

import asyncio
import aiohttp
from typing import Dict


class Session:
    """
    Session information
    """

    def __init__(
        self,
        sesh: aiohttp.ClientSession,
        loop: asyncio.BaseEventLoop,
        session_id: str,
        default: bool,
        auto_accept: bool = False,
    ) -> None:
        """
        Initiation of the session
        """
        self.session_id = session_id
        self.default = default
        self.symptoms: Dict[str, str] = {}
        if auto_accept:
            loop.run_in_executor(None, self.accept_terms_of_use)

    async def request(self, method: str, url: str, **kwargs) -> Dict:
        """
        Make a request to the API
        """
        async with self.sesh.request(
            method, f"https://api.endlessmedical.com/v1/dx{url}", **kwargs
        ) as response:
            data = await response.json()
            return data

    async def accept_terms_of_use(self) -> None:
        """
        Accept the terms of use
        """
        data = await self.request(
            "POST",
            "/AcceptTermsOfUse",
            params={
                "SessionID": self.session_id,
                "passphrase": "I have read, understood and I accept and agree to comply with the Terms of Use of EndlessMedicalAPI and Endless Medical services. The Terms of Use are available on endlessmedical.com"
            },
        )
        if data["status"] != "ok":
            raise Exception("Failed to accept terms of use")

    async def add_feature(self, feature: str) -> None:
        """
        Add a feature
        """
