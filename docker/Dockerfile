FROM python:3.10-slim as builder
COPY requirements/requirements.txt /requirements.txt
RUN pip install --user -r /requirements.txt \
  && rm -rf ~/.cache/pip

FROM python:3.10-slim
LABEL maintainer="Alice Support <support@alicebiometrics.com>"
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY ./app /app/app
EXPOSE 80
CMD ["/root/.local/bin/uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]