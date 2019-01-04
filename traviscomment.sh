# curl -H "Authorization: token ${GITHUB_ACCESS_TOKEN}" -X POST \
# -d "{\"body\": \"Hello world\"}" \
# "https://api.github.com/repos/${TRAVIS_REPO_SLUG}/issues/${TRAVIS_PULL_REQUEST}/comments"
echo ${TRAVIS_JOB_WEB_URL}
