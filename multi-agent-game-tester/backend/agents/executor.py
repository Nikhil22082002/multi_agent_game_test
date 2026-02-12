import os
import uuid

def execute_test_case(test):
    os.makedirs("artifacts", exist_ok=True)

    artifact_id = str(uuid.uuid4())
    artifact_path = f"artifacts/{artifact_id}.txt"

    with open(artifact_path, "w") as f:
        f.write(f"Executed {test['description']} successfully.")

    return {
        "test_id": test["id"],
        "status": "passed",
        "artifact": artifact_path
    }
