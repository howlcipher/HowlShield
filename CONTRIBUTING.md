# Contributing

Use a milestone branch and signed Conventional Commits. Open a pull request
with the acceptance criteria, reproducible commands, observed outcomes and
known limitations. Merge requires an approving review and resolved threads.

Use synthetic or public, appropriately licensed research material. Keep
private documents, credentials and personal data out of issues and fixtures.
Record tool and corpus versions before comparing results.

## Owner approval of agent-authored changes

Open agent-authored pull requests through a dedicated GitHub App installation
scoped to HowlShield. The app needs pull request write permission to open PRs
and contents write permission only if it also pushes feature branches. Keep
its credentials in the configured secret store and use short-lived
installation tokens.

Before submitting an owner review through an agent, identify the repository,
pull request number and full head commit. Obtain William's explicit approval
of that revision. Recheck the head and authenticated reviewer immediately
before submission. Use the owner-authenticated connection to submit the
review with that commit ID and verify GitHub recorded it. If the revision
changes, request fresh approval. Keep independent audit findings in the PR
evidence and use GitHub auto-merge to apply branch protection.

The app must be installed before using this workflow. Pull requests authored
by the owner account require another eligible reviewer.
