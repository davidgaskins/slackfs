# slackfs
The slowest minimal fs you are likely to ever see. 


To run:
  1. Get the token for your slack url and place it into 'credentials.hideme' (*.hideme is in the .gitignore)
  2. vagrant up
  3. vagrant ssh
  4. python2 slackfs.py [mountpoint]

Basically a mirror of Roger Howards IssueFS https://github.com/rogerhoward/issuefs/, I just subbed out github APIs for slack ones.
