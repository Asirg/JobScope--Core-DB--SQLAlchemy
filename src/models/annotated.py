from typing import Annotated
from sqlalchemy.orm import mapped_column
from sqlalchemy import text, String

import datetime



intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]
updated_at = Annotated[datetime.datetime, mapped_column(
        server_default=text("TIMEZONE('utc', now())"),
        onupdate=datetime.datetime.now(datetime.timezone.utc)
)]


str_256 = Annotated[str, mapped_column(String(256))]