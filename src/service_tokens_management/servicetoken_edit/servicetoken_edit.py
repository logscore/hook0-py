# generated by borea

# if you want to edit this file, add it to ignores in borea.config.json, glob syntax

# TODO: not implemented

from typing import Any, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from ...hook0_api import Hook0API


class ServicetokenEdit:
    def __init__(self, parent: "Hook0API"):
        self.parent = parent

    def servicetoken_edit(
        self,
        service_token_id: str,
        request_body: Optional[ServiceTokenPost] = None,
    ) -> Any:
        """
        Updates the name of an existing service token. The token must belong to the specified organization and still be active (not expired or revoked).

        Args:
            service_token_id:
            request_body: Request body

        Returns:
            Response data
        """
        path = f"/api/v1/service_token/{service_token_id}"
        params = {}
        headers = {}
        json_data = request_body.model_dump() if request_body else None

        response = self.parent._make_request(
            method="PUT",
            path=path,
            params=params,
            headers=headers,
            json_data=json_data,
        )
        return response.json()
