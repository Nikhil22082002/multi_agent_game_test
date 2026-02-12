from fastapi import FastAPI
from agents.orchestrator import run_test_pipeline
from report_writer import write_report
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Multi-Agent Game Tester POC")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/run")
def run_tests():
    """
    Trigger the multi-agent test pipeline
    """
    url = "https://play.ezygamers.com/"

    result = run_test_pipeline(url)

    write_report(result)

    return result


@app.get("/")
def health():
    return {"status": "ok"}
