def generate_test_cases(url: str):
    test_cases = []
    for i in range(1, 21):
        test_cases.append({
            "id": i,
            "description": f"Test case {i}: Validate puzzle interaction",
            "url": url
        })
    return test_cases
