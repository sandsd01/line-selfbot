# LINE SELFBOT - [![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fdnswd%2Fline-selfbot&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)
A bot to manage groups. As for now only have `@everyone` command that will tag every member in your group.

## requirements
This project was written on Python 3.8.5  
Install all dependencies using `pip install -r requirements.txt`

## Usage
You can login to your account using one of three ways: token, password, and QR Code.  
If the `EMAIL_ID` and `PASSWORD` environment value is not empty, this bot will try to login using EMAIL/ID and password. If not, then the bot will try to read `TOKEN` environment value and login using token.  

If all three value are empty, it will generate and prints an authentication link and a QR Code. You can open the link on you mobile phone, or scan the QR Code using your Line Messenger App. Both link and QR Code only valid for 2 minutes.

### Deploy  
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/dnswd/line-selfbot/tree/master)  

### Local
`python app.py` or `python3 app.py`

## Disclaimer
Please note that by using a selfbot, you're using an unofficial Line Messenger API, thus risking your account to be blocked and your phone number to be permanently banned from the service.

There's also [Account Regulatory](https://github.com/Dosugamea/l-api-tips/wiki/Account-Regulatory).

I am not responsible for any kind of loss involving this project.

## License
This is free and unencumbered public domain software. For more information, see https://unlicense.org/ or the accompanying [UNLICENSE](https://github.com/dnswd/line-selfbot/blob/master/UNLICENSE) file.