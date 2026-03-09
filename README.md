Invalidate CloudFront to update domain routing:

https://us-east-1.console.aws.amazon.com/cloudfront/v4/home?region=us-east-1#/distributions

https://stackoverflow.com/questions/30154461/aws-cloudfront-not-updating-on-update-of-files-in-s3

# CloudFront Invalidation Setup

I've created the CloudFront invalidation setup. Here's what was created:

Files Created
post-push - A standalone invalidation script
git-push-deploy - A wrapper script that does push + invalidation
Usage
You can now deploy with CloudFront invalidation in two ways:

Option 1: Git alias (recommended)

Option 2: Direct script

Requirements
Make sure AWS CLI is installed and configured with credentials that have cloudfront:CreateInvalidation permission:

Note: Git doesn't have a native post-push hook, so the git deploy alias is the cleanest way to automatically invalidate after pushing. If you want a true automatic approach, you could set up a GitHub Actions workflow or use a pre-push hook that triggers invalidation asynchronously.
