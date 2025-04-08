# generated by borea

# if you want to edit this file, add it to ignores in borea.config.json, glob syntax

# TODO: not implemented

from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from ...hook0_api import Hook0API


class SubscriptionsDelete:
    def __init__(self, parent: "Hook0API"):
        self.parent = parent

    def subscriptions_delete(
        self,
        subscription_id: str,
        application_id: str,
    ) -> Any:
        """
        Marks a subscription as deleted, preventing any further event notifications from being sent. This operation is irreversible.

        Args:
            subscription_id:
            application_id:

        Returns:
            Response data
        """
        path = f"/api/v1/subscriptions/{subscription_id}"
        params = {}
        headers = {}
        if application_id is not None:
            params["application_id"] = application_id
        json_data = None

        response = self.parent._make_request(
            method="DELETE",
            path=path,
            params=params,
            headers=headers,
            json_data=json_data,
        )
        return response.json()
