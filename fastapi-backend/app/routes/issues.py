from fastapi import   APIRouter, HTTPException, status
from uuid import uuid4

# Import Schemas
from app.schemas import Issue, IssueStatus, IssueCreate, IssueUpdate, IssuePriority

# Import Storage Functions
from app.storage import load_data, save_data


router = APIRouter(prefix="/api/v1/issues", tags=["issues"])

@router.get("/", response_model=list[Issue])
def get_issues():
    """ Get all issues """
    issues = load_data()
    return issues


@router.post("/", response_model=Issue, status_code=status.HTTP_201_CREATED)
def create_issue(issue: IssueCreate):
    """ Create a new issue """
    new_issue = {
        "id": str(uuid4()),
        "title": issue.title,
        "description": issue.description,
        "status": IssueStatus.open,
        "priority": issue.priority
    }

    issues = load_data()
    issues.append(new_issue)
    save_data(issues)
    return new_issue

@router.get("/{issue_id}", response_model=Issue)
def get_issue(issue_id: str):
    """
    Get single issue by ID
    Raises 404 if issue not found
    """
    issues = load_data()
    for issue in issues:
        if issue["id"] == issue_id:
            return issue
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="Issue not found")

    # """ Get a specific issue """
    # issues = load_data()
    # issue = next((issue for issue in issues if issue["id"] == issue_id), None)
    # if not issue:
    #     raise HTTPException(status_code=404, detail="Issue not found")
    # return issue

@router.put("/{issue_id}", response_model=Issue)
def update_issue(issue_id: str, issue_to_update: IssueUpdate):
    """Update an existing issue by ID."""
    issues = load_data()

    for issue in issues:
        if issue["id"] == issue_id:
            if issue_to_update.title is not None:
                issue["title"] = issue_to_update.title
            if issue_to_update.description is not None:
                issue["description"] = issue_to_update.description
            if issue_to_update.priority is not None:
                issue["priority"] = issue_to_update.priority.value
            if issue_to_update.status is not None:
                issue["status"] = issue_to_update.status.value

            save_data(issues)
            return issue

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Issue not found"
    )
    # """ Update an existing issue """
    # issues = load_data()
    # issue_to_update = next((issue for issue in issues if issue["id"] == issue_id), None)
    # if not issue_to_update:
    #     raise HTTPException(status_code=404, detail="Issue not found")
    # for field, value in issue.model_dump().items():
    #     issue_to_update[field] = value
    # save_data(issues)
    # return issue_to_update

@router.delete("/{issue_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_issue(issue_id: str):
    """Delete an issue by ID."""
    issues = load_data()

    for i, issue in enumerate(issues):
        if issue["id"] == issue_id:
            issues.pop(i)
            save_data(issues)
            return

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Issue not found"
    )




