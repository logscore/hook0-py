# generated by borea

# if you want to edit this file, add it to ignores in borea.config.json, glob syntax

# TODO: not implemented

from typing import Any, List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from ...hook0_api import Hook0API


class SubscriptionsCreate:
    def __init__(self, parent: "Hook0API"):
        self.parent = parent

    def subscriptions_create(
        self,
        application_id: str,
        event_types: List[str],
        is_enabled: bool,
        label_key: str,
        label_value: str,
        target: Any,
        dedicated_workers: Optional[List[str]] = None,
        description: Optional[str] = None,
        metadata: Optional[Any] = None,
    ) -> Any:
        """
        Creates a new event subscription for an application. This allows clients to receive event notifications via a webhook or another defined target.

        Args:
            application_id: No description provided
            event_types: No description provided
            is_enabled: No description provided
            label_key: No description provided
            label_value: No description provided
            target: No description provided
            dedicated_workers: No description provided
            description: No description provided
            metadata: No description provided

        Returns:
            Response data
        """
        path = "/api/v1/subscriptions/"
        params = None
        headers = None
        json_data = {
            "application_id": application_id if application_id is not None else None,
            "dedicated_workers": dedicated_workers
            if dedicated_workers is not None
            else None,
            "description": description if description is not None else None,
            "event_types": event_types if event_types is not None else None,
            "is_enabled": is_enabled if is_enabled is not None else None,
            "label_key": label_key if label_key is not None else None,
            "label_value": label_value if label_value is not None else None,
            "metadata": metadata if metadata is not None else None,
            "target": target if target is not None else None,
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
