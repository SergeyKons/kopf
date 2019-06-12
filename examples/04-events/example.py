"""
Send the custom events for the handled or other objects.
"""
import asyncio

import kopf


@kopf.on.create('zalando.org', 'v1', 'kopfexamples')
def create_fn(body, **kwargs):

    asyncio.wait([
        # The all-purpose function for the vent creation.
        kopf.event(body, type="SomeType", reason="SomeReason", message="Some message"),

        # The shortcuts for the conventional events and common cases.
        kopf.info(body, reason="SomeReason", message="Some message"),
        kopf.warn(body, reason="SomeReason", message="Some message"),
    ])

    try:
        raise RuntimeError("Exception text.")
    except:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(kopf.exception(body, reason="SomeReason", message="Some exception:"))
