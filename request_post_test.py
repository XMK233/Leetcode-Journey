import requests, json

last_page = 510
sortedBy = "hottest"

payload = '[[""], [[], [], [], [], []], [["{}", 100, true]]]'.format('0,174,"tensorflow/efficientdet/lite0/detection/1"') ## "[\"cma:po\", \"\", \"{}\", 100, true, [[\"subtype\", [\"module\", \"placeholder\"]]], null, [], null, []]"##'{"page":%d,"group":"public","size":"all","fileType":"all","license":"all","viewed":"all","categoryIds":[],"search":"","sortBy":"%s","userId":null,"competitionId":null,"organizationId":null,"maintainerOrganizationId":null,"minSize":null,"maxSize":null,"isUserQuery":false,"hasTasks":false,"topicalDataset":null,"includeTopicalDatasets":false}'  ## "{\"page\":%d,\"group\":\"public\",\"size\":\"all\",\"fileType\":\"all\",\"license\":\"all\",\"viewed\":\"all\",\"categoryIds\":[],\"search\":\"\",\"sortBy\":\"%s\",\"userId\":null,\"organizationId\":null,\"maintainerOrganizationId\":null,\"minSize\":null,\"maxSize\":null,\"isUserQuery\":false,\"hasTasks\":false}"
headers = {
    'content-type': "application/json",
    # 'cookie': 'ka_sessionid=300ac300f45959eea5cdbfcf6a79f43e; _ga=GA1.2.1234651322.1614056813; GCLB=CK_Q2sC22PKl_AE; CSRF-TOKEN=CfDJ8LdUzqlsSWBPr4Ce3rb9VL-U-YFvdLs-D0c1OYFUKiQhrabUIDLZQBNTNulPVEvXzGWx586Qr0nENJabvDXywRCF97DRMxIsXOIU9r-2Qqa6DtkHv9seavn8mZ5Atf505y2-B_ffiX7ASuUuc2vaFVc; _gid=GA1.2.1707050155.1616305142; XSRF-TOKEN=CfDJ8LdUzqlsSWBPr4Ce3rb9VL-PFO8doRN5qa7lYJjgYUdZE34nyqNT_TnnQBLzERTyzrgXY0_e7n7ArHUgDZ9e0WCdWfWamzcvCqxSovF3vsCLcsFl5hMzXqOdBeLnmvX2wcuTMCF72FP7I9dDY6eWZM8; CLIENT-TOKEN=eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJpc3MiOiJrYWdnbGUiLCJhdWQiOiJjbGllbnQiLCJzdWIiOm51bGwsIm5idCI6IjIwMjEtMDMtMjFUMDU6NDE6MDkuNTEwMTgyOVoiLCJpYXQiOiIyMDIxLTAzLTIxVDA1OjQxOjA5LjUxMDE4MjlaIiwianRpIjoiZGY1NTBhMTgtYjIyNi00OTI2LWJjZWQtNWJjODY2OTIzODhlIiwiZXhwIjoiMjAyMS0wNC0yMVQwNTo0MTowOS41MTAxODI5WiIsImFub24iOnRydWUsImZmIjpbIkRvY2tlck1vZGFsU2VsZWN0b3IiLCJBY3RpdmVFdmVudHMiLCJHY2xvdWRLZXJuZWxJbnRlZyIsIktlcm5lbEVkaXRvckNvcmdpTW9kZSIsIkNhaXBFeHBvcnQiLCJDYWlwTnVkZ2UiLCJLZXJuZWxzQWRqdXN0QmFzZVBhdGgiLCJLZXJuZWxzRmlyZWJhc2VMb25nUG9sbGluZyIsIktlcm5lbHNQcmV2ZW50U3RvcHBlZFRvU3RhcnRpbmdUcmFuc2l0aW9uIiwiRGF0YXNldExpdmVNb3VudCIsIkRhdGFzZXRzVGFza09uTm90ZWJvb2tMaXN0aW5nIiwiRGF0YXNldHNEYXRhRXhwbG9yZXJWM1RyZWVMZWZ0IiwiQXZhdGFyUHJvZmlsZVByZXZpZXciLCJEYXRhc2V0c0RhdGFFeHBsb3JlclYzQ2hlY2tGb3JVcGRhdGVzIiwiRGF0YXNldHNEYXRhRXhwbG9yZXJWM0NoZWNrRm9yVXBkYXRlc0luQmFja2dyb3VuZCIsIktlcm5lbHNTdGFja092ZXJmbG93U2VhcmNoIiwiS2VybmVsc01hdGVyaWFsTGlzdGluZyIsIkRhdGFzZXRzTWF0ZXJpYWxEZXRhaWwiLCJEYXRhc2V0c01hdGVyaWFsTGlzdENvbXBvbmVudCIsIkNvbXBldGl0aW9uRGF0YXNldHMiLCJEaXNjdXNzaW9uc1Vwdm90ZVNwYW1XYXJuaW5nIiwiVGFnc0V4cGVyaW1lbnRVSSIsIlRhZ3NMZWFybkFuZERpc2N1c3Npb25zVUkiLCJOb1JlbG9hZEV4cGVyaW1lbnQiLCJOb3RlYm9va3NMYW5kaW5nUGFnZSIsIkRhdGFzZXRzRnJvbUdjcyIsIlRQVUNvbW1pdFNjaGVkdWxpbmciLCJEaXNjdXNzaW9uS01Gb3J1bVBhZ2UiLCJEaXNjdXNzaW9uS01Db21wZXRpdGlvbnMiLCJEaXNjdXNzaW9uS01EYXRhc2V0cyIsIkRpc2N1c3Npb25LTVRhZ3MiLCJEaXNjdXNzaW9uS01BYlRlc3QiLCJLZXJuZWxzTGVzc1JhcGlkQXV0b1NhdmUiXSwicGlkIjoia2FnZ2xlLTE2MTYwNyIsInN2YyI6IndlYi1mZSIsInNkYWsiOiJBSXphU3lEQU5HWEZIdFNJVmM1MU1JZEd3ZzRtUUZnbTNvTnJLb28iLCJibGQiOiJiMDhjN2VhZjI5YTI5YzAxNjIyNjgyMzkzYjQ0YzU1MjlkODgzYTA2In0.',
    # 'x-xsrf-token': 'CfDJ8LdUzqlsSWBPr4Ce3rb9VL-PFO8doRN5qa7lYJjgYUdZE34nyqNT_TnnQBLzERTyzrgXY0_e7n7ArHUgDZ9e0WCdWfWamzcvCqxSovF3vsCLcsFl5hMzXqOdBeLnmvX2wcuTMCF72FP7I9dDY6eWZM8',
}
print(payload)
response1 = requests.request("POST", "https://tfhub.dev/s/list", data = payload, headers = headers)
print(response1)
infos = json.loads(response1.text)
print(infos)

# totalNum = 0
# while True:
#     response1 = requests.request("POST", "https://www.kaggle.com/requests/SearchDatasetsRequest",
#                                          data=payload % (last_page, sortedBy), headers=headers)
#     infos = json.loads(response1.text)
#     coreLen = len(infos["result"]["datasetList"]["items"])
#     totalNum += coreLen
#     if coreLen == 0:
#         break
#     print(last_page * 20)
#     last_page += 1