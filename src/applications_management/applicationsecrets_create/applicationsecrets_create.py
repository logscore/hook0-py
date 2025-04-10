# generated by borea

# if you want to edit this file, add it to ignores in borea.config.json, glob syntax

# TODO: not implemented

from typing import Any, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from ...hook0_api import Hook0API


class ApplicationsecretsCreate:
    def __init__(self, parent: "Hook0API"):
        self.parent = parent

    def applicationsecrets_create(
        self,
        application_id: str,
        name: Optional[str] = None,
    ) -> Any:
        """
        Generates a new API token for an application.

        Args:
            application_id: No description provided
            name: No description provided

        Returns:
            Response data
        """
        path = "/api/v1/application_secrets/"
        params = None
        headers = None
        json_data = {
            "application_id": application_id if application_id is not None else None,
            "name": name if name is not None else None,
        }
        json_data = {k: v for k, v in json_data.items() if v is not None}

        response = self.parent._make_request(
            method="POST",
            path=path,
            params=params,
            headers=headers,
            json_data=json_data,
        )
        return response.json()
