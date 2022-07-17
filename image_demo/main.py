import openstack

con = openstack.connect(
    auth_url="http://10.255.9.193:5000/v3",
    username="admin",
    password="000000",
    user_domain_name="demo",
    )

# image = con.image.get_image("5e50eb70-d648-4263-ac14-42ed474454fd")
# print(image.to_dict())

# 通过名字获取镜像
# image = con.image.find_image("test22")
# print(dict(image))

# 删除镜像
# de = con.image.delete_image(image)
# print(de)
#

# 列出所有镜像
# images = con.image.images()
# for i in images:
#     print(dict(i)["name"])

# 创建镜像
url = "http://10.255.9.137/cirros-0.3.4-x86_64-disk.img"
image = con.image.create_image(name='python', disk_format='qcow2', container_format='bare', visibility="public")
con.image.import_image(image, method="web-download", uri=url)

# 创建镜像
# image = con.image.upload_image(container_format="bare",
#                                disk_format="qcow2",
#                                data=open(r"C:\Users\603\Downloads\CentOS-8-GenericCl"
#                                          r"oud-8.1.1911-20200113.3.x86_64.qcow2", "rb"),
#                                name="test22")
# print(image)
#
# 创建镜像
# image5 = con.image.create_image(name='python22', disk_format='qcow2', container_format='bare', visibility="public")
# d = con.image.stage_image(image5, filename=r"C:\Users\603\Downloads\CentOS-8-GenericCl"
#                                            r"oud-8.1.1911-20200113.3.x86_64.qcow2")
# print(d)



