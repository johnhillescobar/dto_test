from langchain.tools import BaseTool
from pydantic import BaseModel, Field
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class MetersToFeet(BaseModel):
    meters: float | None = Field(description="The length in meters")
    kilometers: float | None = Field(description="The length in kilometers")
    expressed_in_kilometers: bool | None = Field(
        description="If True, the length is expressed in kilometers, if False, the length is expressed in meters"
    )
    expressed_in_meters: bool | None = Field(
        description="If True, the length is expressed in meters, if False, the length is expressed in kilometers"
    )


class MetersToFeetTool(BaseTool):
    """Convert Meters to Feet"""

    name: str = "meters_to_feet"
    description: str = "Convert Meters to Feet"

    def _run(
        self,
        meters: float,
        kilometers: float,
        expressed_in_kilometers: bool = False,
        expressed_in_meters: bool = False,
    ) -> float:
        logger.info(f"Converting Meters to Feet: {meters}")

        if meters is not None:
            feet = meters * 3.28084

            if expressed_in_kilometers:
                feet = feet / 1.60934

            logger.info(f"Feet: {feet}")
            return feet

        elif kilometers is not None:
            meters = kilometers * 1000

            if expressed_in_meters:
                meters = meters / 3.28084

            logger.info(f"Meters: {meters}")
            return meters

        else:
            raise ValueError("Meters or Kilometers is required")

    async def _arun(
        self,
        meters: float,
        kilometers: float,
        expressed_in_kilometers: bool = False,
        expressed_in_meters: bool = False,
    ) -> float:
        logger.info(f"Converting Meters to Feet: {meters}")

        if meters is not None:
            feet = meters * 3.28084

            if expressed_in_kilometers:
                feet = feet / 1.60934

            logger.info(f"Feet: {feet}")
            return feet

        elif kilometers is not None:
            meters = kilometers * 1000

            if expressed_in_meters:
                meters = meters / 3.28084

            logger.info(f"Meters: {meters}")
            return meters

        else:
            raise ValueError("Meters or Kilometers is required")
