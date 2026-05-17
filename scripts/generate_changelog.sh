#!/bin/bash
# scripts/generate_changelog.sh
# Usage: ./generate_changelog.sh [from_tag] [to_tag]

FROM_TAG=$1
TO_TAG=$2

if [ -z "$FROM_TAG" ]; then
    FROM_TAG=$(git describe --tags --abbrev=0 2>/dev/null || git rev-list --max-parents=0 HEAD)
fi

if [ -z "$TO_TAG" ]; then
    TO_TAG="HEAD"
fi

echo "# CHANGELOG"
echo ""
echo "## [Unreleased] - $(date +%Y-%m-%d)"
echo ""

echo "### Features"
git log "$FROM_TAG..$TO_TAG" --oneline --pretty=format:"* %s" --grep="feat:" | sed 's/feat: //'
echo ""

echo "### Fixes"
git log "$FROM_TAG..$TO_TAG" --oneline --pretty=format:"* %s" --grep="fix:" | sed 's/fix: //'
echo ""

echo "### Documentation"
git log "$FROM_TAG..$TO_TAG" --oneline --pretty=format:"* %s" --grep="docs:" | sed 's/docs: //'
echo ""

echo "### Others"
git log "$FROM_TAG..$TO_TAG" --oneline --pretty=format:"* %s" --invert-grep --grep="feat:\|fix:\|docs:"
