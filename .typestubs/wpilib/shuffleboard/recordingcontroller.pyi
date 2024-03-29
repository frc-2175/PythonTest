"""
This type stub file was generated by pyright.
"""

from networktables.instance import NetworkTablesInstance
from .eventimportance import EventImportance

__all__ = ["RecordingController"]
class RecordingController:
    """Controls Shuffleboard recordings via NetworkTables."""
    kRecordingTableName = ...
    kRecordingControlKey = ...
    kRecordingFileNameFormatKey = ...
    kEventMarkerTableName = ...
    def __init__(self, ntInstance: NetworkTablesInstance) -> None:
        self.recordingControlEntry = ...
        self.recordingFileNameFormatEntry = ...
        self.eventsTable = ...
    
    def startRecording(self) -> None:
        ...
    
    def stopRecording(self) -> None:
        ...
    
    def setRecordingFileNameFormat(self, format: str) -> None:
        ...
    
    def clearRecordingFileNameFormat(self) -> None:
        ...
    
    def addEventMarker(self, name: str, description: str, importance: EventImportance):
        ...
    


