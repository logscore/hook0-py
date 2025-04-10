# generated by borea

# if you want to edit this file, add it to ignores in borea.config.json, glob syntax

# TODO: not implemented

from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from ...hook0_api import Hook0API


class ApplicationsCreate:
    def __init__(self, parent: "Hook0API"):
        self.parent = parent

    def applications_create(
        self,
        name: str,
        organization_id: str,
    ) -> Any:
        """
        Registers a new application within an organization. An application emits events that customers can subscribe to using webhooks.

        Args:
            name: No description provided
            organization_id: No description provided

        Returns:
            Response data
        """
        path = "/api/v1/applications/"
        params = None
        headers = None
        json_data = {
            "name": name if name is not None else None,
            "organization_id": organization_id if organization_id is not None else None,
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
