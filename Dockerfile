FROM python:3.8-slim
COPY . /selenium_demo
WORKDIR /selenium_demo
RUN pip install --no-cache-dir -r requirements.txt
RUN ["pytest", "tests", "--browser=chrome", "-v", "--junitxml=reports/result_chrome.xml", "--html=reports/report_chrome.html"]
RUN ["pytest", "tests", "--browser=firefox", "-v", "--junitxml=reports/result_firefox.xml", "--html=reports/report_firefox.html"]
CMD tail -f /dev/null