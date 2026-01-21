from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional

class IssueStatus(str, Enum):
    open = "open"
    in_progress = "in progress"
    closed = "closed"

class IssuePriority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"

class IssueCreate(BaseModel):
    title: str = Field(..., min_length=3, max_length=255)
    # description: Optional[str] = None
    description: str = Field(..., min_length=5, max_length=1000)
    # status: IssueStatus = IssueStatus.open
    priority: IssuePriority = IssuePriority.medium

class IssueUpdate(BaseModel):
    title: Optional[str] = Field(default=None, min_length=3, max_length=255)
    description: Optional[str] = Field(default=None, min_length=5, max_length=1000)
    priority: Optional[IssuePriority] = Field(default=None)
    status: Optional[IssueStatus] = Field(default=None)

class Issue(BaseModel):
    id: str
    status: IssueStatus
    priority: IssuePriority
    title: str
    description: str

