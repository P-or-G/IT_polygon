import reflex as rx

config = rx.Config(
    app_name="prdprf",
    db_url="sqlite:///reflex.db",
    backend_host="localhost",
    telemetry_enabled=False,
)
