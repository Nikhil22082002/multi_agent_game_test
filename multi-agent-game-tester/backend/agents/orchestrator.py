from agents.planner import generate_test_cases
from agents.ranker import rank_test_cases
from agents.executor import execute_test_case
from agents.analyzer import analyze_results

def run_test_pipeline(url: str):
    test_cases = generate_test_cases(url)
    ranked = rank_test_cases(test_cases)
    selected = ranked[:10]

    executions = []
    for test in selected:
        executions.append(execute_test_case(test))

    analysis = analyze_results(executions)

    return {
        "target_url": url,
        "generated_tests": len(test_cases),
        "executed_tests": len(selected),
        "results": analysis
    }
