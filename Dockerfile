FROM python:3

ADD CampaignHelper.py /

RUN pip install discord.py
RUN pip install python-dotenv

CMD [ "python", "./CampaignHelper.py" ]
