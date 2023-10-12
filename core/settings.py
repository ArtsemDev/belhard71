from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    db_url = "db.slite3"


print(__name__)
