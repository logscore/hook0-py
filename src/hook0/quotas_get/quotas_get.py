# generated by borea

# if you want to edit this file, add it to ignores in borea.config.json, glob syntax

# TODO: not implemented

from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from ...hook0_api import Hook0API


class QuotasGet:
    def __init__(self, parent: "Hook0API"):
        self.parent = parent

    def quotas_get(
        self,
    ) -> Any:
        """
        Get the current quotas limitations on the instance.

        Returns:
            Response data
        """
        path = "/api/v1/quotas/"
        params = None
        headers = None
        json_data = None

        response = self.parent._make_request(
            method="GET",
            path=path,
            params=params,
            headers=headers,
            json_data=json_data,
        )
        return response.json()
