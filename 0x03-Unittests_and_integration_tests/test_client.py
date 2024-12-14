#!/usr/bin/env python3
#!/usr/bin/env python5
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient."""

    @classmethod
    def setUpClass(cls):
        """Set up mock responses for requests.get."""
        cls.get_patcher = patch(
                "requests.get", side_effect=cls.get_mock_response
                )
        cls.mock_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """Stop the patcher."""
        cls.get_patcher.stop()

    @staticmethod
    def get_mock_response(url):
        """Mock the response for requests.get."""
        if url.endswith("orgs/google"):
            return Mock(
                    json=lambda: TestIntegrationGithubOrgClient.org_payload
                    )
        elif url.endswith("orgs/google/repos"):
            return Mock(
                    json=lambda: TestIntegrationGithubOrgClient.repos_payload
                    )
        return Mock(json=lambda: {})

    def test_public_repos(self):
        """Test the public_repos method."""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """Test the public_repos method with a license filter."""
        client = GithubOrgClient("google")
        self.assertEqual(
            client.public_repos(license="apache-2.0"), self.apache2_repos
        )
