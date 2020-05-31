import web, json, tempfile

from passporteye import read_mrz

urls = ("/ocr/.*", "RequestHandler")
app = web.application(urls, globals())

class hello:
        def GET(self):
                    return 'Hello, world!'

class RequestHandler(object):
        def POST(self):
                # try:
                        data = web.data()  
                        newfile = tempfile.NamedTemporaryFile(mode='w+b',delete=False)
                        newfile.write(data)
                        print(newfile.name)
                        mrz = read_mrz(newfile.name,extra_cmdline_params="--oem 0 -l eng")
                        if mrz is None:
                                mrz_data = {} 
                        else:
                                mrz_data = mrz.to_dict()

                        newfile.close()
                        
                        print(json.dumps(mrz_data))
                        return(json.dumps(mrz_data))
                # except:
                #     pass

if __name__ == "__main__":
        app.run()
