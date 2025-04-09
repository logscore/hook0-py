from datetime import datetime, timezone
import os
from hook0.src.hook0_api import Hook0API
import uuid



HOOK0_KEY='71fb7ad4-af37-4ba0-84fb-326b7031dad3'
HOOK0_APP_ID='9d6d0dd6-dbd0-4f96-b655-7fdec72d6255'
UUID1=str(uuid.uuid4())
UUID2=str(uuid.uuid4())
print(UUID1)

now = datetime.now(timezone.utc)
time = now.isoformat().replace('+00:00', 'Z')

client = Hook0API(api_key=HOOK0_KEY, timeout=10)

new_event_type = client.events_management.eventtypes_create(HOOK0_APP_ID, "account", "auth", "created")
print("CREATED NEW EVENT TYPE:", new_event_type)

new_event = client.events_management.events_ingest(HOOK0_APP_ID, UUID1, "auth.account.created", {"all": "yes"}, "2025-04-09T02:23:33.000000Z", '{"message": "Is this thing on?"}', "application/json")
print("CREATED NEW EVENT:", new_event)

new_subcription = client.subscriptions_management.subscriptions_create(HOOK0_APP_ID, ["auth.account.created"], True, "all", "yes", {"headers": { "header": "value" }, "type": "http", "url": "https://webhook.site/d30cd100-189c-41c0-8c0a-d06a510cb738", "method": "GET"})
print("CREATED NEW SUBSCRIPTION:", new_subcription)

new_subscription_event = client.events_management.events_ingest(HOOK0_APP_ID, UUID2, "auth.account.created", {"all": "yes"}, "2025-04-09T02:33:33.000000Z", '{"message": "Ship Faster with Borea!"}', "application/json")
print("CREATED NEW SUBSCRIBED EVENT:", new_subscription_event)