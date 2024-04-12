Store module packages when SageMaker instance is offline:

When users work on Python scripts, they often require downloading module packages. While they can download these packages, they encounter an issue when the SageMaker instance transitions from a stopped to an online state: the installed packages disappear. Consequently, users need to reinstall these packages upon resuming work. I seek guidance on an effective solution approach to address this challenge.
