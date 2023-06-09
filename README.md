# Overview

In this project, I was tired of checking results every few seconds. So, I started working on this script that was written in python to web scrape my university results website and check if there's a new result so it can notify me by sending me an email.
Initially, I self hosted this script on my labtop but later i found that it's not handy. So, I looked for a free hosting providers. At the end I chose Heroku.


### Prerequisites

- *Requests*\
Get the grades via HTTP requests\
```pip install requests```

- *BeautifulSoup*\
 Web scraping library for pulling the data from HTML \
```pip install beautifulsoup4```

- *Email*\
Python’s built-in email package to Send emails

- [Heroku](https://www.heroku.com/) [Optional] \
Platform that enables developers to build, run, and operate applications entirely in the cloud.



### Run Locally

1. Clone the project

```bash
  git clone https://github.com/itsOsamasaid/Results-Checker
```

2. Go to the project directory

```bash
  cd Results-Checker
```

3. Start it

```bash
  Python3 CheckGrades.py
```
## Screenshots
![Result](https://github.com/itsOsamasaid/Results-Checker/blob/main/Result.png)



