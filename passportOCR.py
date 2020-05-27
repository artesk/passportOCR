import web, json, tempfile

from passporteye import read_mrz

urls = ("/ocr/.*", "RequestHandler")
app = web.application(urls, globals())

class hello:
        def GET(self):
                    return 'Hello, world!'

class RequestHandler(object):
        def POST(self):
                try:
                    data = web.data() # you can get data use this method
                    newfile = tempfile.NamedTemporaryFile(mode='w+b')
                    newfile.write(data)


                    mrz = read_mrz(newfile.name)
                    newfile.close()
                    mrz_data = mrz.to_dict()
                    return(json.dumps(mrz_data))
                except:
                    pass


if __name__ == "__main__":
        app.run()
