comment_body=$(curl https://api.travis-ci.com/v3/job/${TRAVIS_JOB_ID}/log.txt | sed -n 's/^pylint-response://p')
curl -H "Authorization: token ${GITHUB_ACCESS_TOKEN}" -X POST \
-d "{\"body\": \'$comment_body\'}" \
"https://api.github.com/repos/${TRAVIS_REPO_SLUG}/issues/${TRAVIS_PULL_REQUEST}/comments"
