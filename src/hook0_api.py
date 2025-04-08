# generated by borea

# if you want to edit this file, add it to ignores in borea.config.json, glob syntax

from typing import Any, Callable, Dict, Optional
import httpx

from .events_management.events_management import EventsManagement
from .user_authentication.user_authentication import UserAuthentication
from .applications_management.applications_management import ApplicationsManagement
from .service_tokens_management.service_tokens_management import ServiceTokensManagement
from .hook0.hook0 import Hook0
from .subscriptions_management.subscriptions_management import SubscriptionsManagement
from .organizations_management.organizations_management import OrganizationsManagement


class Hook0API:
    def __init__(
        self,
        base_url: str = "https://app.hook0.com",
        api_key: Optional[str] = None,
        timeout: float = 10.0,
        before_request: Optional[Callable[[httpx.Request], None]] = None,
        after_request: Optional[Callable[[httpx.Response], None]] = None,
    ):
        """
        Hook0 API

        Core REST API of Hook0 — Open-Source Webhooks as a service for SaaS

        Args:
            base_url: The base URL for API requests
            api_key: Optional API key for authentication
            timeout: Request timeout in seconds
            before_request: Optional callback before each request
            after_request: Optional callback after each request
        """
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.timeout = timeout
        self.before_request = before_request
        self.after_request = after_request
        self.client = httpx.Client(timeout=timeout)

        if api_key:
            self.client.headers.update({"Authorization": f"Bearer {api_key}"})

        self.events_management = EventsManagement(parent=self)
        self.user_authentication = UserAuthentication(parent=self)
        self.applications_management = ApplicationsManagement(parent=self)
        self.service_tokens_management = ServiceTokensManagement(parent=self)
        self.hook0 = Hook0(parent=self)
        self.subscriptions_management = SubscriptionsManagement(parent=self)
        self.organizations_management = OrganizationsManagement(parent=self)

    def _make_request(
        self,
        method: str,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        json_data: Optional[Dict[str, Any]] = None,
    ) -> httpx.Response:
        """Make an HTTP request.

        Args:
            method: HTTP method
            path: Request path
            params: Query parameters
            headers: Additional request headers
            json_data: JSON request body

        Returns:
            httpx.Response: The response from the server
        """
        url = f"{self.base_url}/{path.lstrip('/')}"

        # Merge any additional headers with existing ones
        request_headers = self.client.headers.copy()
        if headers:
            request_headers.update(headers)

        request = self.client.build_request(
            method=method,
            url=url,
            params=params,
            headers=request_headers,
            json=json_data,
        )

        if self.before_request:
            self.before_request(request)

        response = self.client.send(request)

        if self.after_request:
            self.after_request(response)

        response.raise_for_status()
        return response

    def close(self):
        """Close the HTTP client."""
        self.client.close()
