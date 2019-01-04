curl -H "Authorization: token 01998876ff1a26f37b3a0a39d5a3840913f230ec" -X POST \
-d "{\"body\": \"Hello world\"}" \
"https://api.github.com/repos/${TRAVIS_REPO_SLUG}/issues/${TRAVIS_PULL_REQUEST}/comments"
