#this code is written for google cloud platform - cloud functions it it written in flask
# Entry point is set to this function 

def main(request):
    from requests import get as G
    from time import perf_counter_ns as t
    import json
    headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600'
        }
    if request.method == 'OPTIONS':
        return ('', 204, headers)
    elif request.method == 'POST':
        try:
            proto = ["http","https"] 
            a  = json.loads(request.get_data())
            if a['url'].split(":")[0] not in proto:
                a['url'] = "http://"+a['url']
            start = t()
            x = G(a['url'])
            end = t()
            return ({"code":x.status_code ,"timetaken":(end-start)/1000000},200, headers)
        except:
            return({'code':404 ,"message":"url not found"},200,headers)

    elif request.method == "GET":
        return {"dev":"github.com/xxparthparekhxx"}
