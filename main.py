#!/usr/bin/env python3

import requests


API_URL='https://api.tmsandbox.co.nz/v1/Categories/6327/Details.json?catalogue=false'


class ValidateApi(object):
    def __init__ (self):
        self.api=None
        self.uname=None
        self.upassword=None
        self.response=None

    def run_get(self,api, username='', password=''):
        self.api=api
        self.uname=username
        self.upassword=password
        self.response=requests.get(self.api)
        self.validate_acceptance()

    def validate_acceptance(self):
        output = self.response.json()
        status = self.response.status_code
        valid = False

        try:
            # Criterion 1: Name = "Carbon credits"
            assert (output["Name"] == "Carbon credits")

            #CanRelist = true
            assert (output["CanRelist"] == True)

            #Condition 3: Promotions element with Name = "Gallery" has a Description that contains the text "2x larger image"
            count = 0
            if output.get("Promotions"):
                for i in output["Promotions"]:
                    if (i["Name"] == "Gallery"):
                        assert ("2x larger image" in i["Description"])
                        count += 1
                        valid = True
            print ("Total Promotion conditions matched :", count)
        except Exception as exp:
            print(repr(exp))
        finally:
            print("API Valid: ", valid)
            return valid

if __name__=='__main__':
    vapi =  ValidateApi()
    vapi.run_get(API_URL)


