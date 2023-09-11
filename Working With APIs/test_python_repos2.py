import requests
import responses  # Import the responses library

# Test the status code.
def test_status_code():
    # Mock the API response with a custom total_count
    responses.add(
        responses.GET,
        "https://api.github.com/search/repositories",
        json={"total_count": 500},  # Adjust the value as needed
        status=200,
    )

    # Make an API call and store the response.
    url = "https://api.github.com/search/repositories"
    url += "?q=language:python+sort:stars+stars:>10000"
    headers = {"Accept": "application/vnd.github.v3+json"}
    response = requests.get(url, headers=headers)

    assert response.status_code == 200

# Test the total number of repositories.
def test_total_repositories():
    # Mock the API response with a custom total_count
    responses.add(
    responses.GET,
    "https://api.github.com/search/repositories",
    json={"total_count": 1500},  # Adjust the value as needed
    status=200,
)


    # Make an API call and store the response.
    url = "https://api.github.com/search/repositories"
    url += "?q=language:python+sort:stars+stars:>10000"
    headers = {"Accept": "application/vnd.github.v3+json"}
    response = requests.get(url, headers=headers)

    response_dict = response.json()
    total_count = response_dict['total_count']
    assert total_count >= 402  # Adjust the threshold as needed

# Test the completeness of results.
def test_incomplete_results():
    # Mock the API response with a custom total_count
    responses.add(
        responses.GET,
        "https://api.github.com/search/repositories",
        json={"total_count": 500},  # Adjust the value as needed
        status=200,
    )

    # Make an API call and store the response.
    url = "https://api.github.com/search/repositories"
    url += "?q=language:python+sort:stars+stars:>10000"
    headers = {"Accept": "application/vnd.github.v3+json"}
    response = requests.get(url, headers=headers)

    response_dict = response.json()
    assert not response_dict['incomplete_results']

# Test the number of repositories returned.
def test_repositories_count():
    # Mock the API response with a custom total_count
    responses.add(
        responses.GET,
        "https://api.github.com/search/repositories",
        json={"total_count": 500},  # Adjust the value as needed
        status=200,
    )

    # Make an API call and store the response.
    url = "https://api.github.com/search/repositories"
    url += "?q=language:python+sort:stars+stars:>10000"
    headers = {"Accept": "application/vnd.github.v3+json"}
    response = requests.get(url, headers=headers)

    response_dict = response.json()
    repo_dicts = response_dict['items']
    assert len(repo_dicts) > 0

# Test selected information about the first repository.
def test_first_repository_info():
    # Mock the API response with a custom total_count
    responses.add(
        responses.GET,
        "https://api.github.com/search/repositories",
        json={"total_count": 500},  # Adjust the value as needed
        status=200,
    )

    # Make an API call and store the response.
    url = "https://api.github.com/search/repositories"
    url += "?q=language:python+sort:stars+stars:>10000"
    headers = {"Accept": "application/vnd.github.v3+json"}
    response = requests.get(url, headers=headers)

    response_dict = response.json()
    repo_dicts = response_dict['items']

    if repo_dicts:
        first_repo = repo_dicts[0]  # Get the first repository if available
        assert 'name' in first_repo
        assert 'owner' in first_repo
        assert 'stargazers_count' in first_repo
        assert 'html_url' in first_repo
        assert 'created_at' in first_repo
        assert 'updated_at' in first_repo
        assert 'description' in first_repo

# Test the presence of Python-related keywords in the response.
def test_python_keywords():
    # Mock the API response with a custom total_count
    responses.add(
        responses.GET,
        "https://api.github.com/search/repositories",
        json={"total_count": 500},  # Adjust the value as needed
        status=200,
    )

    # Make an API call and store the response.
    url = "https://api.github.com/search/repositories"
    url += "?q=language:python+sort:stars+stars:>10000"
    headers = {"Accept": "application/vnd.github.v3+json"}
    response = requests.get(url, headers=headers)

    response_dict = response.json()
    repo_dicts = response_dict['items']
    python_keywords = ['python', 'Py', 'Pythonic']  # Add more relevant keywords
    found_python_repo = any(
        any(keyword.lower() in repo['name'].lower() for keyword in python_keywords)
        for repo in repo_dicts
    )
    assert found_python_repo
