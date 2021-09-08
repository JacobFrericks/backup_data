## Export and Import GPG keys
1. On your local computer, run `gpg --armor --output import.gpg --export $YOUR_EMAIL`
1. Copy `import.gpg` to the aws instance
1. On the EC2 instance, run `gpg --import import.gpg`