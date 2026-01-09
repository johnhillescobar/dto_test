from langchain.tools import BaseTool
from pydantic import BaseModel, Field
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class CelsiusToFarenheit(BaseModel):
    celsius: float | None = Field(description="The temperature in Celsius")


class CelsiusToFarenheitTool(BaseTool):
    """Convert Celsius to Farenheit"""

    name: str = "celsius_to_farenheit"
    description: str = "Convert Celsius to Farenheit"

    def _run(self, celsius: float) -> float:
        logger.info(f"Converting Celsius to Farenheit: {celsius}")
        if celsius is None:
            raise ValueError("Celsius is required")

        farenheit = (celsius * 9 / 5) + 32

        logger.info(f"Farenheit: {farenheit}")
        return farenheit

    async def _arun(self, celsius: float) -> float:
        logger.info(f"Converting Celsius to Farenheit: {celsius}")
        if celsius is None:
            raise ValueError("Celsius is required")

        farenheit = (celsius * 9 / 5) + 32

        logger.info(f"Farenheit: {farenheit}")
        return farenheit
