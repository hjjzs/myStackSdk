import openstack

conn = openstack.connect(
    auth_url="http://10.255.9.202:5000/v3",
    username="admin",
    password="000000",
    user_domain_name="demo"
)


def list_volumes():
    v = conn.volume.volumes()
    for i in v:
        print(i)


def find_volume():
    v = conn.volume.find_volume("py")
    print(v)


def get_volume():
    v = conn.volume.get_volume("c2d54e3c-875b-400a-8609-a200d5f4fa80")
    print(v)

def create_volume():
    v = conn.volume.create_volume(name="py", size=4)
    print(v)


if __name__ == '__main__':
    # list_volumes()
    find_volume()
    get_volume()

    # create_volume()