# coding=gbk
import base64

def pictopy(picture_names, py_name):

    write_data = []
    for picture_name in picture_names:
        filename = picture_name.replace('.', '_')
        open_pic = open("%s" % picture_name, 'rb')
        b64str = base64.b64encode(open_pic.read())
        open_pic.close()
        write_data.append('%s = "%s"\n' % (filename, b64str.decode()))

    f = open('%s.py' % py_name, 'w+')
    for data in write_data:
        f.write(data)
    f.close()

if __name__ == '__main__':
    pic = ["yagi_antenna.png"]
    pictopy(pic, 'memory_pic')
    print("ok")
