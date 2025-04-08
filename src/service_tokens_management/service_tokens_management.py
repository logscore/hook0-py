# generated by borea

# if you want to edit this file, add it to ignores in borea.config.json, glob syntax

from typing import TYPE_CHECKING

from .servicetoken_list.servicetoken_list import ServicetokenList
from .servicetoken_create.servicetoken_create import ServicetokenCreate
from .servicetoken_get.servicetoken_get import ServicetokenGet
from .servicetoken_edit.servicetoken_edit import ServicetokenEdit
from .servicetoken_delete.servicetoken_delete import ServicetokenDelete

if TYPE_CHECKING:
    from ..hook0_api import Hook0API


class ServiceTokensManagement:
    def __init__(self, parent: "Hook0API"):
        """


        Args:
            parent: The parent client to use for the requests
        """
        self.parent = parent

        self.servicetoken_list = ServicetokenList(parent=parent).servicetoken_list
        self.servicetoken_create = ServicetokenCreate(parent=parent).servicetoken_create
        self.servicetoken_get = ServicetokenGet(parent=parent).servicetoken_get
        self.servicetoken_edit = ServicetokenEdit(parent=parent).servicetoken_edit
        self.servicetoken_delete = ServicetokenDelete(parent=parent).servicetoken_delete
