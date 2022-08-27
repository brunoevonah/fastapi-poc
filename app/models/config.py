from pydantic import BaseModel


class Health(BaseModel):
    # TODO use the healthcheck factory
    status: str = "App running"


# from fastapi import FastAPI
# from fastapi_healthcheck import HealthCheckFactory, healthCheckRoute

# app = FastAPI()

# # Add Health Checks
# _healthChecks = HealthCheckFactory()

# # This will check external URI and validate the response that is returned.
# # fastapi-healthcheck-uri
# _healthChecks.add(HealthCheckUri(alias='reddit',
# connectionUri="https://www.reddit.com/r/aww.json", tags=('external', 'reddit', 'aww')))
# app.add_api_route('/health', endpoint=healthCheckRoute(factory=_healthChecks))
