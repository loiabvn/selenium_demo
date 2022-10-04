FROM python:3.8-slim
COPY . /selenium_demo
WORKDIR /selenium_demo
RUN pip install --no-cache-dir -r requirements.txt
RUN ["pytest", "tests", "-v", "--junitxml=reports/result.xml", "--html=reports/report.html", "-s"]
CMD tail -f /dev/null