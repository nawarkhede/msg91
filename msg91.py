import requests


class Msg91(object):

    def __init__(self, authkey=None):
        if not authkey:
            raise Exception
        self.authkey = authkey

    def send_message(self, message, mobiles, route, sender, country):
        """
        this method uses GET request.
        :param message:
        :param mobiles:
        :param route:
        :param sender:
        :param country:
        :return:
        """
        url = 'http://api.msg91.com/api/sendhttp.php'
        response = requests.get(
            url, params={
                'message': message,
                'mobiles': mobiles,
                'route': route,
                'sender': sender,
                'country': country,
                'authkey': self.authkey,
            }
        )
        return response.status_code, response.content

    def change_password(self, cur_password, new_password):
        """

        :param cur_password:
        :param new_password:
        :return:
        """
        url = 'http://api.msg91.com/api/password.php'
        response = requests.get(
            url, params={
                'password': cur_password,
                'newpass': new_password,
                'new_pass2': new_password,
                'authkey': self.authkey,
            }
        )
        return response.status_code, response.content

    def check_balance(self):
        """

        :return:
        """
        url = 'http://control.msg91.com/api/balance.php'
        response = requests.get(
            url, params={
                'type': 4,
                'authkey': self.authkey
            }
        )
        return response.status_code, response.content

    def check_authkey(self):
        """

        :return:
        """
        url = 'http://api.msg91.com/api/validate.php'
        response = requests.get(
            url, params={
                'authkey': self.authkey
            }
        )
        return response.status_code, response.content

    def send_message_v2(self, message1, message2, mobiles1, mobiles2):
        """

        :param message1:
        :param message2:
        :param mobiles1:
        :param mobiles2:
        :return:
        """
        url = 'http://api.msg91.com/api/v2/sendsms'
        data = {
            'sender': 'SOCKET',
            'route': 4,
            'country': 91,
            'sms': [
                {
                    'message': message1,
                    'to': mobiles1
                },
                {
                    'message': message2,
                    'to': mobiles2
                }
            ]
        }
        response = requests.post(
            url, headers={
                'authkey': self.authkey,
                'Content-Type': 'application/json'
            }, data=data
        )
        return response.status_code, response.content
