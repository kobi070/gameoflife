from dataclasses import dataclass


@dataclass
class Config:
    """Defines the params we allow the user to change in the game settings"""

    width: int
    height: int
    threshhold: float
    lifecycle: int
    living_ch: chr

    def setSize(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def setThreshold(self, th: float) -> None:
        self.threshhold = th

    def setLifecycle(self, lfc: int) -> None:
        self.lifecycle = lfc

    def setLiveCh(self, liveCh: chr) -> None:
        self.living_ch = liveCh
