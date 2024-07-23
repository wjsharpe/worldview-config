from datetime import datetime

from pydantic import BaseModel, Field, RootModel


class LayerConfig(BaseModel):
    id: str
    satellite: str
    instrument: str
    measurement: str
    discipline: str
    title: str
    format: str
    colormap_id: str
    matrix_set: str
    source_name: str
    arctic_matrix_set: str | None = Field(default=None)
    arctic_source_name: str | None = Field(default=None)
    antarctic_matrix_set: str | None = Field(default=None)
    antarctic_source_name: str | None = Field(default=None)
    start_date: datetime
    group: str = Field(default="overlays")
    description: str = Field(default="")
    tags: list[str] = Field(default=[])
    period: str | None = Field(default="daily")
    end_date: datetime | None = Field(default=None)
    temporal_start: datetime | None = Field(default=None)
    temporal_end: datetime | None = Field(default=None)
    date_interval: int | None = Field(default=None)


class LayerConfigs(RootModel):
    root: list[LayerConfig]
