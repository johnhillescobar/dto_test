from langchain.tools import BaseTool
from pydantic import BaseModel, Field
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class FeetToMeters(BaseModel):
    feet: float | None = Field(description="The length in feet")
    miles: float | None = Field(description="The length in miles")
    expressed_in_miles: bool | None = Field(
        description="If True, the length is expressed in miles, if False, the length is expressed in feet"
    )
    expressed_in_feet: bool | None = Field(
        description="If True, the length is expressed in feet, if False, the length is expressed in miles"
    )


class FeetToMetersTool(BaseTool):
    """Convert Feet to Meters"""

    name: str = "feet_to_meters"
    description: str = "Convert Feet to Meters"

    def _run(
        self,
        feet: float,
        miles: float,
        expressed_in_miles: bool = False,
        expressed_in_feet: bool = False,
    ) -> float:
        logger.info(f"Converting Feet to Meters: {feet}")

        if feet is not None:
            meters = feet * 0.3048

            if expressed_in_miles:
                meters = meters / 1609.34

            logger.info(f"Meters: {meters}")
            return meters

        elif miles is not None:
            kilometers = miles * 1.60934

            if expressed_in_feet:
                kilometers = kilometers * 0.621371

            logger.info(f"Kilometers: {kilometers}")
            return kilometers

        else:
            raise ValueError("Feet or Miles is required")

    async def _arun(
        self,
        feet: float,
        miles: float,
        expressed_in_miles: bool = False,
        expressed_in_feet: bool = False,
    ) -> float:
        logger.info(f"Converting Feet to Meters: {feet}")

        if feet is not None:
            meters = feet * 0.3048

            if expressed_in_miles:
                meters = meters / 1609.34

            logger.info(f"Meters: {meters}")
            return meters

        elif miles is not None:
            kilometers = miles * 1.60934

            if expressed_in_feet:
                kilometers = kilometers * 0.621371

            logger.info(f"Kilometers: {kilometers}")
            return kilometers

        else:
            raise ValueError("Feet or Miles is required")
