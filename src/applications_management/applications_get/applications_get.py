# generated by borea

# if you want to edit this file, add it to ignores in borea.config.json, glob syntax

# TODO: not implemented

from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from ...hook0_api import Hook0API


class ApplicationsGet:
    def __init__(self, parent: "Hook0API"):
        self.parent = parent

    def applications_get(
        self,
        application_id: str,
    ) -> Any:
        """
        Retrieves details about a specific application, including quotas and consumption statistics.

        Args:
            application_id:

        Returns:
            Response data
        """
        path = f"/api/v1/applications/{application_id}"
        params = {}
        headers = {}
        json_data = None

        response = self.parent._make_request(
            method="GET",
            path=path,
            params=params,
            headers=headers,
            json_data=json_data,
        )
        return response.json()
